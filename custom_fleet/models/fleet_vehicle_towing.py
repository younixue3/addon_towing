from odoo import models, fields, api
from odoo.exceptions import ValidationError

class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'  # Menginherit model fleet.vehicle

    towing_capacity = fields.Float(string='Towing Capacity (kg)')
    towing_type = fields.Selection([
        ('flatbed', 'Flatbed'),
        ('hook', 'Hook'),
        ('wheel_lift', 'Wheel Lift'),
    ], string='Towing Type')
    additional_equipment = fields.Text(string='Additional Equipment Details')
    
    driver_employee_id = fields.Many2one(
        'hr.employee', 
        string='Driver (Employee)', 
        domain="[('department_id.name', '=', 'Field Staff')]"
    )
    
    job_id = fields.Many2one(
        'hr.job', 
        string="Job Position", 
        related='driver_employee_id.job_id', 
        store=True, 
        readonly=True
    )
    
    license_number = fields.Char(string="License Number (SIM)", help="Nomor SIM karyawan driver", readonly=True)
    
    @api.onchange('driver_employee_id')
    def _onchange_driver_employee_id(self):
        if self.driver_employee_id:
            # Mengambil license_number dari driver_employee_id dan mengisi field license_number
            self.license_number = self.driver_employee_id.license_number
        else:
            self.license_number = False

    def write(self, vals):
        # Menyimpan nilai license_number berdasarkan driver_employee_id
        if 'driver_employee_id' in vals:
            employee = self.env['hr.employee'].browse(vals['driver_employee_id'])
            if employee.department_id.name != 'Field Staff':
                raise ValidationError('Only employees from the Field Staff department can be assigned as drivers.')

            # Validasi posisi pekerjaan
            if employee.job_id.name != 'Driver':
                raise ValidationError('The employee must have the "Driver" job position.')

            # Set license_number berdasarkan driver_employee_id
            vals['license_number'] = employee.license_number  # Ambil nomor SIM dari karyawan

        return super(FleetVehicle, self).write(vals)
