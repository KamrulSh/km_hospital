from odoo import models, fields, api
class HospitalPatient(models.Model):
    _name = 'kmhospital.patient'
    _description = 'Hospital Patient'

    name = fields.Char(string='Patient Name', required=True)
    address = fields.Char(string='Address')
    gender = fields.Selection([
        ('male','Male'),
        ('female', 'Female')
    ])
    phone = fields.Char(string='Phone', required=True)
    age = fields.Char(string='Age')
    email = fields.Char(string='Email')
    status = fields.Selection([
        ('new','New'),
        ('old', 'Old')
    ], required=True, default='new')
    description = fields.Text()
    problems = fields.Text()
    