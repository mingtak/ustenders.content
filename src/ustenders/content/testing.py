# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import ustenders.content


class UstendersContentLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=ustenders.content)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'ustenders.content:default')


USTENDERS_CONTENT_FIXTURE = UstendersContentLayer()


USTENDERS_CONTENT_INTEGRATION_TESTING = IntegrationTesting(
    bases=(USTENDERS_CONTENT_FIXTURE,),
    name='UstendersContentLayer:IntegrationTesting'
)


USTENDERS_CONTENT_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(USTENDERS_CONTENT_FIXTURE,),
    name='UstendersContentLayer:FunctionalTesting'
)


USTENDERS_CONTENT_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        USTENDERS_CONTENT_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='UstendersContentLayer:AcceptanceTesting'
)
