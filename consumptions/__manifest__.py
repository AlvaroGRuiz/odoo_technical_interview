# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Consumptions',
    'version' : '1.0',
    'description': """
Consumptions
====================

Model consumption:
timestamp [timestamp]
product [reference]
quantity [integer]

- Create, read, update and delete consumptions from a user interface.
- Interface that displays telecom service consumptions filtering the last month, to facilitate monitoring
- Graphical view that categorizes telecom service consumptions by quarters and by product categories using category 
codes, for a visual representation of data trends.
- REST API for Consumptions resource.
- Data files to import Products, Product categories and Consumptions resources
- Unit tests

    """,
    'category': 'Sales/Sales',
    'depends' : ['base', 'product', 'base_rest'],
    'external_dependencies': {
        "python":[
            'cachetools',
            'cerberus',
            'pyquerystring',
            'parse-accept-language',
            'apispec'
        ]
    },
    'data': [
        'security/account_security.xml',
        'security/ir.model.access.csv',
        'views/consumptions_views.xml',
        'views/product_views.xml',
        "data/product_data.xml"
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
