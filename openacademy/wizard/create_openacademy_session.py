from odoo import models, fields

class OpenAcademySessionsWizard(models.TransientModel):
    _name = 'openacademy.wizard.session'
    _description = 'Create sessions wizard'

    def default_session(self):
        return self.env['openacademy.session'].browse(self._context.get('active_id'))

    session_id = fields.Many2many('openacademy.session', string="Session", required=True, default=default_session)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")

    def subscribe(self):
        self.session_id.attendees |= self.attendee_ids
        return {}
