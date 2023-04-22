from odoo import fields, models

# Essais legacy

class BookModel(models.Model):
    _inherit = 'product.template'
    _description = "Model concernant les livres"

    fields_Publishing_date = fields.Date(
        string="Date de publication",
        required=True
    )

    evaluation_id = fields.One2many(
        comodel_name="bib.evaluation",
        inverse_name="ids_book",
        string="Evaluation"
    )

    genre_id = fields.Many2many(
        comodel_name="bib.genre",
        string="Genre"
    )
    auteur_ids = fields.Many2many(
        comodel_name="res.partner",
        string="Auteur"
    )

    shelf = fields.Many2one(
        comodel_name="bib.shelf",
        string="Etagère",
        required=True
    )
    
    # Booleén qui permet de filtrer uniquement les livres
    is_book = fields.Boolean(
        string="Est-ce un livre",
        default=False
    )
