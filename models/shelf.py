from odoo import fields, models
#Fichier pour la localisation

class Shelf(models.Model):
    _name = "bib.shelf"
    _description = "Localisation de l'étagère dans la bibliothèque"
    _rec_name = "fields_Shelf"

    fields_Shelf = fields.Char(
        string="Numéro",
        required="True",
        help="Où se trouve l'étagère dans la bibliothèque",
        index="True"
    )

    ids_localisation = fields.Many2one(
      comodel_name="bib.localisation",
      inverse_name="shelf_id",
      string="Numéro" # caractere afficher dans la vue
   )