# -*- coding: utf-8 -*-
# Copyright 2018 Mateus - Mateus Delai <mde@odoo.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

{
    'name': 'Unique PO per Customer a',
    'version': '9.0.1.0.1',
    'category': 'Denker',
    'author': 'Mateus Delai',
    'website': "",
    'license': 'AGPL-3',
    'depends': ['sale'],
    'data': [
        'sale_order.xml',
    ],
    'installable': True,
    'auto_install': False
}
