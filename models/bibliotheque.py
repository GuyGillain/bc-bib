from odoo import fields, models

class Bibliotheque(models.Model):
	_name="bib.bibliotheque"
	_description = "bibliotheque"
	_rec_name = "name"

	name = fields.Char(
    	string="Bibliotheque",
    	required=True
	)

	shelf_id = fields.One2many(
    	comodel_name="bib.shelf",
    	inverse_name="ids_biblio",
    	string="Etagère(s)"
	)

	localisation_id = fields.Many2one(
    	comodel_name="bib.localisation",
    	string="Localisation",
    	required=True
    )
	color = fields.Integer(
    	string="Couleur",
    	default=0
    )