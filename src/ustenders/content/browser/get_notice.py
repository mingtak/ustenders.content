# -*- coding: utf-8 -*-

from Products.Five.browser import BrowserView
import urllib2
import md5
from plone import api
import transaction
from DateTime import DateTime
from datetime import date
from plone.app.textfield.value import RichTextValue
from zope import component
from zope.app.intid.interfaces import IIntIds
from z3c.relationfield import RelationValue
from zope.event import notify
from zope.lifecycleevent import ObjectModifiedEvent
from Products.CMFPlone.utils import safe_unicode


FTP_STRING_HEADER = "ftp://ftp.fbo.gov/FBOFeed"
CONTENT_TYPE_LIST = [
    'MOD',
    'SNOTE',
    'SRCSGT',
    'AWARD',
    'COMBINE',
    'AMDCSS',
    'UNARCHIVE',
    'JA',
    'FAIROPP',
    'ARCHIVE',
    'PRESOL',]

ATTRIBUTE_LIST = [
    'AWDNBR',
    'OFFICE',
    'NAICS',
    'AWARDEE',
    'MODNBR',
    'FOJA',
    'CONTACT',
    'LINK',
    'DATE',
    'LINENBR',
    'CLASSCOD',
    'NTYPE',
    'EMAIL',
    'LOCATION',
    'ARCHDATE',
    'ZIP',
    'POPCOUNTRY',
    'URL',
    'POPZIP',
    'POPADDRESS',
    'STAUTH',
    'DONBR',
    'SSALE',
    'YEAR',
    'DESC',
    'SETASIDE',
    'OFFADD',
    'AGENCY',
    'RESPDATE',
    'AWDAMT',
    'AWDDATE',
    'SOLNBR',
    'SUBJECT',]


class GetNotice(BrowserView):

    def creat_notice(self, contentTypeName, noticeContent):
        portal = api.portal.get()
        catalog = portal.portal_catalog
        intIds = component.getUtility(IIntIds)

        # 擷取屬性，使用dict
        attributes = {}
        for line in noticeContent.split('\n'):
            # 確認是否最後一行
            if not line:
                continue
            if '<%s>' % contentTypeName in line:
                continue
            if '</%s>' % contentTypeName in line:
                break

            if line.strip().startswith('<') and '>' in line and line.split('>')[0].split('<')[1] in ATTRIBUTE_LIST:
                attributeName = line.split('>')[0].split('<')[1]
                attributeContent = line.split('>')[1]
                if attributeName == 'DESC' and attributeContent.startswith('Link To Document') :
                    continue
                attributes[attributeName] = '%s' % attributeContent
                continue
            else:
                try:
                    attributes[attributeName] += '</br>%s' % attributeContent
                except:
                    return
        timeString = DateTime().strftime('%Y%m%d_%s')
        contentTypeName = '%s%s' % (contentTypeName[0], contentTypeName[1:].lower())


        # check this notice not exists
        if catalog(md5=md5.new(str(attributes)).hexdigest()):
            return

        object = api.content.create(
            container=portal[contentTypeName.lower()],
            type=contentTypeName,
            safe_id=True,
            title=safe_unicode(attributes.get('SUBJECT', timeString)),
        )

#        import pdb; pdb.set_trace()

        metaDescription = {}
        metaDescription['subject'] = object.Title()

        object.noticeTypeName = object.getParentNode().Title()

        try:
            # attributes['YEAR'] 只有二位數字，前方補20
            year = int('20%s' % attributes['YEAR'])
            month = int(attributes['DATE'][0:2])
            day = int(attributes['DATE'][2:])
            object.date = date(year, month, day)
            metaDescription['date'] = object.date
        except:
            pass

        object.agency = attributes.get('AGENCY')
        if object.agency:
            metaDescription['agency'] = object.agency
        object.office = attributes.get('OFFICE')
        object.ntype = attributes.get('NTYPE')
        if object.ntype:
            metaDescription['ntype'] = object.ntype
        object.email = attributes.get('EMAIL')
        object.location = attributes.get('LOCATION')
        object.zip = attributes.get('ZIP')


        if attributes.get('CLASSCOD'):
            brain = catalog(pCode=attributes.get('CLASSCOD'))
            if brain:
                pCodeObject = brain[0].getObject()
                object.classcod = RelationValue(intIds.getId(pCodeObject))

        if attributes.get('NAICS'):
            brain = catalog(naicsCode=attributes.get('NAICS'))
            if brain:
                naicsObject = brain[0].getObject()
                object.naics = RelationValue(intIds.getId(naicsObject))

#        object.classcod = attributes.get('CLASSCOD')
#        object.naics = attributes.get('NAICS')


        object.offadd = attributes.get('OFFADD')
        object.solnbr = attributes.get('SOLNBR')

        try:
            # attributes['RESPDATE'] format: mmddyy
            year = int('20%s' % attributes['RESPDATE'][4:])
            month = int(attributes['RESPDATE'][0:2])
            day = int(attributes['RESPDATE'][2:4])
            object.respdate = date(year, month, day)
        except:
            pass

        object.contact = attributes.get('CONTACT')

        # desc is a RichText field
        object.desc = RichTextValue(attributes.get('DESC'))

        object.link = attributes.get('LINK')
        object.url = attributes.get('URL')
        object.setAside = attributes.get('SETASIDE')
        object.popcountry = attributes.get('POPCOUNTRY')
        object.popaddress = attributes.get('POPADDRESS')
        object.awdnbr = attributes.get('AWDNBR')
        object.awardee = attributes.get('AWARDEE')
        object.modnbr = attributes.get('MODNBR')
        object.foja = attributes.get('FOJA')
        object.linenbr = attributes.get('LINENBR')

        try:
            # attributes['ARCHDATE'] format: mmddyyyy
            year = int(attributes['ARCHDATE'][4:])
            month = int(attributes['ARCHDATE'][0:2])
            day = int(attributes['ARCHDATE'][2:4])
            object.archdate = date(year, month, day)
        except:
            pass

        object.stauth = attributes.get('STAUTH')
        object.donbr = attributes.get('DONBR')
        object.awdamt = attributes.get('AWDAMT')

        try:
            # attributes['AWDDATE'] format: mmddyy
            year = int('20%s' % attributes['AWDDATE'][4:])
            month = int(attributes['AWDDATE'][0:2])
            day = int(attributes['AWDDATE'][2:4])
            object.archdate = date(year, month, day)
        except:
            pass

        object.subject_ = attributes.get('SUBJECT')

        # md5 checksum
        object.md5 = md5.new(str(attributes)).hexdigest()

        metaString = ''
        if metaDescription.has_key('date'):
            metaString += 'Announcement at %s, ' % metaDescription['date']
        metaString += 'and subject is %s, ' % metaDescription['subject']
        if metaDescription.has_key('agency'):
            metaString += 'from %s, ' % metaDescription['agency']
        if metaDescription.has_key('ntype'):
            metaString += 'notice category is %s.' % metaDescription['ntype']
        object.description = metaString

#        import pdb; pdb.set_trace()
        notify(ObjectModifiedEvent(object))
        object.reindexObject()
        transaction.commit()


    def __call__(self):

        context = self.context
        request = self.request

        date = DateTime()
        while True:
            dateString = date.strftime('%Y%m%d')
            ftpString = '%s%s' % (FTP_STRING_HEADER, dateString)
            try:
                responseDoc = urllib2.urlopen(ftpString)
                break
            except:
                date = date - 1
                pass

        doc = responseDoc.read()

        noticeContent = ''
        for line in doc.split('\n'):
            noticeContent += '%s\n' % line
            if '</' == line[0:2] and '>' in line:
#                try:
                tagName = line.split('</')[1].split('>')[0]
                if tagName in CONTENT_TYPE_LIST:
                    contentTypeName = tagName
                    self.creat_notice(contentTypeName, noticeContent)
                    noticeContent = ''
#                except:
#                    continue
            else:
                continue
