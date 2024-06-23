# Copyright 2024 Uxio Mendez Pazos <uxio.mendez@hotmail.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
from odoo import fields, models, api

class CoachSports(models.Model):
  _name = "coach.sports"
  _description = "coach"

  athletes_ids = fields.One2many("athlete.sports", "coach_id")
  