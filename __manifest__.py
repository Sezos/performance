# -*- coding: utf-8 -*-
{
    'name': "performance",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/screen1.xml',
        'views/screen2.xml',
        'views/screen3.xml'
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
