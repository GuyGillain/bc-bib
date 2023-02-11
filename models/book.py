from odoo import fields, models
#salut les gars

class BookModel(models.Model):
    _name = "bib.book"
    _description = "Model concernant les livres"

    fields_Title = fields.Char(
        string="Titre",
        require="True",
        help="Le titre du livre",
        index="True"
    )

    fields_Screen_cover = fields.Binary(
        string="Photo de la couverture",
        require="True",
        attachment="True"
    )

    fields_Publishing_date = fields.Date(
        string="Date de publication",
        require="True"
    )

    fields_Editing = fields.Selection(
        string="Edition",
        selection=[
            ('1', '1ere'), ('2', '2eme'), ('3', '3eme'), ('4', '4eme'), ('5', 'Xeme')
        ],
        require="True",
        help="Faite le choix de l\'édition"
    )

    fields_Page_count = fields.Integer(
        string="Nombre de pages",
        require="True"
    )

    fields_Bar_code = fields.Integer(
        string="code Barrrrreeee",
        require="True"
    )

    fields_ISBN = fields.Char(
        string="Code ISBN",
        require="True",
        size=50
    )

    fields_Format = fields.Selection(
        string="Format",
        require="True",
        selection=[
            ('1', 'Papier'), ('2', 'Numérique')
        ]
    )

    fields_Pice = fields.Float(
        string="Prixxxxxx",
        require="True"
    )

    
    langue_id = fields.Many2one(
        comodel_name="bib.langue", string="langue"
    )
    

    evaluation_id = fields.One2many(
        comodel_name="bib.evaluation",
        inverse_name="ids_book",
        string="Evaluation"
    )
