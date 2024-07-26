from odoo import models, fields

class Course(models.Model):
    _name = 'wb.course'
    _description = "This is course profile"

    name = fields.Char("Name")
    student_ids = fields.Many2many('wb.student', string="Students")