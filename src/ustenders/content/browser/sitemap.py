# -*- coding: utf-8 -*-

from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class SitemapForGoogle(BrowserView):

    template = ViewPageTemplateFile('template/sitemap.pt')

    def __call__(self):

        request = self.request
        catalog = self.context.portal_catalog
        self.brain = catalog({'Type':['Award', 'Amdcss', 'Combine', 'Document',
                                      'Fairopp', 'Ja', 'Mod', 'Folder', 'Image',
                                      'Presol', 'Srcsgt', 'Snote', 'Discuss',]},
                              sort_on='modified',
                              sort_order='reverse')[:50000]
        return self.template()
