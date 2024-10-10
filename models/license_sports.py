# Copyright 2024 Uxio Mendez Pazos <uxio.mendev@gmail.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
from odoo import api, fields, models
from odoo.exceptions import UserError


class LicenseSports(models.Model):
    _name = "license.sports"
    _description = "License"

    license_number = fields.Char(string="License number", required=True)
    athlete_id = fields.Many2one("athlete.sports", required=True)
    athlete_category = fields.Selection(
        [
            ("senior", "Senior"),
            ("junior", "Junior"),
            ("cadet", "Cadet"),
            ("youth", "Youth"),
            ("beginner", "Beginner"),
        ],
        compute="_compute_athlete_category",
        string="Category",
        required=True,
        store=True,
    )
    partner_id = fields.Many2one(
        "res.partner",
        compute="_compute_partner_id",
        required=True,
    )
    sale_oder_id = fields.Many2one("sale.order")
    category_id = fields.Many2one("product.category")
    product_id = fields.Many2one("product.product")
    sale_order_id = fields.Many2one("sale.order")
    price = fields.Float(string="Price", default=44.0, required=True)
    season_id = fields.Many2one("season.sports", string="Season", required=True)

    @api.depends("partner_id")
    def _compute_partner_id(self):
        for record in self:
            if record.athlete_id and hasattr(record.athlete_id, "partner_id"):
                record.partner_id = record.athlete_id.partner_id
            else:
                record.partner_id = False

    @api.depends("category_id")
    def assign_category_id(self):
        category = self.env["product.category"].search(
            [("name", "=", "Services")], limit=1
        )
        if not category:
            category = self.env["product.category"].create(
                {
                    "name": "Services",
                }
            )
        for record in self:
            record.category_id = category

    @api.depends("product_id")
    def create_product_id(self):
        if not self.category_id:
            self.assign_category_id()
        product = self.env["product.product"].create(
            {
                "name": "License",
                "categ_id": self.category_id.id,
                "list_price": self.price,
                "standard_price": 0,
                "type": "service",
                "uom_id": self.env.ref("uom.product_uom_unit").id,
                "uom_po_id": self.env.ref("uom.product_uom_unit").id,
            }
        )
        for record in self:
            record.product_id = product

    def action_sell_license(self):
        self.ensure_one()
        self.assign_category_id()
        self.create_product_id()
        if not self.product_id.uom_id:
            raise UserError(
                "Product details are incomplete. Please ensure the product is correctly configured."
            )

        if self.sale_order_id:
            raise UserError("This athlete already has a for this season license")

        if not self.product_id or not self.product_id.uom_id:
            raise UserError("Product or UOM is not properly initialized.")

        if (
            self.partner_id
            and self.product_id
            and self.athlete_id
            and self.season
            and self.product_id.uom_id
        ):
            sale_order = self.env["sale.order"].create(
                {
                    "partner_id": self.partner_id.id,
                    "order_line": [
                        (
                            0,
                            False,
                            {
                                "product_id": self.product_id.id,
                                "name": f"{self.athlete_id.name}, {self.season.name}",
                                "product_uom_qty": 1,
                                "product_uom": self.product_id.uom_id.id,
                                "price_unit": self.product_id.list_price,
                            },
                        ),
                    ],
                }
            )
            for record in self:
                record.sale_order_id = sale_order.id

            return {
                "type": "ir.actions.act_window",
                "name": "Sales",
                "view_mode": "form",
                "res_model": "sale.order",
                "res_id": sale_order.id,
                "target": "current",
            }
        else:
            raise ValueError("One or more required fields are missing or invalid.")

    @api.depends("athlete_id")
    def _compute_athlete_category(self):
        for record in self:
            record.athlete_category = record.athlete_id.category
