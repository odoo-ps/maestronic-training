from odoo import _, api, fields, models


class HelpdeskConcession(models.Model):
    _name = "helpdesk.concession"
    _description = "Helpdesk concession"

    name = fields.Char()
