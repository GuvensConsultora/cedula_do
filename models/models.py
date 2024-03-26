# -*- coding: utf-8 -*-

from odoo import models, api
from odoo.exceptions import ValidationError

class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.constrains('vat', 'country_id')
    def check_vat_do(self):
        for record in self:
            if record.country_id.code == 'DO' and record.vat:
                if len(record.vat) not in [9, 11]:
                    raise ValidationError("El número de cédula dominicano no es válido. Debe tener 9 o 11 dígitos.")
