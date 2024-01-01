# -*- coding: utf-8 -*-

from odoo import fields, models

class ProductCategory(models.Model):
    _inherit = "product.category"

    # model fields
    code = fields.Char('Code', index=True)

class Product(models.Model):
    _inherit = 'product.product'

    # model fields
    consumptions_ids = fields.One2many('product.consumption', 'product_id', string='Consumptions')