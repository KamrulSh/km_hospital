# -*- coding: utf-8 -*-

from odoo.exceptions import ValidationError
from odoo import api, fields, models, _


class AppointmentReportWizard(models.TransientModel):
    _name = "kmhospital.appointment.report.wizard"
    _description = "Print Appointment Wizard"

    date_from = fields.Datetime(string='Date from', required=False)
    date_to = fields.Datetime(string='Date to', required=False)
    patient_id = fields.Many2one('kmhospital.patient', string="Patient", required=True)

    def action_print_report(self):
        patient_id = self.patient_id
        domain = []
        if patient_id:
            domain += [('patient_id', '=', patient_id.id)]
        date_from = self.date_from
        if date_from:
            domain += [('checkup_date', '>=', date_from)]
        date_to = self.date_to
        if date_to:
            domain += [('checkup_date', '<=', date_to)]
        # print("\n\nTest................\n", domain)

        appointments = self.env['kmhospital.appointment'].search_read(domain)
        
        data = {
            'form_data': self.read()[0],
            'appointments': appointments
        }
        return self.env.ref('km_hospital.action_report_appointment_card').report_action(self, data=data)

    @api.constrains('date_from', 'date_to')
    def _check_date_validation(self):
        for record in self:
            if record.date_from > record.date_to:
                raise ValidationError("Date from must be previous than date to.")
