from odoo import models, fields, _
from datetime import date

class Transactions(models.Model):
    _name = 'perpus.transactions'
    _description = 'Transaksi Buku'
    
    name = fields.Char(string='Title')
    description = fields.Text(string='Description')
    rent_date = fields.Date(string='Tanggal Pinjam')
    return_date = fields.Date(string='Tanggal Kembali')