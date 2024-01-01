<h1>odoo technical interview</h1>

<h2>Goal</h2>

<p>Create a new Odoo version 14 module to allow a basic managing telecom service consumptions.</p>

<h2>USER STORIES</h2>

<p>The module must cover the following user stories:</p>
<p>• As a user, I want to create, read, update and delete consumptions from a user interface.</p>
<p>• As a user, I want an interface that displays telecom service consumptions filtering the last month, to facilitate
monitoring.</p>
<p>• As a user, I want a graphical view that categorizes telecom service consumptions by quarters and by
product categories using category codes ('LL', 'MO'), for a visual representation of data trends.
Technical guide</p>
<p>• The new module will depend on the following Odoo core modules: base and product.</p>
<p>• Please, create a new Gitlab or Github repository.</p>
<p>• A list of resources is provided along with this document.</p>

<h2>Data model proposal</h2>

<p>Products The products that are available to consume.</p>
code [string] </br>
name [string] </br>
category [reference] </br>

<p>Product categories Products are grouped by categories.</p>
code [string] </br>
name [string] </br>

<p>Consumptions Quantity of products consumed at a given point in time.</p>
timestamp [timestamp] </br>
product [reference] </br>
quantity [integer] </br>

<h2>Bonus points</h2>

<p>1. Use data files to import Products and Product categories resources</p>
<p>2. Install and use the base_rest module to add a REST API for Consumptions resource</p>
<p>3. Add unit tests</p>