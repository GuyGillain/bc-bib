from odoo import fields, models, api

class Bibliotheque(models.Model):
	_name="bib.bibliotheque"
	_description = "bibliotheque"
	_rec_name = "name"

	# On va rechercher le champ "counted" de l'autre model "bib.shelf" en passant par le One2many
	@api.depends("shelf_id.counted")
	def _count_number_book(self):
		for etagere in self:
			etagere.counted = sum(record.counted for record in etagere.shelf_id)



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

    # Champ calculé automatiquement
	counted = fields.Integer(
    	string="Nombre de livre dans la bibliothèque",
    	compute=_count_number_book,
    	store=True
    )