from odoo import fields, models


class ElearningInstructor(models.Model):
    _name = 'elearning.instructor'

    courses = fields.Many2many('elearning.course', string="Courses")
    user_id = fields.Many2one('res.users', string="User")
    partner_id = fields.Many2one('res.partner', string="Partner")

    name = fields.Char(index=True, related='partner_id.name')
    phone = fields.Char(related='partner_id.phone')
    street = fields.Char(related='partner_id.street')
    city = fields.Char(related='partner_id.city')
    email = fields.Char(related='partner_id.email')

    image = fields.Binary("Image", attachment=True,
                          help="This field holds the image used as avatar for this contact, limited to 1024x1024px",
                          related='partner_id.image')
