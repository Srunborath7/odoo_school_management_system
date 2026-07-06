from odoo import fields, models, api

class Subject(models.Model):
    _name = 'school.subject'
    _description = 'School Subject'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name", required=True, tracking=True)

    time_duration = fields.Integer(string="Time Duration (Hours)", required=True, tracking=True)

    teacher_ids = fields.Many2many(
        'school.teacher',
        string="Teachers",
        tracking=True
    )

    class_room_ids = fields.Many2many(
        'school.class.room',
        string="Classrooms",
        tracking=True
    )

    description = fields.Text(string="Description")

    status = fields.Selection([
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('completed', 'Completed'),
    ], default='draft', string="Status", tracking=True)

    def action_active(self):
        self.write({'status': 'active'})

    def action_completed(self):
        self.write({'status': 'completed'})

    def action_inactive(self):
        self.write({'status': 'inactive'})

    def action_reset_draft(self):
        self.write({'status': 'draft'})