# Copyright 2024 Uxio Mendez Pazos <uxio.mendev@gmail.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
from odoo import models, fields, api
from datetime import datetime


class CustomPartner(models.Model):
    _inherit = "res.partner"

    user_id = fields.Many2one(
        "res.users", default=lambda self: self.env.user, readonly=True
    )
    team_id = fields.Many2one(
        "res.users", default=lambda self: self.env.user.team_id, readonly=True
    )
    company_name = fields.Char(
        string="Company Name",
        related="company_id.name",
        readonly=True,
        default=lambda self: self.env.user.company_id.name,
    )
    id_card = fields.Char(string="ID")
    associate_number = fields.Integer(string="Associate number")
    registration_date = fields.Date(
        string="Registration date", default=datetime.now().date()
    )
    withdrawal_date = fields.Date(string="Withdrawal date")
    athlete_ids = fields.One2many("athlete.sports", "partner_id")
