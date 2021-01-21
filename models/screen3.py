
from odoo import models, fields, api


class screen3(models.Model):
    _name = 'screen3'
    _description = 'screen3'

    applied_from = fields.Char()
    applied_to = fields.Char()
    description = fields.Text()
    job_order_location = fields.Char()