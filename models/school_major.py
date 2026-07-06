from reportlab.lib.validators import inherit

from odoo import fields, models

class SchoolMajor(models.Model):
    _name = 'school.major'
    _description = 'School Major'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Major Name',equired=True, tracking=True)
    department_ids = fields.Many2one('school.department', string='Departments', equired=True, tracking=True)
    description = fields.Char(string='Major Description')
    status = fields.Selection([
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('cancel', 'Cancel'),
    ], string='Status', default='draft', equired=True, tracking=True)