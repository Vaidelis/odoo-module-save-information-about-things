from odoo import models, fields, api


class InformationReportWizard(models.TransientModel):
    _name = "save_information.report.wizard"
    _description = "Print information wizard"

    date_from = fields.Date(string="Date From")
    date_to = fields.Date(string="Date To")

    def action_print_report(self):
        data = {
            'date_from': self.date_from,
            'date_to': self.date_to,
        }
        return self.env.ref('save_information.report_save_information').report_action(self, data=data)


class InformationReport(models.AbstractModel):
    _name = 'report.save_information.information_report_template'
    _description = 'Save Information Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        return data
