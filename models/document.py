from odoo import models, fields


class Document(models.Model):
    _name = 'new_document_module.document'

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')
    company = fields.Char(string='Company')
    creator = fields.Char(string='Creator')

    # Define the many-to-many relation with employees
    employee_ids = fields.Many2many('new_document_module.employee',
                                    'document_employee_rel',
                                    'document_id', 'employee_id',
                                    string='Employees')
