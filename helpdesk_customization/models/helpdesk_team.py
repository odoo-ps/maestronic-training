# TODO: apply sequence code and number
from odoo import fields, models

class HelpdeskTeam(models.Model):
    _inherit = "helpdesk.team"

    tickets_no = fields.Integer("Sequence", default=1)
    code = fields.Char(default="TICK")
    # company_restrict = fields.Many2many("res.partner", domain="[('is_company', '=', True)]")
