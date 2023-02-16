# -*- coding: utf-8 -*-
# from odoo import http


# class MubeenTestEcube(http.Controller):
#     @http.route('/mubeen_test_ecube/mubeen_test_ecube', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mubeen_test_ecube/mubeen_test_ecube/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('mubeen_test_ecube.listing', {
#             'root': '/mubeen_test_ecube/mubeen_test_ecube',
#             'objects': http.request.env['mubeen_test_ecube.mubeen_test_ecube'].search([]),
#         })

#     @http.route('/mubeen_test_ecube/mubeen_test_ecube/objects/<model("mubeen_test_ecube.mubeen_test_ecube"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mubeen.test_ecube.object', {
#             'object': obj
#         })
