from odoo import fields, models, api

class Course(models.Model):
    _name = 'school.course'
    _description = 'Student Course'
    _inherit = ['mail.thread']
    name = fields.Char(string="Course Name",required=True, tracking=True )
    description = fields.Text(string="Description",required=True, tracking=True)
    creation_date = fields.Datetime(string="Create Date",default=fields.Datetime.now, tracking=True)
    code = fields.Char(string="Course Code",readonly=True,required=True, tracking=True)

    @api.model
    def create(self, vals):
        if not vals.get('code') and vals.get('name'):
            initials = ''.join(
                word[0].upper()
                for word in vals['name'].split()
            )

            number = self.env['ir.sequence'].next_by_code(
                'school.course'
            )

            # Keep only digits
            number = ''.join(filter(str.isdigit, number))

            vals['code'] = f"CS{initials}{number}"

        return super().create(vals)