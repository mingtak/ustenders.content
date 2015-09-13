# -*- coding: utf-8 -*-

from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class ByProduct(BrowserView):

    index = ViewPageTemplateFile("template/by_product.pt")

    def __call__(self):

        context = self.context
        request = self.request
        catalog = context.portal_catalog

        self.brain = catalog(procurement='Product', sort_on='id', sort_order='reverse')
        return self.index()
