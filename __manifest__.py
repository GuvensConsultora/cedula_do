# -*- coding: utf-8 -*-
{
    'name': "Cedula Rep Dominica",

    'summary': """
        El objetivo es permitir acceder 11 caracteres y 9""",

    'description': """
        Heredo el modulo base_vat y genero la validación de 11 caracteres para la cedula y 9 para Nfc
    """,

    'author': "Güvens and Slyn",
    'website': "https://github.com/GuvensConsultora/cedula_do/edit/main/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','base_vat'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
