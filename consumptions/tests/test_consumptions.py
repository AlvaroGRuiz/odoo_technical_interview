# -*- coding: utf-8 -*-

from odoo.tests.common import TransactionCase, tagged
from datetime import datetime

@tagged('post_install', '-at_install', 'consumptions')
class TestProductConsumption(TransactionCase):

    def setUp(cls):
        super(TestProductConsumption, cls).setUp()
        # Create some test data
        cls.category = cls.env['product.category'].create({'name': 'Test Category', 'code': 'TC'})
        cls.product = cls.env['product.product'].create({'name': 'Test Product', 'type': 'service',
                                                         'categ_id' : cls.category.id})
        cls.consumption = cls.env['product.consumption'].create({
            'timestamp': datetime.now(),
            'product_id': cls.product.id,
            'quantity': 10
        })

    def test_compute_name(cls):
        # Verify that the name field has been constructed correctly
        cls.assertEqual(cls.consumption.name,
                        f"{cls.consumption.convert_to_timestamp(cls.consumption.timestamp)} - {cls.product.name} - 10",
                        "Fail")

    def test_compute_category_code(cls):
        # Verify the code of the category
        cls.assertEqual(cls.consumption.category_code, "TC", "Fail")

    def test_compute_quarter(cls):
        # Verify that the quarter has been calculated correctly
        current_month = datetime.now().month
        expected_quarter = f"Q{(current_month - 1) // 3 + 1}"
        cls.assertEqual(cls.consumption.quarter, expected_quarter, "Fail")

    def test_convert_to_timestamp(cls):
        # Verify datetime to timestamp conversion
        current_time = datetime.now()
        timestamp = cls.consumption.convert_to_timestamp(current_time)
        cls.assertEqual(current_time, cls.consumption.convert_to_datetime(timestamp), "Fail")

    def test_convert_to_datetime(cls):
        # Verify timestamp to datetime conversion
        timestamp = datetime.timestamp(datetime.now())
        converted_datetime = cls.consumption.convert_to_datetime(timestamp)
        cls.assertEqual(timestamp, cls.consumption.convert_to_timestamp(converted_datetime), "Fail")
