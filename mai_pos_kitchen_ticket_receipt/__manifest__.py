{
    'name': 'Print Kitchen Receipt After Validate || POS Kitchen Receipt Print ',
    'version': '14.4.2.1',
    'sequence': 1,
    'category': 'Point of Sale',
    'summary': 'Using this module you can print pos kitchen receipt in POS',
    'description': """Using this module you can print pos kitchen receipt in POS
    """,
    'depends': ['point_of_sale','pos_restaurant'],
    "author" : "MAISOLUTIONSLLC",
    "email": 'apps@maisolutionsllc.com',
    "website":'http://maisolutionsllc.com/',
    'license': 'AGPL-3',
    'price': 15,
    'currency': 'EUR',
    'data': [
        'views/pos_print_views.xml',
    ],
    'qweb': ['static/src/xml/pos.xml',],
    'images': ['static/description/main_screenshot.png'],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}


