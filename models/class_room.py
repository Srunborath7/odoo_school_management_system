from odoo import fields, models

class ClassRoom(models.Model):
    _name = 'school.class.room'
    _description = 'School Classroom'

    name = fields.Char(required=True)
    floor = fields.Char(required=True)
    capacity = fields.Integer(required=True)
    academic_year_ids = fields.Many2one('school.academic.year' ,string="Academic Year", required=True)
    teacher_ids = fields.Many2one('school.teacher', string="Teacher", required=True)
    course_ids = fields.Many2one('school.course', string="Course", required=True)
    semester = fields.Integer(string="Semester", required=True)
    year = fields.Integer(string="Year", required = True)
    status = fields.Selection([
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('completed', 'Completed'),
    ] ,default='active')
    description = fields.Char(string="Description", required=True)
    