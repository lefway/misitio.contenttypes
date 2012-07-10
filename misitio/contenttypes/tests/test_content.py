import unittest2 as unittest

from Products.CMFCore.utils import getToolByName

from misitio.contenttypes.testing import\
    MISITIO_CONTENTTYPES_INTEGRATION_TESTING


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

#    def test_consejo_comunal_allowed_content_types(self):
#        folder = self.types.objectIds()
# 
#        allowed_types = ('miembro', ) 
#        elementos = folder[concejo_comunal].getImmediatelyAddableTypes(allowed_types)
#        self.assertTrue('miembro' in elementos)
