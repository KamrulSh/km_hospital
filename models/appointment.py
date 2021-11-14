from odoo.exceptions import ValidationError
from odoo import models, fields, api, _


class HospitalAppointment(models.Model):
    _name = 'kmhospital.appointment'
    _description = 'Appointments'
    _order = "id desc"
    _inherit = ['mail.thread', 'mail.activity.mixin']

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
    note = fields.Text()
    status = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('done', 'Done'),
        ('cancel', 'Canceled')
    ], default='draft', required=True, tracking=True)
    appointment_date = fields.Datetime(string='Appointment Date', default=fields.datetime.now(), tracking=True)
    checkup_date = fields.Datetime(string='Checkup Date', required=True, tracking=True)
    prescription_medicine_ids = fields.One2many("kmhospital.appointment.prescription.medicine",
                                                "appointment_medicine_id", string="Prescription Medicine")
    appointed_doctor_id = fields.Many2one("kmhospital.doctor", string="Doctor name", required=True)
    prescription_medical_test_ids = fields.Many2many("kmhospital.medicaltest", "medical_test_ids",
                                                     string="Medical tests")

    @api.constrains('appointment_date', 'checkup_date')
    def _check_date_validation(self):
        for record in self:
            if record.checkup_date < record.appointment_date:
                raise ValidationError('Checkup date should not be previous date.')

    # changing the status
    def action_status_draft(self):
        self.status = 'draft'

    def action_status_confirm(self):
        self.status = 'confirm'

    def action_status_done(self):
        self.status = 'done'

    def action_status_cancel(self):
        self.status = 'cancel'

    @api.model
    def create(self, vals):
        if not vals['description']:
            vals['description'] = "Enter the description here"
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('kmhospital.appointment') or _('New')

        res = super(HospitalAppointment, self).create(vals)
        return res

    @api.onchange('patient_id')
    def _change_appointment_note(self):
        if self.patient_id:
            if not self.note:
                self.note = "New appointment"
        else:
            self.note = ""


# for medicine record in patient appointment
class AppointmentPrescriptionMedicine(models.Model):
    _name = "kmhospital.appointment.prescription.medicine"
    _description = "Appointment Prescription Medicine"

    name = fields.Char(string="Medicine", required=True)
    quantity = fields.Integer(string="Quantity")
    appointment_medicine_id = fields.Many2one("kmhospital.appointment", string="Appointment medicine")
