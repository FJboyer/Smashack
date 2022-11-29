{
	"name": "POS print kitchen order receipt KOT in browser| Custom Kitchen Order Receipt | Customer and Cashier name on Kitchen Order Receipt",
	"summary": "Custom Kitchen Order Receipt | Customer and Cashier name on Kitchen Order Receipt",
	"version": "14.1.1.1",
	"description": """Custom Kitchen Order Receipt | Customer and Cashier name on Kitchen Order Receipt""",    
    "category": 'Point of Sale',    
    "author" : "MAISOLUTIONSLLC",
    "email": 'apps@maisolutionsllc.com',
    "website":'http://maisolutionsllc.com/',
    "license": 'OPL-1', 
    "price": 8,
    "currency": "USD",     
	"category": "Point of Sale",
	"depends": ["pos_restaurant"],
	"data": [
		'views/assets.xml',
	],
	"qweb": [
        'static/src/xml/pos.xml'
	],
    "live_test_url" : "", 	
	'installable': True,
	'application': True,
	'auto_install': False,
    "images": ['static/description/main_screenshot.png'],	
}
