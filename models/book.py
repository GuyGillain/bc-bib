from odoo import fields, models
#salut les gars

class BookModel(models.Model):
    _name = "bib.book"
    _description = "Model concernant les livres"

    fields_Title = fields.Char(
        string="Titre",
        required=True,
        help="Le titre du livre",
        index="True"
    )

    fields_Screen_cover = fields.Binary(
        string="Photo de la couverture",
        required=False,
        attachment="True"
    )

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

    fields_Page_count = fields.Integer(
        string="Nombre de pages",
        required=True
    )

    fields_Bar_code = fields.Integer(
        string="code Barre",
        require="True"
    )

    fields_ISBN = fields.Char(
        string="Code ISBN",
        required=False,
        size=50
    )

    fields_Format = fields.Selection(
        string="Format",
        required=True,
        selection=[
            ('1', 'Papier'), ('2', 'Numérique')
        ]
    )

    fields_Pice = fields.Float(
        string="Prix",
        required=True
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
