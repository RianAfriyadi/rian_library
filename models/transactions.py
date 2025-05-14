from odoo import models, fields, _
from odoo.exceptions import UserError

class Transactions(models.Model):
    _name = 'perpus.transactions'
    _description = 'Transaksi Buku'
    
    name = fields.Char(string='Name')
    description = fields.Text(string='Description')
    rent_date = fields.Date(string='Tanggal Pinjam')
    return_date = fields.Date(string='Tanggal Kembali')

    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("progress", "Progress"),
            ("done", "Done")
        ], string='Status', default="draft"
    )

    partner_id = fields.Many2one(
        'res.partner',
        string='Partner')

    book_id = fields.Many2one(
        'perpus.books',
        string='Buku',
        domain=[('available_book', '>', 0)]
    )
    
    def action_state_progress(self):
        if self.state not in ('draft'):
            raise UserError('Hanya untuk status Draft')
        self.rent_date = fields.Datetime.now()
        self.state = 'progress'

    def action_state_done(self):
        if self.state not in ('progress'):
            raise UserError('Hanya untuk status Progress')
        self.return_date = fields.Datetime.now()
        self.state = 'done'