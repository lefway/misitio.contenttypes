# -*- coding: utf-8 -*-

#estructura de los datos como se van almacenar al ZODB
from zope import schema
from plone.directives import form

class IConsejoComunal(form.Schema):
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
