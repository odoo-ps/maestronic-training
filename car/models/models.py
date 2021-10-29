# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Car(models.Model):
    _name = 'car.car'
    _description = 'car.car'

    # fields/attributes of Car
    name = fields.Char()
    brand = fields.Char()
    miles = fields.Integer()

class HelpdeskTicket(models.Model):
    _inherit = "helpdesk.ticket"

    additional_note = fields.Text()
    car = fields.Many2one('car.car')
