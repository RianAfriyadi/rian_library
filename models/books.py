from odoo import models, fields, _
from datetime import date

class Books(models.Model):
    _name = 'perpus.books'
    _description = 'Master Data Buku'
    
    name = fields.Char(string='Title')
    description = fields.Text(string='Description')
    total = fields.Float(string='Total')