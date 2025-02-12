from odoo import models, fields

class AccountMove(models.Model):
    _inherit = 'account.move'
    
    hide_tax = fields.Boolean(string='Print Without Tax')