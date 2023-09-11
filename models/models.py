# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class my_module_demo(models.Model):
#     _name = 'my_module_demo.my_module_demo'
#     _description = 'my_module_demo.my_module_demo'

#     name = fields.Char()
#     value = fields.Integer()
#     code = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.code = '%s (code)' record.code
