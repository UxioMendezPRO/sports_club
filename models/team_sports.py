# Copyright 2024 Uxio Mendez Pazos <uxio.mendev@gmail.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
from odoo import api, fields, models


class TeamSports(models.Model):
    _name = "team.sports"
    _description = "Sports teams"

    name = fields.Char(string="Team")
    coach_id = fields.Many2one("coach.sports")
    athlete_ids = fields.Many2many("athlete.sports")
