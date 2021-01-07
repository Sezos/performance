# -*- coding: utf-8 -*-
# from odoo import http


# class Performance(http.Controller):
#     @http.route('/performance/performance/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/performance/performance/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('performance.listing', {
#             'root': '/performance/performance',
#             'objects': http.request.env['performance.performance'].search([]),
#         })

#     @http.route('/performance/performance/objects/<model("performance.performance"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('performance.object', {
#             'object': obj
#         })
