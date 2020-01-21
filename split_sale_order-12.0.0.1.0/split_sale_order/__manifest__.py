# -*- coding: utf-8 -*-
{
    'name': 'Split Sales Order',
    'summary': "Split Sales Order and create New Sale order with selected lines and Partner",
    'description': "Split Sales Order",

    'author': 'iPredict IT Solutions Pvt. Ltd.',
    'website': 'http://ipredictitsolutions.com',
    'support': 'ipredictitsolutions@gmail.com',

    'category': 'Sales',
    'version': '13.0.0.1.0',
    'depends': ['sale_management'],

    'data': [
        'security/split_security.xml',
        'views/split_sale_order.xml',
        'wizard/split_sale_order_wizard.xml',
    ],

    'license': "OPL-1",
    'price': 10,
    'currency': "EUR",

    'auto_install': False,
    'installable': True,

    'images': ['static/description/banner.png'],
}
