from Products.Five.browser import BrowserView
from plone import api


from Acquisition import aq_inner
from zope.component import getUtility
from zope.intid.interfaces import IIntIds
from zope.security import checkPermission
from zc.relation.interfaces import ICatalog


def back_references(source_object, attribute_name):
    """ Return back references from source object on specified attribute_name """
    catalog = getUtility(ICatalog)
    intids = getUtility(IIntIds)
    result = []
    for rel in catalog.findRelations(
                            dict(to_id=intids.getId(aq_inner(source_object)),
                                 from_attribute=attribute_name)
                            ):
        obj = intids.queryObject(rel.from_id)
        if obj is not None and checkPermission('zope2.View', obj):
            result.append(obj)
    return result



class PloneApi(object):

    def get_state(self, item):
        return api.content.get_state(item)


class ClassCodeView(BrowserView, PloneApi):
    """ ClassCode View (default)
    """
    def get_back_references(self):
        context = self.context
        return back_references(context, 'classcod')



class NaicsView(BrowserView, PloneApi):
    """ Naics View (default)
    """
    def get_back_references(self):
        context = self.context
        return back_references(context, 'naics')


    def get_next_level(self):
        context = self.context
        catalog = context.portal_catalog
        naicsLen = len(context.naicsCode)
        if naicsLen >= 5:
            queryLen = 6
        else:
            queryLen = naicsLen + 2
        indexKey = 'naics_%s' % naicsLen

        if naicsLen == 6:
            return None
        return catalog({'type':context.Type(), indexKey:context.naicsCode, 'naicsLen':queryLen},
                       sort_on='created', sort_order='reverse')


class ModView(BrowserView, PloneApi):
    """ Mod View (default)
    """
    def get_back_references(self):
        context = self.context
        return back_references(context, 'relatedItem')


class SnoteView(BrowserView, PloneApi):
    """ Snote View (default)
    """
    def get_back_references(self):
        context = self.context
        return back_references(context, 'relatedItem')



class SrcsgtView(BrowserView, PloneApi):
    """ Srcsgt View (default)
    """
    def get_back_references(self):
        context = self.context
        return back_references(context, 'relatedItem')


class AwardView(BrowserView, PloneApi):
    """ Award View (default)
    """
    def get_back_references(self):
        context = self.context
        return back_references(context, 'relatedItem')


class CombineView(BrowserView, PloneApi):
    """ Combine View (default)
    """
    def get_back_references(self):
        context = self.context
        return back_references(context, 'relatedItem')


class AmdcssView(BrowserView, PloneApi):
    """ Amdcss View (default)
    """
    def get_back_references(self):
        context = self.context
        return back_references(context, 'relatedItem')


class UnarchiveView(BrowserView, PloneApi):
    """ Unarchive View (default)
    """
    def get_back_references(self):
        context = self.context
        return back_references(context, 'relatedItem')


class JaView(BrowserView, PloneApi):
    """ Ja View (default)
    """
    def get_back_references(self):
        context = self.context
        return back_references(context, 'relatedItem')


class FairoppView(BrowserView, PloneApi):
    """ Fairopp View (default)
    """
    def get_back_references(self):
        context = self.context
        return back_references(context, 'relatedItem')


class ArchiveView(BrowserView, PloneApi):
    """ Archive View (default)
    """
    def get_back_references(self):
        context = self.context
        return back_references(context, 'relatedItem')


class PresolView(BrowserView, PloneApi):
    """ Presol View (default)
    """
    def get_back_references(self):
        context = self.context
        return back_references(context, 'relatedItem')


class DiscussView(BrowserView, PloneApi):
    """ Discuss View (default)
    """


class DocumentHeroView(BrowserView, PloneApi):
    """ Document Hero View
    """

