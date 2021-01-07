
from odoo import models, fields, api


class performanceState(models.Model):
    _name = 'screen2'
    _description = 'screen2'
    
    ID = fields.Integer(compute="random_ID")
    from_who = fields.Char()
    from_where = fields.Char()
    works = fields.Char()
    date_begin = fields.Datetime(default=fields.Datetime.now())
    date_end = fields.Datetime(default=fields.Datetime.now())
    assigned_to = fields.Char()
    accepted_by = fields.Char()

    def random_ID(self):
        self.ID = 1