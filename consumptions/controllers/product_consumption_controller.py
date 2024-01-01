# -*- coding: utf-8 -*-

from odoo.addons.base_rest.controllers import main


class ProductConsumptionController(main.RestController):
    _root_path = '/consumptions/api/'
    _collection_name = 'consumptions.services'
    _default_auth = "public"


