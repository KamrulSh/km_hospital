from odoo import models, fields, api


class EquipmentSaleOrder(models.Model):
    _inherit = 'sale.order'
    _description = 'Equipment Sales Order'