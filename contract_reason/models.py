# -*- coding: utf-8 -*-

from openerp import models, fields, api

class ContractReason(models.Model):
	
    _name = 'contractreason'

    name = fields.Char(string='Caption', size=64, required=True)


class AccountAnalyticAccount(models.Model):

	_inherit = 'account.analytic.account'

	contractreason_ids = fields.Many2many('contractreason', string='How did he know us?', required=True)
        