# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models,api


class ProductStockQuantity(models.Model):
    _name = 'product.template'

    stock_level = fields.Integer('Stock level')

    @api.onchange('stock_level')
    def _onchange_stock_level(self):
        print("Stock level ", self.stock_level)
        template_obj = self.env['mail.mail']
        template_data = {
                        'subject': 'Niveau de stock modifier Notification ' ,
                        'body_html':  '<p>Niveau de stock modifier </p>',
                        'email_from': sender,
                        'email_to': "admin@admin.com"
                        }
        template_id = template_obj.create(template_data)
        template_obj.send(template_id)
        pass
    
