from odoo import fields, models

class Student(models.Model):
    _inherit = 'wb.student'

    newfield1 = fields.Char("Blood group")
    newfield2 = fields.Char("Religion")

