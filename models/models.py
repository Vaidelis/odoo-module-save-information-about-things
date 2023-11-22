# -*- coding: utf-8 -*-
from odoo import models, fields

class saleOrder(models.Model):
    _inherit = 'sale.order'

    spokentoclient = fields.Boolean('Spoken to client', required=True)
