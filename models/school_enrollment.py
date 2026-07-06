from odoo import models, fields, api


class SchoolEnrollment(models.Model):
    _name = "school.enrollment"
    _description = "School Enrollment"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name")
    student_id = fields.Many2one('school.student.registry', string="Student")
    batch_id = fields.Many2one('school.batch', string="Batch")
    curriculum_id = fields.Many2one('school.curriculum', string="Curriculum")
    academic_program = fields.Char(related="curriculum_id.academic_program_id.name", string="Academic Program")
    major = fields.Char(related="curriculum_id.major_id.name", string="Major")
    academic_year = fields.Char(related="curriculum_id.academic_year_id.name", string="Academic Year")
    academic_year_level = fields.Char(related="curriculum_id.academic_level_id.name" , string="Academic Year Level")
    description = fields.Char(string="Description")
    status = fields.Selection([
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('closed', 'Closed'),
    ], default='draft', tracking=True)
    @api.model
    def create(self, vals):
        if vals.get("name", "New") == "New":
            vals["name"] = self.env["ir.sequence"].next_by_code(
                "school.enrollment"
            ) or "New"
        return super().create(vals)