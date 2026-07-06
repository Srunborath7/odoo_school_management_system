{
    'name': 'School Management System',
    'version': '1.0',
    'category': 'Education',
    'summary': 'School Management',
    'author': 'RMA Cambodia',
    'license': 'LGPL-3',

    'depends': [
        'base',
        'mail'
    ],

    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'data/mail_template.xml',
        'security/record_rules.xml',
        'views/student_registry_views.xml',
        'views/student_course_views.xml',
        'views/department_views.xml',
        'views/teacher_views.xml',
        'views/school_setting_views.xml',
        'views/batch_views.xml',
        'views/time_table_slot_views.xml',
        'views/academic_program_views.xml',
        'views/academic_year_views.xml',
        'views/academic_year_level_views.xml',
        'views/school_major_views.xml',
        'views/class_room_views.xml',
        'views/room_views.xml',
        'views/school_curriculum_views.xml',
        'views/school_enrollment_views.xml',
        'views/menu.xml',
    ],
    'assets': {
            'web.assets_backend': [
                'school_management_system/static/src/css/timetable_calendar.css',
            ],
        },
    'application': True,
    'installable': True,
}