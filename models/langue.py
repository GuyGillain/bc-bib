from odoo import fields, models

class langue(models.Model) :
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
      string="ID des livres"
      )

