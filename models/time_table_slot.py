from odoo import fields, models, api

class TimeTableSlot(models.Model):
    _name = 'school.timetable.slot'
    _description = 'TimeTable Slot'
    name = fields.Char(string="Title", compute="_compute_name", required=True)
    day_of_week = fields.Selection([
        ('mon', 'Monday'),
        ('tue', 'Tuesday'),
        ('wed', 'Wednesday'),
        ('thu', 'Thursday'),
        ('fri', 'Friday'),
        ('sat', 'Saturday'),
        ('sun', 'Sunday'),
    ], required=True)

    start_time = fields.Datetime(string="Start Time", required=True)
    end_time = fields.Datetime(string="End Time", required=True)

    academic_year_id = fields.Many2one('school.academic.year', required=True)
    program_id = fields.Many2one('school.academic.program', required=True)
    class_id = fields.Many2one('school.class.room', required=True)

    subject_id = fields.Many2one('school.subject', required=True)
    teacher_id = fields.Many2one('school.teacher', required=True)

    color = fields.Integer(string="Color Index")
    is_active = fields.Boolean(default=True)
    duration = fields.Float(
        string="Duration (Hours)",
        compute="_compute_duration",
        store=True
    )

    @api.depends('day_of_week', 'start_time', 'end_time', 'subject_id', 'class_id')
    def _compute_name(self):
        for rec in self:
            rec.name = f"{rec.class_id.name or ''} - {rec.subject_id.name or ''} ({rec.day_of_week})"

    @api.depends('start_time', 'end_time')
    def _compute_duration(self):
        for rec in self:
            if rec.start_time and rec.end_time:
                delta = rec.end_time - rec.start_time
                rec.duration = delta.total_seconds() / 3600
            else:
                rec.duration = 0.0