from openerp import api, models

class SaleOrder(models.Model):
    _inherit = "sale.order"

    _sql_constraints = [
        ('unique_po','UNIQUE(client_order_ref)',('This is not an Unique PO.'))
    ]
    _sql_constraints = [
        ('value_company_uniq', 'unique (client_order_ref)', 'This attribute value already exists !')
    ]
