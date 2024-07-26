from odoo import fields, models


class School(models.Model):
    _name = 'wb.school'
    _description = "This is school profile"

    name = fields.Char("Name")
    student_ids = fields.One2many('wb.student','school_id', string="Students")
    schools_ids = fields.Many2one('wb.student', string="School")


    
    School_type = fields.Selection([
        ('primary', 'Primary'),
        ('secondary', 'Secondary')
    ],"SelectType")