from odoo import models, fields, api, _
from datetime import date

class Books(models.Model):
    _name = 'perpus.books'
    _description = 'Master Data Buku'
    
    name = fields.Char(string='Title')
    description = fields.Text(string='Description')
    total = fields.Float(string='Total')

    transaction_ids = fields.One2many(
        comodel_name='perpus.transactions',
        inverse_name='book_id',
        string='Transaksi'
    )

    available_book = fields.Integer(
        string='Buku Tersedia',
        compute='_compute_available_book',
        store=True
    )
    
    @api.depends('transaction_ids.state', 'total')
    def _compute_available_book(self):
        for rec in self:
            i_transaction_progress = rec.transaction_ids.filtered(lambda x: x.state == 'progress')
            rec.available_book = rec.total - len(i_transaction_progress)