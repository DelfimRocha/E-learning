from odoo import fields, models


class CourseProgram(models.Model):
    _name = 'elearning.course.program'

    name = fields.Char()
    description = fields.Text(string="Description", )
    media_type = fields.Selection([('video', 'Video'), ('pdf', 'Pdf'), ('audio', 'Audio')], string="Media Type")
    media_url = fields.Char(string="URL Media", )
    course = fields.Many2one('elearning.course', string='Course')
