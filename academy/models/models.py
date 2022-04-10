from odoo import models, fields

class Teachers(models.Model):
    _name = 'academy.teachers'
    name = fields.Char('Name')
    biography = fields.Html('Biography')
    course_ids = fields.One2many('product.template', 'teacher_id', string="Courses")

class Courses(models.Model):
    # _name = 'academy.courses'
    # _inherit = ['mail.thread', 'product.template']
    # _name = 'academy.courses'
    _inherit = 'product.template'
    name = fields.Char()
    teacher_id = fields.Many2one('academy.teachers', string="Teacher")
