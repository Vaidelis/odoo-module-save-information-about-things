from odoo import api, fields, models

class InformationReportWizard(models.TransientModel):
    _name = "save_information.report.wizard"
    _description = "Print information wizard"

    date_from = fields.Date(string="Date From")
    date_to = fields.Date(string="Date To")