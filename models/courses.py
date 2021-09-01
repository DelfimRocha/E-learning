# from datetime import timedelta
from odoo import models, fields, api
from datetime import datetime


class Course(models.Model):
    _name = 'elearning.course'

    course_name = fields.Char(string="")
    course_description = fields.Text(string="Description", required=True)
    course_version = fields.Char(string="Version", required=True)
    course_author = fields.Char(string="Author", required=True)
    programs = fields.One2many('elearning.course.program', 'course')
    instructors = fields.Many2many('elearning.instructor')
    data_creation = fields.Date(default=datetime.today(), string="Data of Creation")
    enrolment = fields.One2many('elearning.enrolment', 'course_id')
    image = fields.Binary("Image", attachment=True,
                          help="This field holds the image used as avatar for this contact, limited to 1024x1024px")
    image_medium = fields.Binary()
    image_small = fields.Binary()
