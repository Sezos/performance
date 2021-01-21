from odoo import models, fields, api

class screen1(models.Model):
    _name = 'screen1'
    _description = 'screen1'

    department = fields.Char()
    work = fields.Text()
    date_begin = fields.Datetime(default=fields.Datetime.now())
    date_end = fields.Datetime(default=fields.Datetime.now())
    assigned_to = fields.Char()
    supervisor = fields.Char()
    verified_by = fields.Char()