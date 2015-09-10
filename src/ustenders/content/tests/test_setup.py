# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from ustenders.content.testing import USTENDERS_CONTENT_INTEGRATION_TESTING  # noqa
from plone import api

import unittest2 as unittest


class TestSetup(unittest.TestCase):
    """Test that ustenders.content is properly installed."""

    layer = USTENDERS_CONTENT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if ustenders.content is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('ustenders.content'))

    def test_browserlayer(self):
        """Test that IUstendersContentLayer is registered."""
        from ustenders.content.interfaces import IUstendersContentLayer
        from plone.browserlayer import utils
        self.assertIn(IUstendersContentLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = USTENDERS_CONTENT_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['ustenders.content'])

    def test_product_uninstalled(self):
        """Test if ustenders.content is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled('ustenders.content'))

    def test_browserlayer_removed(self):
        """Test that IUstendersContentLayer is removed."""
        from ustenders.content.interfaces import IUstendersContentLayer
        from plone.browserlayer import utils
        self.assertNotIn(IUstendersContentLayer, utils.registered_layers())
