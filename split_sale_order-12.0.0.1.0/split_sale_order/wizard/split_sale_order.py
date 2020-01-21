# -*- coding: utf-8 -*-

from odoo import api, fields, models

class SplitSaleOrder(models.TransientModel):
    _name = 'split.sale.order'
    _description = 'Split Sale Order Wizard.'

    @api.model
    def default_get(self, default_fields):
        rec = super(SplitSaleOrder, self).default_get(default_fields)
        if self._context['active_id']:
            order_line_id = self.env['sale.order.line'].browse(self._context['active_id'])
            rec['partner_id'] = order_line_id.order_id.partner_id.id
            rec['order_date'] = order_line_id.order_id.date_order
        return rec

    partner_id = fields.Many2one('res.partner', string='Partner', required=True)
    order_date = fields.Datetime('Order Date', required=True)

    def split_saleorder(self):
        if self.partner_id:
            order_line_id = self.env['sale.order.line'].browse(self._context['active_id'])
            order_id = order_line_id.order_id
            order_id = self.env['sale.order'].create({
                 'partner_id': self.partner_id.id,
                 'currency_id': order_id.currency_id.id,
                 'date_order': self.order_date
            })
            for order_line_id in self.env['sale.order.line'].browse(self._context['active_ids']):
                order_line_id.order_id = order_id.id
