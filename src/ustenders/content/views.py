from Products.Five.browser import BrowserView
from plone import api

class PloneApi(object):

    def get_state(self, item):
        return api.content.get_state(item)


class ModView(BrowserView, PloneApi):
    """ Mod View (default)
    """


class SnoteView(BrowserView, PloneApi):
    """ Snote View (default)
    """


class SrcsgtView(BrowserView, PloneApi):
    """ Srcsgt View (default)
    """


class AwardView(BrowserView, PloneApi):
    """ Award View (default)
    """


class CombineView(BrowserView, PloneApi):
    """ Combine View (default)
    """


class AmdcssView(BrowserView, PloneApi):
    """ Amdcss View (default)
    """


class UnarchiveView(BrowserView, PloneApi):
    """ Unarchive View (default)
    """


class JaView(BrowserView, PloneApi):
    """ Ja View (default)
    """


class FairoppView(BrowserView, PloneApi):
    """ Fairopp View (default)
    """


class ArchiveView(BrowserView, PloneApi):
    """ Archive View (default)
    """


class PresolView(BrowserView, PloneApi):
    """ Presol View (default)
    """

