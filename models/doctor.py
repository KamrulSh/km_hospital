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
    ])
    phone = fields.Char(string='Phone', required=True)
    
    email = fields.Char(string='Email')

    @api.constrains('email')
    def _check_email(self):
        for record in self:
            valid_email = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', record.email)
            
            if valid_email == None:
                raise ValidationError('Please provide a valid E-mail')
    
    age = fields.Char(string='Age')
    status = fields.Selection([
        ('fulltime','Full time'),
        ('parttime', 'Part time')
    ], required=True)
    description = fields.Text()
    joined_from = fields.Date(string='Joined Date')

    view_patients_ids = fields.One2many('kmhospital.patient','view_doctors_ids', string="Patients List")