from odoo import fields, models, api
#Fichier pour la localisation

class Shelf(models.Model):
    _name = "bib.shelf"
    _description = "Localisation de l'étagère dans la bibliothèque"
    _rec_name = "Numéro"


    #Fonction crée pour remplir le champ "counted" automatiquement
    @api.depends("books") #Décorateur, indique que l'on a besoin du champ 'books''
    def _count_number_book(self):
        for livre in self:
            self.counted = len(self.books)



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


    # Ce champ est calculé automatiquement
    # on utilise la fonction de la class
    # crée plus haut pour automatiquement
    # le remplir :) 
    counted = fields.Integer(
        string="Nombre de livre(s) présent",
        compute=_count_number_book,
        store=True
    )