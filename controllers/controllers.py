# -*- coding: utf-8 -*-
# from odoo import http


# class KmHospital(http.Controller):
#     @http.route('/km__hospital/km__hospital/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/km__hospital/km__hospital/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('km__hospital.listing', {
#             'root': '/km__hospital/km__hospital',
#             'objects': http.request.env['km__hospital.km__hospital'].search([]),
#         })

#     @http.route('/km__hospital/km__hospital/objects/<model("km__hospital.km__hospital"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('km__hospital.object', {
#             'object': obj
#         })
