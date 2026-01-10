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

    serial_number = fields.Char("Serial number", required=True)
    manufacture_date = fields.Date(string="Manufacture date")
    sending_date = fields.Date(string="Sending date")
    location = fields.Char("Location")
    model = fields.Char("Model")
    thumbnail = fields.Binary("Thumbnail")
    
    state = fields.Selection([
        ('broken','Broken Down'),
        ('repaired', 'Being repaired'),
        ('usable', 'Usabled')
    ])
    
    def _sending_date(self):
        self.ensure_one()
        if self.manufacture_date and self.sending_date:
            manufacture_plus_2weeks = self.manufacture_date + relativedelta(weeks=2)
            if self.sending_date < manufacture_plus_2weeks:
                raise ValidationError("The sending date must be at least 2 weeks after the manufacture date")
        return True
    
    def button_check_sending_date(self):
        for printer in self:
            if not printer._sending_date():
                raise ValidationError("The sending date is invalid")
        return True