# TODO: apply sequence code and number
from odoo import fields, models

class HelpdeskTeam(models.Model):
    _inherit = "helpdesk.team"

    tickets_no = fields.Integer("Sequence", default=1)
    code = fields.Char(default="TICK")
