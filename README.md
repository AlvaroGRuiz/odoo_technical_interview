# odoo_technical_interview

# Goal

Create a new Odoo version 14 module to allow a basic managing telecom service consumptions.

# USER STORIES

The module must cover the following user stories:
• As a user, I want to create, read, update and delete consumptions from a user interface.
• As a user, I want an interface that displays telecom service consumptions filtering the last month, to facilitate
monitoring.
• As a user, I want a graphical view that categorizes telecom service consumptions by quarters and by
product categories using category codes ('LL', 'MO'), for a visual representation of data trends.
Technical guide
• The new module will depend on the following Odoo core modules: base and product.
• Please, create a new Gitlab or Github repository.
• A list of resources is provided along with this document.

# Data model proposal

Products The products that are available to consume.
code [string]
name [string]
category [reference]

Product categories Products are grouped by categories.
code [string]
name [string]

Consumptions Quantity of products consumed at a given point in time.
timestamp [timestamp]
product [reference]
quantity [integer]

# Bonus points

1. Use data files to import Products and Product categories resources
2. Install and use the base_rest module to add a REST API for Consumptions resource
3. Add unit tests


