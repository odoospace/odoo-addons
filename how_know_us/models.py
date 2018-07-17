# -*- coding: utf-8 -*-

from openerp import models, fields, api

class how_know_us(models.Model):
	
    _name = 'how_know_us.how_know_us'
    _rec_name = 'name'

    name = fields.Char(string='Caption', size=64, required=True)


class AccountAnalyticAccount(models.Model):

	_inherit = 'account.analytic.account'

	howknowus_ids = fields.Many2many('how_know_us.how_know_us', string='How did he know us?', required=True)
        