from odoo import fields, models

class langue(models.Model) :
     _name = "bib.langue"
     _description= "langue"

     Fields_langue = fields.Char(

        string="langue",
        require="True"

     )