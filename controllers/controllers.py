# -*- coding: utf-8 -*-
# from odoo import http


# class Actavator(http.Controller):
#     @http.route('/actavator/actavator/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/actavator/actavator/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('actavator.listing', {
#             'root': '/actavator/actavator',
#             'objects': http.request.env['actavator.actavator'].search([]),
#         })

#     @http.route('/actavator/actavator/objects/<model("actavator.actavator"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('actavator.object', {
#             'object': obj
#         })
