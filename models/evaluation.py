from odoo import fields, models, api

class evaluation(models.Model):

	_name = "bib.evaluation"
	_description = "Evaluation des boukins"

	note = fields.Selection(
		string="Note",
		selection=[("1", "1/5"), ("2", "2/5"), ("3", "3/5"), ("4", "4/5"), ("5", "5/5")],
		required="True"
	)
	appreciation = fields.Char(
		string="Appréciation",
		required="False"
	)

	ids_book = fields.One2many(
		comodel_name="bib.book",
		inverse_name="evaluation_id",
		string="Nombre"
	)