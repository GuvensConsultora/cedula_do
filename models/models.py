# -*- coding: utf-8 -*-
from odoo import models, api
from odoo.exceptions import ValidationError

class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.constrains('vat')
    def check_vat_do(self):
        for record in self:
            if record.vat and len(record.vat) not in [9, 11]:
                raise ValidationError("El número de cédula no es válido. Debe tener 9 o 11 dígitos.")
