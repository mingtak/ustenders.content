# -*- coding: utf-8 -*-

from ustenders.content import _
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.interface import Interface
from plone.z3cform.layout import wrap_form
from Products.statusmessages.interfaces import IStatusMessage
from z3c.form import button
from z3c.form import form, field
from zope import schema


class ISetProfile(Interface):

    email = schema.TextLine(
        title=_(u'Email'),
        description=_(u'Please fill in your e-mail address for the recipient.'),
    )

    keywords = schema.TextLine(
        title=_(u'Keywords'),
        description=_(u'Please fill out the keywords you want, to filter the results. One keyword per line.'),
        required=False
    )


class HelloWorldForm(form.Form):

    fields = field.Fields(ISetProfile)
    ignoreContext = True

    def updateWidgets(self):
#        import pdb; pdb.set_trace()
#        default初始值放這裏
        super(HelloWorldForm, self).updateWidgets()

    @button.buttonAndHandler(u'Save')
    def handleSave(self, action):
        data, errors = self.extractData()
        if errors:
            return False

        if data['hello_world_name'] is not None:
            hello_name = data['hello_world_name']
        else:
            hello_name = 'World'

        IStatusMessage(self.request).addStatusMessage(
            "Hello %s" % hello_name,
            'info')
        redirect_url = "%s/@@set_profile" % self.context.absolute_url()
        self.request.response.redirect(redirect_url)

    @button.buttonAndHandler(u'Cancel')
    def handleCancel(self, action):
        IStatusMessage(self.request).addStatusMessage(
            "Hello No One",
            'info')
        redirect_url = "%s/@@set_profile" % self.context.absolute_url()
        self.request.response.redirect(redirect_url)





from plone.z3cform.layout import wrap_form
HelloWorldFormView = wrap_form(HelloWorldForm)
