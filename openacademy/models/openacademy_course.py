from odoo import models, fields, api, _

class Course(models.Model):
    _name = 'openacademy.course'
    _description = _('Course')
    name = fields.Char(_("Title"), required=True)
    description = fields.Text()
    responsible_user = fields.Many2one('res.users', string=_('Responsible user'))
    session_id = fields.One2many('openacademy.session', 'course', string=_('Session'), readonly=True)
    _sql_constraints = [
        ('name_diff',
         'CHECK(name != description)',
         _("The name of the course don't must be the description!")),

        ('name_uniq',
         'unique(name)',
         _('The name of the course must be unique!')),
    ]

    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        default = dict(default or {})
        qty = self.search_count([('name','like',f'Copy of {self.name}')])
        if qty == 0:
            default['name']  = f"Copy of {self.name}"
        else:
            default['name']  = f"Copy of {self.name} #{qty}"
        return super().copy(default=default)
