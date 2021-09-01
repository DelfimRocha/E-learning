from odoo import http


class Elearning(http.Controller):
    @http.route('/elearning/courses', auth='public', website=True)
    def index(self, **kw):
        course = http.request.env['elearning.course'].search([])
        return http.request.render('e-learning.courses_template', {'courses': course})


class Program(http.Controller):
    @http.route('/elearning/courses/<int:course_id>', auth='public', website=True)
    def program(self, course_id, **kw):
        program = http.request.env['elearning.course.program'].search([("course", "=", course_id)])
        return http.request.render('e-learning.program_template', {'programs': program})
