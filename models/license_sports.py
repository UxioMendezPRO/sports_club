# Copyright 2024 Uxio Mendez Pazos <uxio.mendez@hotmail.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
from odoo import fields, models, api

class LicenseSports(models.Model):
  _name = "license.sports"
  _description = "License"

  season = fields.Char(string="Season", required=True)
  athlete_id = fields.Many2one("athlete.sports", string="Athlete")