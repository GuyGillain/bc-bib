from odoo import fields, models

class genre(models.Model) :
   _name = "bib.genre"
   _description= "genre"
   _rec_name = "fields_genre"
   
   fields_genre = fields.Char(
        string="genre",
        required="True"
   )

   # En utilisant le widget many2many_tags
   # On peut spécifier une couleur :)
   color = fields.Integer(
      string="Couleur du tag",
      default=0
      )
