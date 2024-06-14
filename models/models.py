# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class new_document_module(models.Model):
#     _name = 'new_document_module.new_document_module'
#     _description = 'new_document_module.new_document_module'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

