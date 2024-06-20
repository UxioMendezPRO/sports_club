o# Copyright 2024 Uxio Mendez Pazos <uxio.mendez@hotmail.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
from odoo import fields, models, api


class AthleteSpots(models.Model):
    _name = "athlete.sports"
    _description = "Athletes"

    name = fields.Char(string="Name", required=True)
    surname = fields.Char(string="Surname", required=True)
    id = fields.Char(string="ID number", required=True)
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
    # category = fields.Selection(
    #     compute="_compute_category", string="Category", required=True
    # )

    # @api.depends("category")
    # def _compute_category(self):