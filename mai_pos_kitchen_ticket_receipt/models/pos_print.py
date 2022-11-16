
from odoo import fields, models,tools,api
import logging

class pos_config(models.Model):
    _inherit = 'pos.config' 

    allow_kitchen_ticket_print = fields.Boolean('Allow kitchen ticket print',default=True)