{
    'name': "Test Real State",
    'version': '1.0',
    'depends': ['base'],
    'author': "Darkside",
    'category': 'App',
    'description': """
    Description text
    """,
    # data files always loaded at installation
    'data': [
        'views/estate_property_views.xml',
        'views/estate_menus.xml'
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        'security/ir.model.access.csv',
        
    ],
    'application': True,
}
