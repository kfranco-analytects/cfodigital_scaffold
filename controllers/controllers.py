# -*- coding: utf-8 -*-
# from odoo import http


# class MyModule(http.Controller):
#     @http.route('/my_module_demo/my_module_demo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_module_demo/my_module_demo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_module_demo.listing', {
#             'root': '/my_module_demo/my_module_demo',
#             'objects': http.request.env['my_module_demo.my_module_demo'].search([]),
#         })

#     @http.route('/my_module_demo/my_module_demo/objects/<model("my_module_demo.my_module_demo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_module_demo.object', {
#             'object': obj
#         })
