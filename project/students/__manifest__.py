{
    'name': 'Student Module',
    'version': '1.0',
    'category': 'Uncategorized',
    'summary': 'Module for managing student profiles',
    'description': """A module for managing student profiles.""",
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'security/access_right.xml',
        'views/student_templete.xml',
        'views/student_templete.xml',
        'views/school_view.xml',
        'views/cource_view.xml',
        'views/student_view.xml',


    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}




