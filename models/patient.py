from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re

class HospitalPatient(models.Model):
    _name = 'kmhospital.patient'
    _description = 'Hospital Patient'
    _order = 'id desc'

    name = fields.Char(string='Patient Name', required=True)
    address = fields.Char(string='Address')
    gender = fields.Selection([
        ('male','Male'),
        ('female', 'Female')
    ], default="male")
    phone = fields.Char(string='Phone', required=True)
    age = fields.Integer(string='Age', required=True)
    email = fields.Char(string='Email')
    patient_appointment_ids = fields.One2many('kmhospital.appointment','name', string="Appointment Count", readonly=True)

    # check if the patient is already exists based on the patient name and phone number
    @api.constrains('name', 'phone')
    def _check_patient_exists(self):
        for record in self:
            patient = self.env['kmhospital.patient'].search([('name', '=', record.name), ('phone', '=', record.phone), ('id' , '!=', record.id)])
            if patient:
                raise ValidationError(f'Patient {record.name} already exists')

    @api.constrains('email')
    def _check_email(self):
        for record in self:
            valid_email = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', record.email)
            if valid_email == None:
                raise ValidationError('Please provide a valid Email')

    @api.constrains('age')
    def _check_patient_age(self):
        for record in self:
            if record.age <= 0:
                raise ValidationError('Age must be greater than 0')

    def action_url(self):
        return {
            "type": "ir.actions.act_url",
            "url": "https://github.com/KamrulSh/km_hospital",
            "target": "new",
        }