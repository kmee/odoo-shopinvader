# Copyright 2025 KMEE
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models


class ResPartner(models.Model):

    _name = "res.partner"
    _inherit = ["res.partner", "se.indexable.record"]
