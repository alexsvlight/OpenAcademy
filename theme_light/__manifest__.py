{
    'name': 'Light theme',
    'description': 'Learning theme creation',
    'version': '15.0.1',
    'author': 'Svietlyi Oleksandr',
    'category': 'Theme/Creative',

    'depends': ['website'],
    'data': [
    'views/layout.xml',
    'views/pages.xml',
    'views/snippets.xml',
    'views/options.xml',
    ],

    'assets': {
        'web.assets_frontend': [
            'theme_light/static/scss/style.scss',
        ],
        'web._assets_primary_variables': [
            'theme_light/static/scss/primary_variables.scss',
        ],
        'web._assets_frontend_helpers': [
            'theme_light/static/scss/bootstrap_overriden.scss',
        ],
        'website.assets_editor': [
            'theme_light/static/src/js/tutorial_editor.js',
        ]
    }
}