from odoo import models, fields

class POSConfig(models.Model):
	_inherit = 'pos.config'

	print_kitchen_receipt = fields.Boolean(string="Allow to print Kitchen receipt")