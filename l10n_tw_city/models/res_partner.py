# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Partner(models.Model):
    _inherit = 'res.partner'

    city_id = fields.Many2one('res.city', string='City of Address', domain="[('state_id', '=', state_id)]")

    @api.onchange('state_id')
    def _onchange_state(self):
        super(Partner, self)._onchange_state()
        if self.state_id and self.state_id != self.city_id.state_id:
            self.city_id = False

    @api.onchange('city_id')
    def _onchange_city_id(self):
        if self.city_id:
            self.city = self.city_id.name
            self.zip = self.city_id.zipcode
            self.state_id = self.city_id.state_id
