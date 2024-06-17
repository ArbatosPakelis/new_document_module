from odoo import models, fields


class Employee(models.Model):
    _name = 'new_document_module.employee'

    name = fields.Char(string='Name')

    # Define the many-to-many relation with documents
    document_ids = fields.Many2many('new_document_module.document',
                                    'document_employee_rel',
                                    'employee_id', 'document_id',
                                    string='Documents')