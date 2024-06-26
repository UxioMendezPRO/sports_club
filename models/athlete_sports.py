# Copyright 2024 Uxio Mendez Pazos <uxio.mendez@hotmail.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
from odoo import fields, models, api
from datetime import datetime


class AthleteSpots(models.Model):
    _name = "athlete.sports"
    _description = "Athletes"

    name = fields.Char(string="Name", required=True)
    id_card = fields.Char(string="ID number", required=True)
    phone = fields.Integer(string="Phone", required=True)
    email = fields.Char(string="Email", required=True)
    sex = fields.Selection(
        [("male", "Male"), ("female", "Female")], string="Sex", required=True
    )
    birthdate = fields.Date(string="Birthdate", required=True)
    address = fields.Char(string="Address", required=True)
    postal_code = fields.Integer(string="Postal code", required=True)
    nationality = fields.Char(string="Nationality", required=True)
    place_of_birth = fields.Char(string="Place of birth", required=True)
    license_number = fields.Char(string="License number")
    is_partner = fields.Boolean(string="Partner")
    partner_id = fields.Many2one("res.partner", string="Partner name")
    category = fields.Selection(
        [
            ("senior", "Senior"),
            ("junior", "Junior"),
            ("cadet", "Cadet"),
            ("youth", "Youth"),
            ("beginner", "Beginner"),
        ],
        compute="_compute_category",
        string="Category",
    )
    current_date = fields.Date(compute="_compute_current_date")
    coach_id = fields.Many2one("coach.sports", string="Coach")

    @api.depends()
    def _compute_current_date(self):
        for record in self:
            record.current_date = datetime.now().date()

    @api.depends("category")
    def _compute_category(self):
        for record in self:
            if datetime.now().year - record.birthdate.year > 18:
                record.category = "senior"
            elif datetime.now().year - record.birthdate.year < 18:
                record.category = "junior"
            elif datetime.now().year - record.birthdate.year < 16:
                record.category = "cadet"
            elif datetime.now().year - record.birthdate.year < 14:
                record.category = "youth"
            elif datetime.now().year - record.birthdate.year < 12:
                record.category = "beginner"

    @api.onchange("is_partner")
    def _onchange_is_partner(self):
        if self.is_partner:
            partner = self.env["res.partner"].create(
                {
                    "name": self.name,
                    "id": self.id,
                    "phone": self.phone,
                    "email": self.email,
                    "address": self.address,
                }
            )
