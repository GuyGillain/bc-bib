from odoo import fields, models

class book(models.Model):
	_name = "book.model"
	_description = "Model concernant les livres"

	#nom_column = fields.Type()