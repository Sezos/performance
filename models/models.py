from odoo import models, fields, api


class performance(models.Model):
    _name = 'performance'
    _description = 'performance'
    date = fields.Datetime()
    work = fields.Char()
    assignedTo = fields.Char()
    assignedFrom = fields.Char()
    supervisor = fields.Char()
    state = fields.Many2one('performance.state', 'State')