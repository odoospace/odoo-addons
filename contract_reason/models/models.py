from odoo import models, fields, api

class ContractReason(models.Model):
	
    _name = 'contractreason'

    name = fields.Char(string='Caption', size=64, required=True)


class AccountAnalyticAccount(models.Model):

	_inherit = 'contract.contract'

	contractreason_ids = fields.Many2many('contractreason', string='How did he know us?', required=True)
        