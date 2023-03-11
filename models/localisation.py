from odoo import fields, models
#Fichier pour la localisation

class Localisation(models.Model):
    _name = "bib.localisation"
    _description = "Localisation de la bibliothèque"
    _rec_name = "fields_Location"

    fields_Location = fields.Char(
        string="Localisation",
        required="True",
        help="Où se trouve la bibliothèque",
        index="True"
    )
