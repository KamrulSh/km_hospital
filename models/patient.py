from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re

class HospitalPatient(models.Model):
    _name = 'kmhospital.patient'
    _description = 'Hospital Patient'

    name = fields.Char(string='Patient Name', required=True)
    address = fields.Char(string='Address')
    gender = fields.Selection([
        ('male','Male'),
        ('female', 'Female')
    ], default="male")
    phone = fields.Char(string='Phone', required=True)
    age = fields.Char(string='Age')
    email = fields.Char(string='Email')

    @api.constrains('email')
    def _check_email(self):
        for record in self:
            valid_email = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', record.email)
            
            if valid_email == None:
                raise ValidationError('Please provide a valid E-mail')
    status = fields.Selection([
        ('new','New'),
        ('old', 'Old')
    ], required=True, default='new')
    description = fields.Text()
    problems = fields.Text()
    
    patient_appointment_ids = fields.One2many('kmhospital.appointment','name', string="Appointment List")