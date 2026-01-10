#-*- coding: utf-8 -*-

from odoo import fields, models
import re
from odoo.exceptions import ValidationError
from datetime import date
from dateutil.relativedelta import relativedelta

class Printer(models.Model):
    _name = 'lynxter.printer'
    _description = 'Description of printer'

    active=fields.Boolean("Actif ?", default=True)

    num_serie = fields.Char("Serial number", required=True)
    manufacture_date = fields.Date(string="Manufacture date")
    model = fields.Char("Model")
    thumbnail = fields.Binary("Thumbnail")
    
    state = fields.Selection([
        ('broken','Broken Down'),
        ('repaired', 'Being repaired'),
        ('usable', 'Usabled')
    ])
    
    def _check_num_serie(self):
        self.ensure_one()
        pattern = re.compile("\w{2}[0-9]{3}\w{2}$")
        return pattern.match(self.num_serie)
    
    def button_check_num_serie(self):
        for printer in self:
            if not printer.num_serie:
                raise (ValidationError("Please provide a serial number for this printer"))
            if printer.num_serie and not printer._check_num_serie():
                raise ValidationError("%s Serial number is invalid" % (printer.num_serie))
        return True