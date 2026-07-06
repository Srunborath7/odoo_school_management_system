from odoo import models, fields, api


class SchoolCurriculum(models.Model):
    _name = 'school.curriculum'
    _description = 'School Curriculum'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'name'

    name = fields.Char(string="Curriculum Name",compute="_compute_name",store=True,tracking=True,)
    major_id = fields.Many2one('school.major',string="Major",required=True,tracking=True,)
    academic_program_id = fields.Many2one('school.academic.program',string="Academic Program",required=True,tracking=True,)
    academic_year_id = fields.Many2one('school.academic.year',string="Academic Year",required=True,tracking=True,)
    academic_level_id = fields.Many2one('school.academic.year.level',string="Academic Year Level",required=True,tracking=True,)
    course_ids = fields.Many2many('school.course','school_curriculum_course_rel','curriculum_id','course_id',string="Courses",tracking=True,)
    total_credit = fields.Integer(string="Total Credit",store=True,)
    description = fields.Text(string="Description")

    status = fields.Selection([
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('closed', 'Closed'),
    ], default='draft', tracking=True)

    @api.depends(
        'major_id.name',
        'academic_level_id.name',
        'academic_level_id.semester'
    )
    def _compute_name(self):
        for rec in self:
            rec.name = "%s Year %s Semester %s" % (
                rec.major_id.name or "",
                rec.academic_level_id.name or "",
                rec.academic_level_id.semester or ""
            )


    def action_active(self):
        self.write({'status': 'active'})
        self.message_post(body="Curriculum has been activated.")

    def action_inactive(self):
        self.write({'status': 'inactive'})
        self.message_post(body="Curriculum has been set to inactive.")

    def action_closed(self):
        self.write({'status': 'closed'})
        self.message_post(body="Curriculum has been closed.")

    def action_reset_draft(self):
        self.write({'status': 'draft'})
        self.message_post(body="Curriculum has been reset to draft.")