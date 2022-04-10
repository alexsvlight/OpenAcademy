from odoo import models, fields, api

class Teachers(models.Model):
    _name = 'academy.teachers'
    name = fields.Char('Name')
    biography = fields.Html('Biography')
    course_ids = fields.One2many('academy.courses', 'teacher_id', string="Courses")

class Courses(models.Model):

    _inherit = 'mail.thread'
    # _inherit = 'product.template'
    _name = 'academy.courses'
    # _inherit = 'product.public.category'
    name = fields.Char()
    teacher_id = fields.Many2one('academy.teachers', string="Teacher")
