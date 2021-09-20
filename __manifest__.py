# -*- coding: utf-8 -*-
{
    'name': "KM Hospital",
    'sequence': 1,
    'summary': """
        A hospital management module.""",

    'description': """
        A hospital management module for creating patient, doctor, 
        department, medical test, and appointments.
    """,

    'author': "Kamrul & Niazi",
    'website': "http://www.yourcompany.com",
    'category': 'Services',
    'version': '0.1',
    'license': 'LGPL-3',
    # any module necessary for this one to work correctly
    'depends': ['base','hr','website'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',    
        'wizard/appointment_report_view.xml',
        'views/patient_view.xml',
        'views/doctor_view.xml',
        'views/department_view.xml',
        'views/appointment_view.xml',
        'views/medicaltest_view.xml',
        'views/website_patient_form.xml',
        'views/website_patient_view.xml',
        'reports/report.xml',
        'reports/sale_report_inherit.xml',
        'reports/appointment_report.xml',
    ],
    'installable' : True,
    'application' : True,
    'auto_install' : False,
}
