from odoo import models, fields, api

class DocumentFilterWizard(models.TransientModel):
    _name = 'document.filter.wizard'
    _description = 'Document Filter Wizard'

    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    employee_id = fields.Many2one('new_document_module.employee', string='Employee')

    def filter_documents(self):
        domain = []
        if self.start_date:
            domain.append(('create_date', '>=', self.start_date))
        if self.end_date:
            domain.append(('create_date', '<=', self.end_date))
        if self.employee_id:
            domain.append(('employee_ids', 'in', self.employee_id.id))
        return {
            'type': 'ir.actions.act_window',
            'name': 'Filtered Documents',
            'view_mode': 'tree,form',
            'res_model': 'new_document_module.document',
            'domain': domain,
        }
