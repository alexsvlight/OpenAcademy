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
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/course_views.xml',
        'views/session_views.xml',
        'views/res_partner_views.xml',
        'views/menu.xml',
        'views/session_dashboard.xml',
        'wizard/wizard_session_view.xml',
        'reports/report_sessions.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo_openacademy.xml',
    ],
}