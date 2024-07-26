# -*- coding: utf-8 -*-
# from odoo import http


# class CheckModule(http.Controller):
#     @http.route('/check_module/check_module', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/check_module/check_module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('check_module.listing', {
#             'root': '/check_module/check_module',
#             'objects': http.request.env['check_module.check_module'].search([]),
#         })

#     @http.route('/check_module/check_module/objects/<model("check_module.check_module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('check_module.object', {
#             'object': obj
#         })

