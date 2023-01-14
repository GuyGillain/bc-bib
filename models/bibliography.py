# Ajout du champ biblio à contact
class BibliographyModel(res.partner):
    _name = "bib.bibliography"
    _description = "Model pour le bibliographie des auteurs.es"

    fields_author = fields.Boolean(
        require="True",
        default="False"
    )

    fields_Title = fields.Text(
        string="Bibliographie",
        require="False",
        help="Bibliographie de l'auteur.e",
        index="False"
    )