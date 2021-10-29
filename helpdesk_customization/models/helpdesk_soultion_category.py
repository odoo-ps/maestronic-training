from odoo import fields, models

class HelpdeskSolutionSubcategory(models.Model):
    _name = "helpdesk.solution.subcategory"
    _description = "Helpdesk Solution Subcategory"

    name = fields.Char()
    solution_category_id = fields.Many2one("helpdesk.solution.category")


class HelpdeskSolutionCategory(models.Model):
    _name = "helpdesk.solution.category"
    _description = "Helpdesk Solution Category"

    name = fields.Char()
    subcategory_ids = fields.One2many("helpdesk.solution.subcategory", "solution_category_id")
