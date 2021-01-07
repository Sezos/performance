
from odoo import models, fields, api


class screen5(models.Model):
    _name = 'screen5'
    _description = 'screen5'
    
    department = fields.Char()
    work = fields.Char()
    date = fields.Datetime(default=fields.Datetime.now())
    assigned_to = fields.Char()
    position = fields.Char()
