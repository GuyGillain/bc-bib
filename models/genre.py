from odoo import fields, models

class genre(models.Model) :
   _name = "bib.genre"
   _description= "genre"
   _rec_name = "fields_genre"
   
   fields_genre = fields.Char(
        string="genre",
        required="True"
   )
   
   ids_book = fields.One2many(
      comodel_name="bib.book",
      inverse_name="genre_id",
      string="Genre" # caractere afficher dans la vue
   )

