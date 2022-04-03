from odoo import models, fields, api, _

class ResPartner(models.Model):
    _inherit = 'res.partner'
    session = fields.Many2many('openacademy.session', readonly=True)
    is_instructor = fields.Boolean(_('Is instructor?'))
