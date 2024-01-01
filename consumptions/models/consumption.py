# -*- coding: utf-8 -*-

from odoo import fields, models, api
from datetime import datetime

class Consumption(models.Model):
    _name = 'product.consumption'
    _description = 'Comsuptions'
    _order = 'name asc'

    # model fields
    name = fields.Char(compute="_compute_name", index=True, readonly=True, store=True, string="Name")
    timestamp = fields.Datetime(required=True, string='Timestamp')
    product_id = fields.Many2one('product.product', string='Product', ondelete='cascade', required=True)
    quantity = fields.Integer(string='Quantity', required=True)

    category_code = fields.Char(compute="_compute_category_code", index=True, readonly=True, store=True,
                                string="Category code")
    quarter = fields.Selection([
        ('Q1', 'Q1'),
        ('Q2', 'Q2'),
        ('Q3', 'Q3'),
        ('Q4', 'Q4'),
    ], string='Quarter', compute="_compute_quarter", index=True, store=True)

    # name field calculation
    @api.depends('timestamp', 'product_id', 'quantity')
    def _compute_name(self):
        self.name = ""
        for record in self:
            if record.timestamp and record.product_id and record.product_id.name and record.quantity:
                record.name = str(record.convert_to_timestamp(record.timestamp)) + " - " + record.product_id.name \
                              + " - " + str(record.quantity)

    # calculation of the product category code field
    @api.depends('product_id')
    def _compute_category_code(self):
        self.category_code = ""
        for record in self:
            record.category_code = record.product_id.categ_id.code

    # Quarterly calculation
    @api.depends('timestamp')
    def _compute_quarter(self):
        self.quarter = ""
        for record in self:
            quarter = (record.timestamp.month - 1) // 3 + 1
            record.quarter = "Q"+str(quarter)

    # datetime to timestamp conversion
    def convert_to_timestamp(self, datetimeutf):
        return datetime.timestamp(datetimeutf)

    # timestamp to datetime conversion
    def convert_to_datetime(self, timestamp):
        return datetime.utcfromtimestamp(timestamp)