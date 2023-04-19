from odoo import fields, models, api

class langue(models.Model) :

   def books_by_languages(self):
      # passage de dummy en books_by_languages
      self.ensure_one()
      result = {
      # Equivalent query SQL
      "type": "ir.actions.act_window",
      # Dans quelle table
      "res_model": "product.template",
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


