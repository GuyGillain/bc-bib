from odoo import fields, models, api

class evaluation(models.Model):

	_name = "bib.evaluation"
	_description = "Evaluation des boukins"
	_rec_name = "note"

	note = fields.Selection(
		string="Note",
		selection=[("1/5", "1/5"), ("2/5", "2/5"), ("3/5", "3/5"), ("4/5", "4/5"), ("5/5", "5/5")],
		required="True"
	)

	appreciation = fields.Char(
		string="Appréciation",
		required="False"
	)

	ids_book = fields.Many2one(
		comodel_name="bib.book",
		inverse_name="evaluation_id",
		string="Nombre"
	)