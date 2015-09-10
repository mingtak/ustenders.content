# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from ustenders.content import _
from zope import schema
from plone.autoform import directives as form
from plone.app.textfield import RichText
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from collective import dexteritytextindexer


class IUstendersContentLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""

from z3c.relationfield.schema import RelationList, RelationChoice

class INotice(Interface):

    title = schema.TextLine(
        title=_(u"Title"),
        required=True,
    )

    # 保留不用
    form.omitted('description')
    description = schema.Text(
        title=_(u"Description"),
        required=False,
    )

    # 保留不用
    form.omitted('noticeType')
    noticeType = schema.Text(
        title=_(u"Notice Type"),
        required=True,
    )

    noticeTypeName = schema.TextLine(
        title=_(u"Notice Type Name"),
        required=True,
    )

    date = schema.Date(
        title=_(u"Date/Year"),
        description=_(u"Include date & year"),
        required=False,
    )

    agency = schema.TextLine(
        title=_(u"Agency"),
        required=False,
    )

    office = schema.TextLine(
        title=_(u"Office"),
        required=False,
    )

    ntype = schema.TextLine(
        title=_(u"Ntype"),
        required=False,
    )

    email = schema.TextLine(
        title=_(u"Email"),
        required=False,
    )

    location = schema.TextLine(
        title=_(u"Location"),
        required=False,
    )

    zip = schema.TextLine(
        title=_(u"ZIP"),
        required=False,
    )
    """
    classcod = schema.TextLine(
        title=_(u"Classification Code"),
        required=False,
    )
    """
    classcod = RelationChoice(
        title=_(u"Classification Code"),
        vocabulary="plone.app.vocabularies.Catalog",
        required=False,
    )

    """
    naics = schema.TextLine(
        title=_(u"NAICS Code"),
        required=False,
    )"""

    naics = RelationChoice(
        title=_(u"NAICS Code"),
        vocabulary="plone.app.vocabularies.Catalog",
        required=False,
    )

    offadd = schema.TextLine(
        title=_(u"Office Address"),
        required=False,
    )

    solnbr = schema.TextLine(
        title=_(u"Solicitation Number"),
        required=False,
    )

    respdate = schema.Date(
        title=_(u"Response Date"),
        required=False,
    )

    contact = schema.TextLine(
        title=_(u"Contact"),
        required=False,
    )

    dexteritytextindexer.searchable('desc')
    desc = RichText(
        title=_(u"Description RichText"),
        required=False,
    )

    link = schema.URI(
        title=_(u"Link"),
        description=_(u"???"),
        required=False,
    )

    url = schema.URI(
        title=_(u"URL"),
        required=False,
    )

    setAside = schema.TextLine(
        title=_(u"Original Set Aside"),
        required=False,
    )

    popcountry = schema.TextLine(
        title=_(u"Pop Country"),
        required=False,
    )

    popaddress = schema.TextLine(
        title=_(u"Pop Address"),
        required=False,
    )

    awdnbr = schema.TextLine(
        title=_(u"Contract Award Number"),
        required=False,
    )

    awardee = schema.Text(
        title=_(u"Contractor Awarded Name & Address"),
        required=False
    )

    modnbr = schema.TextLine(
        title=_(u"Modification Number"),
        required=False,
    )

    foja = schema.TextLine(
        title=_(u"Fair Opportunity / Limited Sources Justification Authority"),
        required=False,
    )

    linenbr = schema.TextLine(
        title=_(u"Contract Line Item Number"),
        required=False,
    )

    archdate = schema.Date(
        title=_(u"Archive Date"),
        required=False,
    )

    stauth = schema.TextLine(
        title=_(u"J&A Statutory Authority"),
        required=False,
    )

    donbr = schema.TextLine(
        title=_(u"Task/Delivery Order Number"),
        required=False,
    )

    awdamt = schema.TextLine(
        title=_(u"Contract Award Dollar Amount"),
        required=False,
    )

    awddate = schema.Date(
        title=_(u"Contract Award Date"),
        required=False,
    )

    subject_ = schema.TextLine(
        title=_(u"Subject"),
        required=False,
    )

    md5 = schema.TextLine(
        title=_(u"Md5 Checksum"),
        required=True,
    )


class IMod(Interface, INotice):
    """ MOD content type """
    noticeTypeName = schema.TextLine(
        title=_(u"Notice Type Name"),
        default=_(u"Modified"),
        required=True,
    )


class ISnote(INotice):
    """ SNOTE content type """
    noticeTypeName = schema.TextLine(
        title=_(u"Notice Type Name"),
        default=_(u"Special Notice"),
        required=True,
    )


class ISrcsgt(INotice):
    """ SRCSGT content type """
    noticeTypeName = schema.TextLine(
        title=_(u"Notice Type Name"),
        default=_(u"Sources Sought"),
        required=True,
    )


class IAward(INotice):
    """ AWARD content type """
    noticeTypeName = schema.TextLine(
        title=_(u"Notice Type Name"),
        default=_(u"Award"),
        required=True,
    )


class ICombine(INotice):
    """ COMBINE content type """
    noticeTypeName = schema.TextLine(
        title=_(u"Notice Type Name"),
        default=_("Combined Synopsis/Solicitation"),
        required=True,
    )


class IAmdcss(INotice):
    """ AMDCSS content type """
    noticeTypeName = schema.TextLine(
        title=_(u"Notice Type Name"),
        default=_("Combined Synopsis/Solicitation (Modified)"),
        required=True,
    )


class IUnarchive(INotice):
    """ UNARCHIVE content type """
    noticeTypeName = schema.TextLine(
        title=_(u"Notice Type Name"),
        default=_("Unarchive"),
        required=True,
    )


class IJa(INotice):
    """ JA content type """
    noticeTypeName = schema.TextLine(
        title=_(u"Notice Type Name"),
        default=_("J&A Statutory Authority"),
        required=True,
    )


class IFairopp(INotice):
    """ FAIROPP content type """
    noticeTypeName = schema.TextLine(
        title=_(u"Notice Type Name"),
        default=_("Fair Opportunity"),
        required=True,
    )


class IArchive(INotice):
    """ ARCHIVE content type """
    noticeTypeName = schema.TextLine(
        title=_(u"Notice Type Name"),
        default=_("Archive"),
        required=True,
    )


class IPresol(INotice):
    """ PRESOL content type """
    noticeTypeName = schema.TextLine(
        title=_(u"Notice Type Name"),
        default=_("Presolicitation"),
        required=True,
    )


proc_code = SimpleVocabulary(
    [SimpleTerm(value=u'Service', title=_(u'Service')),
     SimpleTerm(value=u'Product', title=_(u'Product')),]
)

class IClassCode(Interface):

    """ Classification Code """

    title = schema.TextLine(
        title=_(u"Title"),
        required=True,
    )

    procurement = schema.Choice(
        title=_(u"Procurement Classification"),
        vocabulary=proc_code,
        required=True,
    )

    pCode = schema.TextLine(
        title=_(u"Classification Code"),
        required=True,
    )


class INaics(Interface):

    """ NAICS Code """

    title = schema.TextLine(
        title=_(u"Title"),
        required=True,
    )

    naicsCode = schema.TextLine(
        title=_(u"NAICS Code"),
        min_length=2,
        max_length=6,
        required=True,
    )
