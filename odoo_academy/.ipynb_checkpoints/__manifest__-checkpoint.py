# -*- coding: utf-8 -*-

{
    'name' : 'Odoo Academy',
    'summary' : 'Academy app yp manage training',
    'description': """
        Academy module to manage training:
        -courses
        -sessions
        -attendees
    """,
    'autor' : 'Francisco Sanchez B',
    'website' : 'https://www.odoo.com',
    'category' : 'training',
    'license' : 'OPL-1',
    'version' : '0.1',
    'depends' : [],
    'data' : ['security/academy_security.xml',
              'security/ir.model.access.csv',
              'views/academy_menuitems.xml',
              'views/course_views.xml',
             ],
    'demo' : ['demo/academy_demo.xml'],
  
}
