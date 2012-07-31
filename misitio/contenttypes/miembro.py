# -*- coding: utf-8 -*-
from Acquisition import aq_inner
from five import grok
from zope import schema #estructura de los datos como se van almacenar al ZODB
from plone.directives import form
from Products.CMFCore.utils import getToolByName

class IMiembro(form.Schema):
    """Tipo de Contenido Miembro
    """
    
    nombres = schema.TextLine(
        description = u'DESCRIPCIÓN DEL NOMBRE',
        title = u'nombres',
        required = True, 
    )

    apellido = schema.TextLine(
        description = u'DESCRIPCIÓN DEL APELLIDO',
        title = u'apellido',
        required = True, 
    )

    ci = schema.TextLine(
        description = u'DESCRIPCIÓN DE LA CÉDULA DE IDENTIDAD',
        title = u'ci',
        required = True, 
    )

    direcci_n_f_sica = schema.TextLine(
        description = u'DESCRIPCIÓN DE  DE DIRECCIÓN ELECTRÓNICA',
        title = u'dirección electrónica',
        required = True,
    )

    twitter = schema.TextLine(
        description = u'DESCRIPCIÓN DEL TWITTER',
        title = u'twitter',
        required = False,
    )

grok.templatedir('miembro_templates')

class View(grok.View):
    """Clase vista para el esquema miembro   
    """
    
    grok.context(IMiembro)
    grok.require('zope2.View')
    grok.template("view")

