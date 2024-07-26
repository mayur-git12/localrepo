from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Bill(models.Model):
    _inherit = 'sale.order'

    transcation = fields.Char("Transaction ID")

    @api.constrains('transcation')
    def _check_transcation_length(self):
        for record in self:
            if record.transcation and len(record.transcation) != 10:
                raise ValidationError("Transaction ID must in 10 characters")



    # offer = fields.Char("Discount")

# class Invoic(models.Model):
#     _inherit = 'sale.order.line'


#  x transcation = fields.Char("Trancation ID")
#     offer = fields.Char("Discount")