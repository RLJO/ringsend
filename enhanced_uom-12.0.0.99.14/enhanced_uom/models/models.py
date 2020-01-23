# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging


class product_uom_category_view(models.Model):
    _inherit = 'product.template'
    uom_category_name = fields.Char(string='UOM category', related='uom_id.category_id.name', readonly=True)
    uom_category_ids = fields.Many2many('uom.uom',string='Product UOMs', compute='_get_uoms')

    @api.depends('uom_id')
    def _get_uoms(self):
#        _logger = logging.getLogger(__name__)
        for record in self:
            result = self.env['uom.uom'].search([('category_id','=',record.uom_id.category_id.id)])
            record.uom_category_ids = result
#            _logger.error(result)
#        self.uom_category_ids = result

class MrpBomBetterUomLine(models.Model):
    _inherit = 'mrp.bom.line'
    
    @api.onchange('product_id')
    def onchange_product_id(self):
        result =  {}
#        _logger = logging.getLogger(__name__)
#        _logger.error("in onchange event")
        if self.product_id:
            self.product_uom_id = self.product_id.uom_id.id
            result['domain'] = {'product_uom_id': [('category_id', '=', self.product_id.uom_id.category_id.id)]}
        return result

class uom_superscript(models.Model):
    _inherit = 'uom.uom'

    @api.onchange('name')
    def onchange_name(self):
        if type(self.name) is str:
            self.name = self.name.replace("^2","²")
            self.name = self.name.replace("^3","³")
