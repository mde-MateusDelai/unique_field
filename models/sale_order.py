from openerp import addons
from openerp import models, fields, api, _
from openerp.exceptions import UserError, RedirectWarning, ValidationError


class sale_order(models.Model):
	_inherit = ['sale.order']

_sql_constraints = [
        ('code_company_uniq', 'UNIQUE(client_order_ref)','The code of the account must be unique per company !')
    ]
