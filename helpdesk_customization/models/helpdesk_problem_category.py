from odoo import fields, models

class HelpdeskProblemSubcategory(models.Model):
    _name = "helpdesk.problem.subcategory"
    _description = "Helpdesk Problem Subcategory"

    name = fields.Char()
    problem_category_id = fields.Many2one("helpdesk.problem.category")


class HelpdeskProblemCategory(models.Model):
    _name = "helpdesk.problem.category"
    _description = "Helpdesk Problem Category"

    name = fields.Char()
    subcategory_ids = fields.One2many("helpdesk.problem.subcategory", "problem_category_id")
