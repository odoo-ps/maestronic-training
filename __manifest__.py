# -*- coding: utf-8 -*-
{
    'name': "Car",

    'summary': """
        Car Model""",

    'description': """
        Representation of Car
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '14.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'helpdesk'
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
}
