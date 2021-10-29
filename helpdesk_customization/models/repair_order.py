from odoo import fields, models

class RepairOrder(models.Model):
    _inherit = "repair.order"

    x_vehicle_type = fields.Char("Vehicle Type", related="partner_id.x_vehicle_type")
    x_license_plate = fields.Char("License Plate", related="partner_id.x_license_plate")
    x_reported_by = fields.Char("Reported By")

    x_problem_analysis_mt = fields.Text("Problem Analysis MT")
    x_problem_analysis_cxx = fields.Text("Problem Analysis CXX")
    x_problem_resolution_mt = fields.Text("Problem Resolution MT")
    x_problem_resolution_cxx = fields.Text("Problem Resolution CXX")
