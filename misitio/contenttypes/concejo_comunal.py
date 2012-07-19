# -*- coding: utf-8 -*-

#estructura de los datos como se van almacenar al ZODB
from Acquisition import aq_inner
from five import grok
from zope import schema
from plone.directives import form
from Products.CMFCore.utils import getToolByName
from misitio.contenttypes.miembro import IMiembro

class IConcejoComunal(form.Schema):
    """Tipo de Contenido Consejo Comunal
    """
    
    ubicacion = schema.Text(
        description = u'DESCRIPCIÓN DE LA UBICACIÓN',
        title = u'ubicacion',
        required = True, 
    )

    persona_de_contacto = schema.TextLine(
        description = u'DESCRIPCION DE LA PERSONA DE CONTACTO',
        title = u'persona de contacto',
        required = True, 
    )

    correo = schema.TextLine(
        description = u'DESCRIPCIÓN DE CORREO ELECTRÓNICO',
        title = u'correo',
        required = True, 
    )

    telefono = schema.TextLine(
        description = u'DESCRIPCIÓN DE TELÉFONO',
        title = u'telefono',
        required = False,
    )

grok.templatedir('concejo_comunal_templates')

class View(grok.View):
    """Clase vista para el esquema consejo_comunal   
    """
    
    grok.context(IConcejoComunal)
    grok.require('zope2.View')
    grok.template("view")

    def miembros_concejo_comunal(self):
        """Retorna un resultado de busqueda en el catalogo de los tipos miembros de un concejo comunal
        """

        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')

        return catalog(object_provides=IMiembro.__identifier__,
                       path='/'.join(context.getPhysicalPath()),
                       sort_on='sortable_title')

