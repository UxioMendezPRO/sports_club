# Copyright 2024 Uxio Mendez Pazos <uxio.mendez@hotmail.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
{
    "name": "sports_club",
    "summary": "Custom module",
    "version": "16.0.0.0.0",
    "category": "Sports",
    "website": "https://github.com/UxioMendezPRO/sports_club",
    "author": "Uxio Mendez Pazos",
    "license": "LGPL-3",
    "installable": True,
    "depends": ["base"],
    "application": True,
    "data": [
        "security/ir.model.access.csv",
        "views/sports_club_menus.xml",
        "views/athlete_sports_views.xml",
    ],
}
