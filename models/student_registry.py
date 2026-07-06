from odoo import fields, models, api
from datetime import date
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError

class StudentRegistry(models.Model):
    _name = 'school.student.registry'
    _description = 'Student Registry'
    _inherit = ['mail.thread']

    name = fields.Char(string='Name', required=True, tracking=True)
    DOB = fields.Date(string='DOB', required=True,default='2005-01-01', tracking=True)
    phone = fields.Char(string='Phone', tracking=True)
    email = fields.Char(string='Email', tracking=True)
    address = fields.Char(string='Address', tracking=True)
    course_ids = fields.Many2one('school.course',string='Course', required=True, tracking=True)
    enrolled_date = fields.Date(
        string="Enrolled Date",
        default=fields.Date.today,
        required=True,
        tracking=True
    )

    status = fields.Selection(
        [
            ('draft', 'Draft'),
            ('enrolled', 'Enrolled'),
            ('graduated', 'Graduated'),
            ('cancelled', 'Cancelled')
        ],
        string="Status",
        default='draft',
        required=True,
        tracking=True
    )
    calc_age = fields.Integer(string="Calc Age", compute='_compute_calc_age')
    theme_primary = fields.Char(compute='_compute_theme_colors')
    theme_secondary = fields.Char(compute='_compute_theme_colors')
    text_color_primary= fields.Char(compute='_compute_theme_colors')
    text_color_secondary= fields.Char(compute='_compute_theme_colors')

    def action_enroll(self):
        for student in self:
            if not student.email:
                raise UserError(_("Please set an email address before enrolling %s.") % student.name)

            # Update status
            student.status = 'enrolled'

            # Send enrollment email
            student._send_enrollment_email()

    def action_graduate(self):
        self.write({'status': 'graduated'})
        self.message_post(body="Student graduated.")

    def action_cancel(self):
        self.write({'status': 'cancelled'})
        self.message_post(body="Student registration cancelled.")

    def action_reset_draft(self):
        self.write({'status': 'draft'})
        self.message_post(body="Student reset to draft.")

    @api.constrains('DOB')
    def _check_dob(self):
        for rec in self:
            if rec.DOB:
                age = date.today().year - rec.DOB.year
                if age < 18:
                    raise ValidationError("Student must be at least 18 years old to enroll.")

    @api.depends('DOB')
    def _compute_calc_age(self):
        for rec in self:
            if rec.DOB:
                rec.calc_age = date.today().year - rec.DOB.year
            else:
                rec.calc_age = 0

    @api.depends()
    def _compute_theme_colors(self):
        theme = self.env['school.setting'].search(
            [('active', '=', True)],
        )

        for rec in self:
            rec.theme_primary = theme.primary_color
            rec.theme_secondary = theme.secondary_color
            rec.text_color_primary = theme.text_color_primary
            rec.text_color_secondary = theme.text_color_secondary

    def _send_enrollment_email(self):
        self.ensure_one()
        template = self.env.ref(
            'school_management_system.email_template_student_enrollment',
            raise_if_not_found=False
        )
        if template:
            template.send_mail(self.id, force_send=True)
        else:
            mail_values = {
                'subject': 'Enrollment Confirmation',
                'body_html': '<p>Dear %s,</p><p>You have been successfully enrolled.</p>' % self.name,
                'email_to': self.email,
                'email_from': 'srunborath44@gmail.com',
            }
            self.env['mail.mail'].create(mail_values).send()