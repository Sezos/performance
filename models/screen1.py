from odoo import models, fields, api

class screen1(models.Model):
    _name = 'screen1'
    _description = 'screen1'
    ID = fields.Integer(compute="random_ID")
    department = fields.Char()
    work = fields.Char()
    date_begin = fields.Datetime(default=fields.Datetime.now())
    date_end = fields.Datetime(default=fields.Datetime.now())
    assigned_to = fields.Char()
    supervisor = fields.Char()
    verified_by = fields.Char()

    def random_ID(self):
        self.ID = 1