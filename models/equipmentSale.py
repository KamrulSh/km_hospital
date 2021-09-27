from odoo import models, fields


class CourseSale(models.Model):
    _inherit = 'product.template'
    _description = 'Hospital equipment Add'

    name = fields.Char(string="Hospital equipment")
    price = fields.Float(string="Price")
    image = fields.Binary(string='Photo', attachment=True)