from odoo import fields, models
#salut les gars
# Essais legacy

class BookModel(models.Model):
    _inherit = 'product.template'
    _description = "Model concernant les livres"

    fields_Publishing_date = fields.Date(
        string="Date de publication",
        required=True
    )

    fields_Editing = fields.Selection(
        string="Edition",
        selection=[
            ('1', '1ere'), ('2', '2eme'), ('3', '3eme'), ('4', '4eme'), ('5', 'Xeme')
        ],
        required=True,
        help="Faite le choix de l\'édition"
    )

    fields_Format = fields.Selection(
        string="Format",
        required=True,
        selection=[
            ('1', 'Papier'), ('2', 'Numérique')
        ]
    )


    langue_id = fields.Many2one(
        comodel_name="res.lang",
        domain=['|', ('active', '=', False), ("active", "=", True)],
        string="langue",
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
