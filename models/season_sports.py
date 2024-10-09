# Copyright 2024 Uxio Mendez Pazos <uxio.mendev@gmail.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
from odoo import fields, models


class SeasonSports(models.Model):
    _name = "season.sports"
    _description = "Season"

    name = fields.Char(string="Season", required=True)
    license_ids = fields.One2many("license.sports", "season_id", string="Licenses")
