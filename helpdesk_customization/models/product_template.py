from odoo import fields, models

class ProductTemplate(models.Model):
    _inherit = "product.template"

    customer_access = fields.Many2many("res.partner", string="Customer Access", domain="[('is_company', '=', True)]")
