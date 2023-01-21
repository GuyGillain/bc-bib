from odoo import fields, models

class langue(models.Model) :
   

      def _count_number_book(self):
         for rec in self:
            rec.count_book = len(rec.ids_book)

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
      compute=_count_number_book
      )

