from odoo import fields, models, api

class langue(models.Model) :

   @api.depends('ids_book')
   def _count_number_book(self):
      for rec in self:
         rec.count_book = len(rec.ids_book)

   def dummy(self):
      self.ensure_one()
      result = {
      "type": "ir.actions.act_window",
      "res_model": "account.move",
      "domain": [],
      "context": {"create": False},
      "name": {"Books by languages"},
      "view_mode": "tree,form"
      }
      return {}

   _name = "bib.langue"
   _description= "langue"
   _rec_name = "Fields_langue"

   Fields_langue = fields.Char(
        string="langue",
        require="True"
   )

   ids_book = fields.One2many(
      comodel_name="bib.book",
      inverse_name="langue_id",
      string="Nombre"
   )

   count_book = fields.Integer(
      string="Nombre de bouquins",
      compute=_count_number_book,
      store=True
   )

