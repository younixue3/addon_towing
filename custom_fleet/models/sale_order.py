from odoo import models, fields

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    vehicle_id = fields.Many2one('fleet.vehicle', string='Vehicle')
    driver_name = fields.Char(related='vehicle_id.driver_id.name', string='Driver', readonly=True)
    towing_type = fields.Selection(related='vehicle_id.towing_type', string='Towing Type', readonly=True)
    pickup_location = fields.Char(string='Pickup Location')
    dropoff_location = fields.Char(string='Dropoff Location')
