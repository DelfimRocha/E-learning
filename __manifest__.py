# -*- coding: utf-8 -*-
{
    'name': "E-learning",
    'version': '11.0',
    'depends': ['hr', 'base', 'website'],
    'author': "Alien-group",
    'category': 'E-learning',
    'sequence': 2,
    'summary': """
    E-learning for Odoo 
        """,
    'description': """   
    E-learning for Odoo
        """,
    'data': [
        'views/course.xml',
        'views/program.xml',
        'views/instructor.xml',
        'views/student.xml',
        'views/enrolment.xml',
        'views/templates.xml',
        'data/view.xml',
        'security/ir.model.access.csv'

    ],
    'demo': [
        'demo.xml',
    ],

    'application': True,
}
