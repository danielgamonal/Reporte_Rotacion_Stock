from odoo import api, models, _
from odoo.exceptions import UserError


class ReportStockRotation(models.AbstractModel):
    _name = 'report.cit_stock_rotation_report.report_stock_rotation'

    @api.model
    def _get_report_values(self, docids, data=None):
        if not data.get('form'):
            raise UserError(_("Form content is missing, this report cannot be printed."))
        return {
            'stockMoves': data.get('get_stock_moves'),
            'data': data,
        }
