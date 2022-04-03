from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import timedelta

class Session(models.Model):
    _name = 'openacademy.session'
    _description = _('Session')
    active = fields.Boolean(default=True)
    name = fields.Char(required=True)
    date_start = fields.Date(_('Start Date'), default=fields.Date.today())
    date_end = fields.Date(_('End Date'), compute='_calc_enddate', store=True)
    duration = fields.Integer()
    number_seats = fields.Integer(_('Number of seats'))
    instructor = fields.Many2one('res.partner', string=_('Instructor'),
                                 domain = ['|',('is_instructor', '=', True),('category_id.name','ilike','Teacher')])
    course = fields.Many2one('openacademy.course')
    attendees = fields.Many2many('res.partner', string=_('Attendees'))
    taken_seats = fields.Float(compute='_calc_percent_seats', string=_('Percent of taken seats'))
    qty_seats = fields.Float(compute='_calc_seats', string=_('Quantity of taken seats'), store=True)

    @api.depends('attendees','number_seats')
    def _calc_percent_seats(self):
        for record in self:
            if record.number_seats == 0:
                record.taken_seats = 0
            else:
                record.taken_seats = 100 * len(record.attendees) / record.number_seats

    @api.depends('attendees','number_seats')
    def _calc_seats(self):
        for record in self:
            record.qty_seats = len(record.attendees)

    @api.depends('date_start','duration')
    def _calc_enddate(self):
        for record in self:
            record.date_end = record.date_start + timedelta(days=self.duration)

    @api.onchange('attendees','number_seats')
    def _check_valid_sets(self):
        if len(self.attendees) > self.number_seats:
            return {'warning':{'title':_('There are no free seats'),
                               'message':_('Check the number of sets or quantity of attendees')}}
        if self.number_seats < 0:
            self.number_seats = 0
            return {'warning': {'title': _('Incorrect value'),
                                'message': _('Incorrect value in number of seats')}}

    @api.constrains('attendees','instructor')
    def _check_instructor(self):
        if self.instructor in self.attendees:
            raise ValidationError(_("Instructor can't be an attendee"))
