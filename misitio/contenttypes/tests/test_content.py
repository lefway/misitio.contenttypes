import unittest2 as unittest

from Products.CMFCore.utils import getToolByName
from misitio.utilities.utility import createConcejoComunal

from misitio.contenttypes.testing import\
    MISITIO_CONTENTTYPES_INTEGRATION_TESTING

from plone.app.testing import TEST_USER_ID, TEST_USER_NAME
from plone.app.testing import (
   login, setRoles,
   )
#from plone.dexterity.utils import createContent


class TestContent(unittest.TestCase):

    layer = MISITIO_CONTENTTYPES_INTEGRATION_TESTING
    
    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.types = getToolByName(self.portal, 'portal_types')
        self.qi_tool = getToolByName(self.portal, 'portal_quickinstaller')

    def test_product_is_installed(self):
        """ Validate that our products GS profile has been run and the product 
            installed
        """
        pid = 'misitio.contenttypes'
        installed = [p['id'] for p in self.qi_tool.listInstalledProducts()]
        self.assertTrue(pid in installed,
                        'package appears not to have been installed')


    def test_contenttypes_is_registed_contenttypes(self):
        existing = self.types.objectIds()

        self.assertTrue('concejo_comunal' in existing)
        self.assertTrue('miembro' in existing)


    def test_consejo_comunal_allowed_content_types(self):

       setRoles(self.portal, TEST_USER_ID, ['Manager'])
       login(self.portal, TEST_USER_NAME)
       createConcejoComunal(self.portal,'tipitiripe')
       self.assertTrue('tipitiripe' in self.portal, 'tipitiripe ConcejoComunal not created.')
       setRoles(self.portal, TEST_USER_ID, ['Member'])
       cc = self.portal['tipitiripe']
       self.assertEqual(cc.getImmediatelyAddableTypes(), ['File', 'Image', 'Link', 'miembro'])

