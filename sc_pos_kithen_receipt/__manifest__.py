{
    'name': 'POS Kitchen Receipt | POS Custom Kitchen Receipt',
    "description": """Using this module you can print POS Kitchen Receipt From front end""",
    'summary': 'Using this module you can print POS Kitchen Receipt From front end',
    'category': 'Point of Sale',    
    'version': '14.3.2.1',
    'sequence': 1,
    "author" : "DOTSPRIME",
    "email": 'dotsprime@gmail.com',
    'price': 10,
    'currency': 'EUR',
    'license': 'OPL-1', 
    "depends" : ['base','point_of_sale','pos_restaurant'],
    "data": [
        'views/pos_receipt_template.xml',
        'views/pos_config_view.xml'
    ],
    'demo': [],
    'images': ['static/description/main_screenshot.jpg'],  
    "live_test_url" : "https://youtu.be/26pi7Y0NDsY",       
    'qweb': ['static/src/xml/templates.xml'],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
