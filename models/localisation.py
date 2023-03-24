from odoo import fields, models
#Fichier pour la localisation

class Localisation(models.Model):
    _name = "bib.localisation"
    _description = "Localisation de la bibliothèque"
    _rec_name = "fields_Location"

    #Voir les autres models, flemme de réécrire... :)
    @api.depends("ids_biblio.counted")
    def _count_number_book(self):
        for biblio in self:
            biblio.counted = sum(record.counted for record in biblio.ids_biblio)


    fields_Location = fields.Char(
        string="Localisation",
        required="True",
        help="Où se trouve la bibliothèque",
        index="True"
    )

    ids_biblio = fields.One2many(
        comodel_name="bib.bibliotheque",
        inverse_name="localisation_id",
        string="Bibliotheque"
    )

    #champ calculé auto
    counted = fields.Integer(
        string="Nombre de livre à cet emplacement",
        compute=_count_number_book,
        store=True
        )