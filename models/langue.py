from odoo import fields, models, api

class langue(models.Model) :

   @api.depends('ids_book') # appeler par la vue, sert a afficher le petit chiffre
   def _count_number_book(self): #appeler dans la vue, smart bouton pour connaitre le nombre de livre
      for rec in self:
         rec.count_book = len(rec.ids_book)

   def books_by_languages(self):
      # passage de dummy en books_by_languages
      self.ensure_one()
      result = {
      # Equivalent query SQL
      "type": "ir.actions.act_window",
      # Dans quelle table
      "res_model": "bib.book",
      # Clause WHERE
      "domain": [("langue_id", "=", self.id)],

      "name": {"Books by languages"},
      "view_mode": "tree,form"
      }
      return result

   _name = "bib.langue"
   _description= "langue"
   _rec_name = "Fields_langue"

   Fields_langue = fields.Char(
        string="langue",
        required="True"
   )



   count_book = fields.Integer(
      string="Nombre de bouquins",
      compute=_count_number_book,
      store=True
   )

