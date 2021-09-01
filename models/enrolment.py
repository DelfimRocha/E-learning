from odoo import models, fields, api
from datetime import datetime


class ElearningEnrolment(models.Model):
    _name = 'elearning.enrolment'

    name = fields.Char(string="Name")
    user_id = fields.Many2one('res.users', string="User")
    course_id = fields.Many2one('elearning.course', string="Course")
    data_enrolment = fields.Date(default=datetime.today(), sting="Data of Enrolment")
    data_completion = fields.Date(string="Data of Completion")
    state = fields.Selection(
        [('new', 'Start course'),
         ('progress', 'In Progress'),
         ('finished', 'finished course'),
         ('cancel', 'Cancelled')],
        string="Status", readonly=True, store=True, default='new')

    @api.multi
    def started_progressbar(self):
        self.write({'state': 'new'})

    @api.multi
    def progress_progressbar(self):
        self.write({'state': 'progress'})

    @api.multi
    def done_progressbar(self):
        self.write({'state': 'finished'})

    @api.multi
    def cancel_progressbar(self):
        self.write({'state': 'cancel'})
