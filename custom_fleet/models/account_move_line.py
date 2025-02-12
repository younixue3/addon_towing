from odoo import models, fields

class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    vehicle_id = fields.Many2one('fleet.vehicle', string='Vehicle', readonly=True)
    employee_id = fields.Many2one('hr.employee', string='Employee', readonly=True)
    towing_type = fields.Selection([
    ('flatbed', 'Flatbed'),
    ('hook', 'Hook'),
    ('wheel_lift', 'Wheel Lift'),
    ], string="Towing Type", readonly=True)

    pickup_location = fields.Char(string='Pickup Location', readonly=True)
    dropoff_location = fields.Char(string='Dropoff Location', readonly=True)
