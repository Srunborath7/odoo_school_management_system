from odoo import fields, models

class Department(models.Model):
    _name = 'school.department'
    _description = 'Department'
    _inherit = ['mail.thread']

    name = fields.Char(string="Department Name", required=True, tracking=True)
    phone = fields.Char(string="Phone Number", required=True, tracking=True)
    email = fields.Char(string="Email Address", required=True, tracking=True)
    head_teacher = fields.Many2one("school.teacher",string="Head Teacher", required=True, tracking=True)
    faculty = fields.Char(string="Faculty", required=True, tracking=True)
    note = fields.Text(string="Note")