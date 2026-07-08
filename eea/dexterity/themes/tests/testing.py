"""Test layer for eea.dexterity.themes."""

from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile

import eea.dexterity.themes


class EeaDexterityThemesLayer(PloneSandboxLayer):
    """Test layer for eea.dexterity.themes."""

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        """Set up Zope."""
        import plone.app.dexterity

        self.loadZCML(package=plone.app.dexterity)
        self.loadZCML(package=eea.dexterity.themes)

    def setUpPloneSite(self, portal):
        """Set up Plone site."""
        applyProfile(portal, "eea.dexterity.themes:default")


EEA_DEXTERITY_THEMES_FIXTURE = EeaDexterityThemesLayer()

EEA_DEXTERITY_THEMES_INTEGRATION_TESTING = IntegrationTesting(
    bases=(EEA_DEXTERITY_THEMES_FIXTURE,),
    name="EeaDexterityThemesLayer:IntegrationTesting",
)
