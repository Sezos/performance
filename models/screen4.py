
from odoo import models, fields, api


class screen4(models.Model):
    _name = 'screen4'
    _description = 'screen4'
    
    department = fields.Char()
    work = fields.Char()
    date = fields.Datetime(default=fields.Datetime.now())
    shift = fields.Char()
    position = fields.Char()
    assigned_to = fields.Char()
    supervisor = fields.Char()
    verified_by = fields.Char()