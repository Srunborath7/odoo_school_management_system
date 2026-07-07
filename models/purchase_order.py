from odoo import models, fields

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    approval_state = fields.Selection([
        ('pending', 'Pending Approval'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ], string="Approval Status", default='pending', tracking=True)
    approved_by = fields.Many2one('res.users', string="Approved By", readonly=True)
    approved_date = fields.Datetime(string="Approved On", readonly=True)
    approval_notes = fields.Text(string="Approval Notes")

    def action_custom_approve(self):
        self.write({
            'approval_state': 'approved',
            'approved_by': self.env.user.id,
            'approved_date': fields.Datetime.now(),
        })

    def action_custom_reject(self):
        self.write({'approval_state': 'rejected'})