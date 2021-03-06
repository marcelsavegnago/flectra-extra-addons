.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

=================
Stock Cycle Count
=================

This module provides the capability to execute a cycle count strategy in a
warehouse through different rules defined by the user. Cycle count is an
alternative to full wall-to-wall physical inventories in which little
portions (stock locations) of the stock are selected to count on a regular
basis.

The system propose locations in which to perform a inventory adjustment every
day based on a set of rules defined for the warehouse. In addition the system
can propose Zero-Confirmations which are simple and opportunistic counts to
check whether a locations has actually became empty or not.

With this strategy it is possible to:

* Remove the need to perform full physical inventories and to stop the
  production in the warehouse.
* Measure the accuracy of the inventory records and improve it.
* Correct inventory errors earlier and prevent them to become bigger.

Installation
============

To install this module, you need to:

* Download this module to your addons path.
* Install the module in your database.

Recommendations
---------------

It is highly recommended to use this module in conjunction with:

* `stock_inventory_verification_request`: Adds the capability to request Slot
  Verifications.
* `stock_inventory_lockdown`: Lock down locations during inventories.

Configuration
=============

You can configure the rules to compute the cycle count, acting as follow:

#. Go to *Inventory > Configuration > Cycle Count Rules*.
#. Create as much cycle count rules as you want.
#. Assign the rules to the Warehouse or zones where you want to apply the rules
   in.
#. Go to *Inventory > Configuration > Warehouse Management > Warehouses* and
   set a *Cycle Count Planning Horizon* for each warehouse.

Usage
=====

Once you have some rules configured for your warehouses, you can proceed as
is described below.

#. Go to "Inventory > Configuration > Warehouse Management > Warehouses".
#. Select all the warehouses you want to compute the rules in.
#. Click on "Action" and then in "Compute Cycle Count Rules". (**note**: A
   cron job will do this for every warehouse daily.)
#. Go to "Inventory Control > Cycle Counts".
#. Select a planned Cycle Count and confirm it, this will create a draft
   Inventory Adjustment.
#. In the right top corner of the form view you can access to the generated
   Inventory Adjustment.
#. Proceed with the Inventory Adjustment as usual.


Contributors
------------

* Lois Rilo <lois.rilo@eficent.com>
* Jordi Ballester Alomar <jordi.ballester@eficent.com>

