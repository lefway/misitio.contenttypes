# -*- coding: utf-8 -*-

from zope import schema #estructura de los datos como se van almacenar al ZODB
from plone.directives import form

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
