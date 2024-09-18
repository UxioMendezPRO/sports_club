from odoo import api, fields, models


class TeamSports(models.Model):
    _name = "team.sports"
    _description = "Sports teams"

    name = fields.Char(string="Team")
    coach_id = fields.Many2one("coach.sports")
    athlete_ids = fields.Many2many("athlete.sports")
    