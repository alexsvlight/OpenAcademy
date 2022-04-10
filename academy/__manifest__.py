# -*- coding: utf-8 -*-
{
    'name': "Academy",

    'summary': """
        
        Quest #3 """,

    'description': """
        Quest #3 in learning ODOO
    """,

    'author': "My_Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '15.0.1',

    # any module necessary for this one to work correctly
    'depends': ['mail','website_sale'],
    # 'depends': ['website_sale', 'product'],
    # 'depends': ['mail', 'website_sale'],

    # always loaded
    'data': [
        # 'security/groups.xml',
        'security/ir.model.access.csv',
        'views/templates.xml',
        'views/views.xml',
        'data/data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    # 'application': True,
    # 'auto_install': False,
    # 'license': 'LGPL-3',
}
