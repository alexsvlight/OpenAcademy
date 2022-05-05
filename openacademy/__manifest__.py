{
    'name': "Open Academy",

    'summary': """
        Open Academy
        """,

    'description': """
    Open Academy
    """,
#    Учет курсов для самообразования
    'author': "Svetliy Alexander",
    'website': "odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Learning',
    'version': '15.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','board'],

    # always loaded
    'data': [
        'security/openacademy_groups.xml',
        'security/ir.model.access.csv',
        'views/openacademy_course_views.xml',
        'views/openacademy_session_views.xml',
        'views/openacademy_menu.xml',
        'views/res_partner_views.xml',
        'wizard/create_openacademy_session_view.xml',
        'reports/openacademy_session_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/openacademy_demo.xml',
    ],
}