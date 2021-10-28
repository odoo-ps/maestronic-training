# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Car(models.Model):
    _name = 'car.car'
    _description = 'car.car'

    # fields/attributes of Car
    name = fields.Char()
    brand = fields.Char()
    miles = fields.Integer()
