from openerp import api, models

class ResPartner(models.Model):
    _inherit = "sale.order"

    _sql_constraints = [
        ('unique_po',
         'UNIQUE (client_order_ref)',
         _('This is not an Unique PO.'))
    ]
