from openerp import api, models

class SaleOrders(models.Model):
    _inherit = "sale"

    _sql_constraints = [
        ('unique_po','UNIQUE(client_order_ref)',('This is not an Unique PO.'))
    ]

