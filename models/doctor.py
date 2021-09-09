from odoo import models, fields, api
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
    age = fields.Char(string='Age')
    status = fields.Selection([
        ('fulltime','Full time'),
        ('parttime', 'Part time')
    ], required=True)
    description = fields.Text()
    joined_from = fields.Date(string='Joined Date')
    
    