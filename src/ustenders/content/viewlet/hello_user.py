from plone.app.layout.viewlets import common as base
from plone import api


class HelloUserViewlet(base.ViewletBase):
    """ """

    def get_portal(self):
        return api.portal.get()

    def is_anonymous(self):
        return api.user.is_anonymous()

    def get_current(self):
        return api.user.get_current()
