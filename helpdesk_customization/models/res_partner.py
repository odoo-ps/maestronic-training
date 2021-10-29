from odoo import fields, models

class ResPartner(models.Model):
    _inherit = "res.partner"

    x_vehicle_type = fields.Char("Vehicle Type")
    x_license_plate = fields.Char("License Plate")
