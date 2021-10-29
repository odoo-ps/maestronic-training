from odoo import _, api, fields, models


class HelpdeskTicket(models.Model):
    _inherit = "helpdesk.ticket"

    code_sequence = fields.Integer("Sequence")
    direct_fs_intervention = fields.Boolean(string="Direct fs intervention")

    x_driver = fields.Char("Driver")
    x_gps_coordinates = fields.Char("GPS Coordinates")
    x_license_plate = fields.Char("License Plate", related="partner_id.x_license_plate")
    x_line = fields.Char("Line")
    x_relocation_trip = fields.Char("Relocation Trip")
    x_reporter = fields.Char("Reporter")
    x_roundtrip = fields.Char("Roundtrip")
    x_stop = fields.Char("Stop")
    x_trip = fields.Char("Trip")
    x_trip_start_time = fields.Char("Trip Start Time")
    x_vehicle_location = fields.Char("Vehicle Location")
    x_vehicle_type = fields.Char("Vehicle Type", related="partner_id.x_vehicle_type")

    # Description : All other incidents/ticket related to this bus.
    x_related_incident_ids = fields.Many2many(
        "helpdesk.ticket", string="Related Incidents", compute="_compute_x_related_incident_ids"
    )

    x_concession_id = fields.Many2one("helpdesk.concession", string="Concession")
    x_customer_id = fields.Many2one("res.partner", related="partner_id.parent_id", string="Customer")

    # Description : selections TBC
    # x_problem_category = fields.Selection([('cat_1', "Category 1"), ('cat_2', "Category 2")], "Problem Category")
    # x_resolution_category = fields.Selection([('cat_1', "Category 1"), ('cat_2', "Category 2")], "Resolution Category")
    x_problem_category = fields.Many2one("helpdesk.problem.category", string="Problem Category")
    x_problem_subcategory = fields.Many2one("helpdesk.problem.subcategory", domain="[('problem_category_id', '=', x_problem_category)]", string="Problem Subcategory")
    x_resolution_category = fields.Many2one("helpdesk.solution.category", string="Resolution Category")
    x_resolution_subcategory = fields.Many2one("helpdesk.solution.subcategory", domain="[('solution_category_id', '=', x_resolution_category)]", string="Resolution Subcategory")

    # x_customer_case = fields.Text("Customer Case")

    @api.depends('partner_id')
    def _compute_x_related_incident_ids(self):
        for rec in self:
            rec.x_related_incident_ids = [(6, 0, (self.search([('partner_id', '=', rec.partner_id.id)]) - self).ids)]

    def action_view_related_incidents(self):
        action = {
            'type': 'ir.actions.act_window',
            'name': _("Incidents"),
            "res_model": "helpdesk.ticket",
            "view_mode": "tree,form",
            "domain": [('id', 'in', self.x_related_incident_ids.ids)],
        }
        return action

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('team_id'):
                team = self.env['helpdesk.team'].browse(vals.get('team_id'))
                vals['code_sequence'] = team.tickets_no
                team.tickets_no += 1
        return super().create(vals_list)

    def name_get(self):
        """{team_id.code}-code_sequence"""
        res = []
        for ticket in self:
            if not ticket.team_id:
                res += super(HelpdeskTicket, ticket).name_get()
            else:
                res.append((ticket.id, "%s-%06d" % (ticket.team_id.code, ticket.code_sequence)))
        return res
