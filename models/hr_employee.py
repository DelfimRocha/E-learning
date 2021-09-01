# -*- coding: utf-8 -*-
from odoo import fields, models


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    #reporter = fields.One2many('e.learning', 'reported_by')


