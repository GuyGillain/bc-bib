from odoo import fields, models
#Fichier pour la localisation

class Shelf(models.Model):
    _name = "bib.shelf"
    _description = "Localisation de l'étagère dans la bibliothèque"
    _rec_name = "Numéro"

    Numéro = fields.Char(
        string="Numéro",
        required="True",
        help="Où se trouve l'étagère dans la bibliothèque",
        index="True"
    )
    color = fields.Integer(
        string="Couleur",
        default=0
        )

    ids_biblio = fields.Many2one(
      comodel_name="bib.bibliotheque",
      string="Bibliothèque",
      required=True
    )

    books = fields.One2many(
        comodel_name="bib.book",
        inverse_name="shelf",
        string="Livres"
    )