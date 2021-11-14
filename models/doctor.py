from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re


class HospitalDoctor(models.Model):
    _name = 'kmhospital.doctor'
    _description = 'Hospital Doctor'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Doctor Name', required=True, tracking=True)
    college = fields.Char(string='College', tracking=True)
    address = fields.Char(string='Address', tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], default='male')
    phone = fields.Char(string='Phone', required=True, tracking=True)
    email = fields.Char(string='Email', required=True, tracking=True)
    department_id = fields.Many2one("hr.department", string='Department', required=True, tracking=True)
    view_appointment_ids = fields.One2many('kmhospital.appointment', 'appointed_doctor_id', string="Appointment Count",
                                           readonly=True)
    age = fields.Integer(string='Age', required=True, tracking=True)
    status = fields.Selection([
        ('fulltime', 'Full time'),
        ('parttime', 'Part time')
    ], required=True, default='fulltime', tracking=True)
    description = fields.Text()
    joined_from = fields.Date(string='Joined Date', tracking=True)
    image = fields.Binary(string='Image', attachment=True)
    total_appointments = fields.Integer(string='Total appointments', compute='_compute_appointments')

    def action_status_halftime(self):
        self.status = 'parttime'

    def action_status_fulltime(self):
        self.status = 'fulltime'

    @api.constrains('email')
    def _check_email(self):
        for record in self:
            valid_email = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$',
                                   record.email)

            if valid_email is None:
                raise ValidationError('Please provide a valid E-mail')

    @api.constrains('age')
    def _check_doctor_age(self):
        for record in self:
            if record.age <= 0:
                raise ValidationError('Age must be greater than 0')

    # same as view_appointment_ids but implemented using computed fields
    # compute appointments of individual doctor
    def _compute_appointments(self):
        for record in self:
            record.total_appointments = self.env['kmhospital.appointment'].search_count(
                [('appointed_doctor_id', '=', record.id)])
