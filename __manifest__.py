{
    "name": "Module de gestion d\'un catalogue de livres",
    "category": "Stock",
    "Version": "15.0.0",
    "author": "Delire - Gillain - Varlet",
    "website": "",
    "depends": ["base","website_sale"],
    "data":
        [
            'views/menuitems.xml',
            'views/genre.xml',
            'views/book.xml',
            'views/localisation.xml',
            'views/library.xml',
            'views/shelf.xml',
            'security/ir.model.access.csv',
            
        ],
    "installable": True,
    'images': ['static/description/icon.png'],
    "application": True,
    "sequence":-100
}
