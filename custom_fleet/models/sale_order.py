from odoo import models, fields

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    vehicle_id = fields.Many2one('fleet.vehicle', string='Vehicle')
    employee_id = fields.Many2one('hr.employee', string='Employee')  
    towing_type = fields.Selection(related='vehicle_id.towing_type', string='Towing Type', readonly=True)
    pickup_location = fields.Char(string='Pickup Location')
    dropoff_location = fields.Char(string='Dropoff Location')

    def _prepare_invoice_line(self, **optional_values):
        res = super()._prepare_invoice_line(**optional_values)
        res.update({
            'vehicle_id': self.vehicle_id.id,
            'employee_id': self.employee_id.id,
            'towing_type': self.towing_type,
            'pickup_location': self.pickup_location,
            'dropoff_location': self.dropoff_location,
        })
        return res
