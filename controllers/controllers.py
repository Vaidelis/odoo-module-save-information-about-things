# -*- coding: utf-8 -*-
# from odoo import http


# class SaveInformation(http.Controller):
#     @http.route('/save_information/save_information/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/save_information/save_information/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('save_information.listing', {
#             'root': '/save_information/save_information',
#             'objects': http.request.env['save_information.save_information'].search([]),
#         })

#     @http.route('/save_information/save_information/objects/<model("save_information.save_information"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('save_information.object', {
#             'object': obj
#         })
