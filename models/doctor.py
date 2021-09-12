from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re

class HospitalDoctor(models.Model):
    _name = 'kmhospital.doctor'
    _description = 'Hospital Doctor'

    name = fields.Char(string='Doctor Name', required=True)
    college = fields.Char(string='College')
    address = fields.Char(string='Address')
    gender = fields.Selection([
        ('male','Male'),
        ('female', 'Female')
    ], default='male')
    phone = fields.Char(string='Phone', required=True)
    email = fields.Char(string='Email', required=True)
    department_id = fields.Many2one("hr.department", string='Department', required=True)
    view_appointment_ids = fields.One2many('kmhospital.appointment', 'appointed_doctor_id', string="Appointment List", readonly=True)
    age = fields.Integer(string='Age', required=True)
    status = fields.Selection([
        ('fulltime','Full time'),
        ('parttime', 'Part time')
    ], required=True, default='fulltime')
    description = fields.Text()
    joined_from = fields.Date(string='Joined Date')
    image = fields.Binary(string='Image', attachment=True)
    
    @api.constrains('email')
    def _check_email(self):
        for record in self:
            valid_email = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', record.email)
            
            if valid_email == None:
                raise ValidationError('Please provide a valid E-mail')
    
    @api.constrains('age')
    def _check_doctor_age(self):
        for record in self:
            if record.age <= 0:
                raise ValidationError('Age must be greater than 0')