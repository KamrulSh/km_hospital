from odoo.exceptions import ValidationError
from odoo import models, fields, api

class HospitalAppointment(models.Model):
    _name = 'kmhospital.appointment'
    _description = 'Appointments'

    name = fields.Many2one("kmhospital.patient", string='Patient Name', required=True)
    gender = fields.Selection([
        ('male','Male'),
        ('female', 'Female')
    ], related='name.gender')
    phone = fields.Char(string='Phone', related='name.phone')
    email = fields.Char(string='Email', related='name.email')
    age = fields.Integer(string='Age', related='name.age')
    description = fields.Text()
    status = fields.Selection([
        ('draft','Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done')
    ], default='draft', required=True)
    appointment_date = fields.Datetime(string='Appointment Date', default=fields.datetime.now())
    checkup_date = fields.Datetime(string='Checkup Date', required=True)
    prescription_medicine_ids = fields.One2many("kmhospital.appointment.prescription.medicine", 
            "appointment_medicine_id", string="Prescription Medicine")
    prescription_medtest_ids = fields.One2many("kmhospital.appointment.prescription.tests", 
            "appointment_medtest_id", string="Prescription Tests")
    appointed_doctor_id = fields.Many2one("kmhospital.doctor", string="Doctor name", required=True)
    # appointed_patient_id = fields.Many2one("kmhospital.patient", string="Patient name")

    @api.constrains('appointment_date', 'checkup_date')
    def _check_date_validation(self):
        for record in self:
            if record.checkup_date < record.appointment_date:
                raise ValidationError('Checkup date should not be previous date.')

# for medicine record in patient appointment
class AppointmentPrescriptionMedicine(models.Model):
    _name = "kmhospital.appointment.prescription.medicine"
    _description = "Appointment Prescription Medicine"

    name = fields.Char(string="Medicine", required=True)
    quantity = fields.Integer(string="Quantity")
    appointment_medicine_id = fields.Many2one("kmhospital.appointment", string="Appointment medicine")

# for medical test record in patient appointment
class AppointmentPrescriptionTest(models.Model):
    _name = "kmhospital.appointment.prescription.tests"
    _description = "Appointment Prescription Tests"

    name = fields.Char(string="Medical Tests", required=True)
    appointment_medtest_id = fields.Many2one("kmhospital.appointment", string="Appointment medical test")
