from odoo.exceptions import ValidationError
from odoo import models, fields, api, _


class HospitalAppointmentWizard(models.TransientModel):
    _name = 'kmhospital.appointment.wizard'
    _description = 'Create Appointment'

    name = fields.Char(string='Appointment Reference', required=True, copy=False, readonly=True,
                       default=lambda self: _('New'))
    patient_id = fields.Many2one("kmhospital.patient", string='Patient Name', required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], related='patient_id.gender')
    phone = fields.Char(string='Phone', related='patient_id.phone')
    email = fields.Char(string='Email', related='patient_id.email')
    age = fields.Integer(string='Age', related='patient_id.age')
    description = fields.Text()
    appointment_date = fields.Datetime(string='Appointment Date', default=fields.datetime.now())
    checkup_date = fields.Datetime(string='Checkup Date', required=True)
    appointed_doctor_id = fields.Many2one("kmhospital.doctor", string="Doctor name", required=True)

    @api.constrains('appointment_date', 'checkup_date')
    def _check_date_validation(self):
        for record in self:
            if record.checkup_date < record.appointment_date:
                raise ValidationError('Checkup date should not be previous date.')
