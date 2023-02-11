from odoo import fields, models, api

class genre(models.Model) :
   _name = "bib.genre"
   _description= "genre"
   _rec_name = "Fields_genre"
   
   Fields_genre = fields.Char(
        string="genre",
        require="True"
   )
   
   ids_genre = fields.One2many(
      comodel_name="bib.book",
      inverse_name="genre_id",
      string="Genre" # caractere afficher dans la vue
   )

