# -*- coding: utf-8 -*-
from odoo.addons.component.core import Component
from odoo.addons.base_rest import restapi

class ProductConsumptionService(Component):
    _inherit = 'base.rest.service'
    _name = 'product.consumption.service'
    _usage = 'product_consumption'
    _collection = 'consumptions.services'
    _description = "API service consimptions"

    # Service method searching for all consumptions
    @restapi.method(
        [(["/","/search"], "GET")],
        output_param=restapi.CerberusValidator("_validator_search_consumption"),
        auth="public"
    )
    def search(self):
        consumptions_records = self._search()
        response = []
        for consumption_record in consumptions_records:
            response.append({
                'id': consumption_record.id,
                'name': consumption_record.name,
                'timestamp': consumption_record.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                'product_id': consumption_record.product_id.id,
                'quantity': consumption_record.quantity,
                'category_code': consumption_record.category_code,
                'quarter': consumption_record.quarter,
            })
        return {'list': response}

    # Private search method for all consumption
    def _search(self):
        return self.env['product.consumption'].search([])

    # Service method bringing specific consumption per ID
    @restapi.method(
        [(["/<int:id>"], "GET")],
        output_param=restapi.CerberusValidator("_validator_get_consumption"),
        auth="public"
    )
    def get(self, consumption_id):
        consumption_record = self._get(consumption_id)
        return {
            'id': consumption_record.id,
            'name': consumption_record.name,
            'timestamp': consumption_record.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            'product_id': consumption_record.product_id.id,
            'quantity': consumption_record.quantity,
            'category_code': consumption_record.category_code,
            'quarter': consumption_record.quarter,
        }

    # Private method bringing specific consumption per ID
    def _get(self, consumption_id):
        return self.env['product.consumption'].browse(consumption_id)

    # Service method creating a consumption
    @restapi.method(
        [(["/"], "POST")],
        input_param=restapi.CerberusValidator("_validator_input_create_consumption"),
        output_param=restapi.CerberusValidator("_validator_create_consumption"),
        auth="public"
    )
    def create(self, **params):
        # Create a new product consumption record
        new_consumption = self._create({
            'timestamp': params.get('timestamp'),
            'product_id': params.get('product_id'),
            'quantity': params.get('quantity'),
        })

        return {
            'id': new_consumption.id,
            'name': new_consumption.name,
            'timestamp': new_consumption.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            'product_id': new_consumption.product_id.id,
            'quantity': new_consumption.quantity,
            'category_code': new_consumption.category_code,
            'quarter': new_consumption.quarter,
        }

    # Private method creating a consumption
    def _create(self, create_data):
        return self.env['product.consumption'].create(create_data)

    # Service method updating a consumption
    @restapi.method(
        [(["/<int:id>"], "PUT")],
        input_param=restapi.CerberusValidator("_validator_input_update_consumption"),
        output_param=restapi.CerberusValidator("_validator_update_consumption"),
        auth="public"
    )
    def update(self, consumption_id, **params):
        # Update an existing product consumption record
        update_data = {}
        if "timestamp" in params:
            update_data["timestamp"] = params.get('timestamp')
        if "product_id" in params:
            update_data["product_id"] = params.get('product_id')
        if "quantity" in params:
            update_data["quantity"] = params.get('quantity')

        consumption_record = self._update(consumption_id, update_data)

        return {
            'id': consumption_record.id,
            'name': consumption_record.name,
            'timestamp': consumption_record.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            'product_id': consumption_record.product_id.id,
            'quantity': consumption_record.quantity,
            'category_code': consumption_record.category_code,
            'quarter': consumption_record.quarter,
        }

    # Private method updating a consumption
    def _update(self, consumption_id, update_data):
        consumption_record = self.env['product.consumption'].browse(consumption_id)
        consumption_record.write(update_data)
        return consumption_record

    # Service method deleting a consumption
    @restapi.method(
        [(["/<int:id>"], "DELETE")],
        output_param=restapi.CerberusValidator("_validator_delete_consumption"),
        auth="public"
    )
    def delete(self, consumption_id):
        # Delete an existing product consumption record
        self._delete(consumption_id)
        return {'id': consumption_id}

    # Private method deleting a consumption
    def _delete(self, consumption_id):
        self.env['product.consumption'].browse(consumption_id).unlink()

    # Validators - Methods to validate the input and output data of the services taking into account that they are JSON
    def _get_partner_schema(self):
        return {
            "name": {"type": "string", "required": True, "nullable": False, "empty": False}
        }

    def _validator_search_consumption(self):
        return {
            "list": {
                "type": "list",
                "required": True,
                "schema": {"type": "dict", "schema": self._validator_get_consumption()},
            }
        }

    def _validator_get_consumption(self):
        return {
            'id': {'type': 'integer', "required": True, "nullable": False, "empty": False},
            'name': {'type': 'string', "required": True, "nullable": False, "empty": False},
            'timestamp': {'type': 'string', "required": True, "nullable": False, "empty": False},
            'product_id': {'type': 'integer', "required": True, "nullable": False, "empty": False},
            'quantity': {'type': 'integer', "required": True, "nullable": False, "empty": False},
            'category_code': {'type': 'string', "required": True, "nullable": False, "empty": False},
            'quarter': {'type': 'string', "required": True, "nullable": False, "empty": False}
        }

    def _validator_create_consumption(self):
        return {
            'id': {'type': 'integer', "required": True, "nullable": False, "empty": False},
            'name': {'type': 'string', "required": True, "nullable": False, "empty": False},
            'timestamp': {'type': 'string', "required": True, "nullable": False, "empty": False},
            'product_id': {'type': 'integer', "required": True, "nullable": False, "empty": False},
            'quantity': {'type': 'integer', "required": True, "nullable": False, "empty": False},
            'category_code': {'type': 'string', "required": True, "nullable": False, "empty": False},
            'quarter': {'type': 'string', "required": True, "nullable": False, "empty": False}
        }

    def _validator_input_create_consumption(self):
        return {
            'timestamp': {'type': 'string', "required": True, "nullable": False, "empty": False},
            'product_id': {'type': 'integer', "required": True, "nullable": False, "empty": False},
            'quantity': {'type': 'integer', "required": True, "nullable": False, "empty": False},
        }

    def _validator_update_consumption(self):
        return {
            'id': {'type': 'integer', "required": True, "nullable": False, "empty": False},
            'name': {'type': 'string', "required": True, "nullable": False, "empty": False},
            'timestamp': {'type': 'string', "required": True, "nullable": False, "empty": False},
            'product_id': {'type': 'integer', "required": True, "nullable": False, "empty": False},
            'quantity': {'type': 'integer', "required": True, "nullable": False, "empty": False},
            'category_code': {'type': 'string', "required": True, "nullable": False, "empty": False},
            'quarter': {'type': 'string', "required": True, "nullable": False, "empty": False}
        }

    def _validator_input_update_consumption(self):
        return {
            'timestamp': {'type': 'string', "required": False, "nullable": True, "empty": True},
            'product_id': {'type': 'integer', "required": False, "nullable": True, "empty": True},
            'quantity': {'type': 'integer', "required": False, "nullable": True, "empty": True},
        }

    def _validator_delete_consumption(self):
        return {'id': {'type': 'integer', "required": True, "nullable": False, "empty": False}}
