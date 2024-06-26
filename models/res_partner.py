# Copyright 2024 Uxio Mendez Pazos <uxio.mendez@hotmail.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
from odoo import fields, models, api


class ResPartner(models.Model):  # pq falla estooo????
    _inherit = "res.partner"

    _name = "res.partner"
    _description = "res.partner inheritance"

    id = fields.Char(string="ID")
    associate_number = fields.Integer(string="Associate number")
    registration_date = fields.Date(string="Registration date")
    withdrawal_date = fields.Date(string="Withdrawal date")
