# Ajout du champ biblio à contact
class BibliographyModel(res.partner.Model):
    _name = "bibliography.model"
    _description = "Model pour le bibliographie des auteurs.es"

    fields_author = fields.Boolean(
        require="True",
        default="Non",
    )
    fields_Title = fields.Char(
        string="Bibliographie",
        require="False",
        help="Bibliographie de l'auteur.e",
        index="False"
    )