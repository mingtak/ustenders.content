# -*- coding: utf-8 -*-
from plone.app.testing import TEST_USER_ID
from zope.component import queryUtility
from zope.component import createObject
from plone.app.testing import setRoles
from plone.dexterity.interfaces import IDexterityFTI
from plone import api

from ustenders.content.testing import USTENDERS_CONTENT_INTEGRATION_TESTING  # noqa
from ustenders.content.interfaces import INotice

import unittest2 as unittest


class NoticeIntegrationTest(unittest.TestCase):

    layer = USTENDERS_CONTENT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='Notice')
        schema = fti.lookupSchema()
        self.assertEqual(INotice, schema)

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='Notice')
        self.assertTrue(fti)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='Notice')
        factory = fti.factory
        obj = createObject(factory)
        self.assertTrue(INotice.providedBy(obj))

    def test_adding(self):
        self.portal.invokeFactory('Notice', 'Notice')
        self.assertTrue(
            INotice.providedBy(self.portal['Notice'])
        )
