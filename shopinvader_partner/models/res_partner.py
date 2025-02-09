# Copyright 2025 KMEE
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResPartner(models.Model):

    _name = "res.partner"
    _inherit = ["res.partner", "seo.title.mixin", "abstract.url"]

    sequence = fields.Integer(default=10, required=True)
    description = fields.Char()
    meta_description = fields.Char()
    meta_keywords = fields.Char()
    short_description = fields.Text()
