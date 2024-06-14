# -*- coding: utf-8 -*-
# from odoo import http


# class NewDocumentModule(http.Controller):
#     @http.route('/new_document_module/new_document_module', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/new_document_module/new_document_module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('new_document_module.listing', {
#             'root': '/new_document_module/new_document_module',
#             'objects': http.request.env['new_document_module.new_document_module'].search([]),
#         })

#     @http.route('/new_document_module/new_document_module/objects/<model("new_document_module.new_document_module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('new_document_module.object', {
#             'object': obj
#         })

