from odoo import fields, models

class Material(models.Model):
    _name = 'lynxter.material'
    _description = 'Description of material'

    name = fields.Char("Material Name", required=True)
    type = fields.Selection([
        ('FIL', 'Filament'),
        ('LIQ', 'Liquid'),
        ('PAS', 'Paste')
    ], string="Material Type", required=True)
    color = fields.Char("Color")
    manufacturer = fields.Char("Manufacturer")
    

    #Vérifier si un matériel est compatible avec une imprimante donnée
