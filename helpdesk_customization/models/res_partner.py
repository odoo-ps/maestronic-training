from odoo import fields, models

class ResPartner(models.Model):
    _inherit = "res.partner"

    x_vehicle_type = fields.Char("Vehicle Type")
    x_license_plate = fields.Char("License Plate")
    x_concession_id = fields.Many2one("helpdesk.concession", string="Concession")
