# -*- coding: utf-8 -*-
from openerp import http

# class HowKnowUs(http.Controller):
#     @http.route('/how_know_us/how_know_us/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/how_know_us/how_know_us/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('how_know_us.listing', {
#             'root': '/how_know_us/how_know_us',
#             'objects': http.request.env['how_know_us.how_know_us'].search([]),
#         })

#     @http.route('/how_know_us/how_know_us/objects/<model("how_know_us.how_know_us"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('how_know_us.object', {
#             'object': obj
#         })