from odoo import models, fields

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    assigned_vehicles_ids = fields.One2many(
        'fleet.vehicle', 
        'driver_employee_id', 
        string='Assigned Vehicles'
    )
    license_number = fields.Char(string="License Number (SIM)", help="Nomor SIM karyawan")
    license_expiry_date = fields.Date(string="License Expiry Date", help="Tanggal kadaluarsa SIM")
