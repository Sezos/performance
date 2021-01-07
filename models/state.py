
from odoo import models, fields, api


class performanceState(models.Model):
    _name = 'performance.state'
    _description = 'performance.state'
    name = fields.Char()
    