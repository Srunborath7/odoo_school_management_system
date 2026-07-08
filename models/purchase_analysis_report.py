from odoo import fields, models, tools

class PurchaseAnalysisReport(models.Model):
    _name = 'school.purchase.analysis.report'
    _description = 'Purchase Analysis Report'
    _auto = False
    _order = 'date_order desc'

    name = fields.Char(string='Analysis Report')
    date_order = fields.Datetime(string='Order Date')
    partner_id = fields.Many2one('res.partner', string='Vendor', readonly=True)
    product_id = fields.Many2one('product.product', string='Product', readonly=True)
    approval_state = fields.Selection(
        [('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')],
        readonly=True,
    )
    qty_ordered = fields.Float(string='Qty Ordered', readonly=True)
    price_total = fields.Monetary(string='Total', readonly=True)
    currency_id = fields.Many2one('res.currency', readonly=True)
    company_id = fields.Many2one('res.company', readonly=True)

    def init(self):
        tools.drop_view_if_exists(self.env.cr, self._table)
        self.env.cr.execute("""
            CREATE OR REPLACE VIEW %s AS (
                SELECT
                    pol.id AS id,
                    po.name AS name,
                    po.date_order AS date_order,
                    po.partner_id AS partner_id,
                    pol.product_id AS product_id,
                    po.approval_state AS approval_state,
                    pol.product_qty AS qty_ordered,
                    pol.price_total AS price_total,
                    po.currency_id AS currency_id,
                    po.company_id AS company_id
                FROM purchase_order_line pol
                JOIN purchase_order po ON po.id = pol.order_id
                WHERE pol.product_id IS NOT NULL
            )
        """ % self._table)