from odoo import models, fields,api


class Mybill(models.Model):
    _inherit = 'account.move'
    transaction = fields.Char("Transaction ID")
 
    
    



    @api.onchange('transaction')
    def _onchange_transaction(self):
        if self.transaction:
            if len(self.transaction) != 10 or not self.transaction.startswith('12'):
                self.transaction = ''
                return {
                    'warning': {
                        'title': "Invalid Transaction ID",
                        'message': "Transaction ID must be exactly 10 digit, start with '1' '2'."
                    }
                }
class Myinvoice(models.Model):
    _inherit = 'account.move.line'

    prefer = fields.Char("Customer Reference")





            

