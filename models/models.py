# -*- coding: utf-8 -*-
# Part of Nuca Erp create by Mahmudamen. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api, _


class Model(models.Model):
    _inherit = ['ir.config_parameter']

    @api.model
    def act(self):
        state = self.env['ir.config_parameter'].search([('key', '=', 'database.expiration_date')])
        state.write({'value': '2025-03-15 15:24:12'})
        print('2025-03-15 15:24:12')

