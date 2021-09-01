#from datetime import timedelta
from odoo import models, fields, api
#from datetime import datetime


class Course(models.Model):
    _name = 'learning.course'

    course_name = fields.Char(string="Name", required=True)
    course_description = fields.char(string="Description", required=True)
    course_version = fields.char(string="Version", required=True)
