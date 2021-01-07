
from odoo import models, fields, api


class screen3(models.Model):
    _name = 'screen3'
    _description = 'screen3'
    
    ID = fields.Integer(compute="random_ID")
    applied_from = fields.Char()
    applied_to = fields.Char()
    description = fields.Char()
    job_order_location = fields.Char()
    
    def random_ID(self):
        self.ID = 1