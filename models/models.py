# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Information(models.Model):
    _name = 'save_information.save_information'
    _description = 'Save stuff information'

    name = fields.Char(string="Name", required=True, help="Save information")
    description = fields.Text(string='Description')
    company_id = fields.Many2one('res.company', string='Company', required=True)