# Copyright 2024 Uxio Mendez Pazos <uxio.mendez@hotmail.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
from datetime import datetime

from odoo import api, fields, models
from odoo.exceptions import UserError


class AthleteSpots(models.Model):
    _name = "athlete.sports"
    _description = "Athletes"

    name = fields.Char(string="Name", required=True)
    id_card = fields.Char(string="ID number", required=True)
    phone = fields.Integer(string="Phone", required=True)
    email = fields.Char(string="eMail", required=True)
    sex = fields.Selection(
        [("male", "Male"), ("female", "Female")], string="Sex", required=True
    )
    birthdate = fields.Date(string="Birthdate", required=True)
    street = fields.Char(string="Address", required=True)
    city = fields.Char(string="City")
    state_id = fields.Many2one("res.country.state", string="State")
    zip = fields.Integer(string="ZIP", required=True)
    country_id = fields.Many2one("res.country", string="Nationality", required=True)
    place_of_birth = fields.Char(string="Place of birth", required=True)
    license_number = fields.Char(string="License number")
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
    image = fields.Image(string="Image")
    license_ids = fields.One2many("license.sports", "athlete_id", string="Licenses")

    @api.depends()
    def _compute_current_date(self):
        for record in self:
            record.current_date = datetime.now().date()

    @api.depends("birthdate")
    def _compute_category(self):
        for record in self:
            age = datetime.now().year - record.birthdate.year
            if age >= 18:
                record.category = "senior"
            elif age >= 16:
                record.category = "junior"
            elif age >= 14:
                record.category = "cadet"
            elif age >= 12:
                record.category = "youth"
            else:
                record.category = "beginner"

    def action_make_partner(self):
        existing_partner = self.env["res.partner"].search(
            [("athlete_ids", "in", [self.id])], limit=1
        )
        if existing_partner:
            raise UserError("This athlete is already a partner")  
        partner_vals = {
            "name": self.name,
            "athlete_ids": [(4, self.id)],
            "phone": self.phone,
            "email": self.email,
            "street": self.street,
            "city": self.city,
            "zip": self.zip,
            "state_id": self.state_id.id if self.state_id else False,
            "country_id": (self.country_id.id if self.country_id else False),
        }
        partner = self.env["res.partner"].create(partner_vals)
        return partner
