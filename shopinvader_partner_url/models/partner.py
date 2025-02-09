# Copyright 2025 KMEE (https://www.kmee.com.br).
# @author Luis Felipe Miléo <mileo@kmee.com.br>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models


class Partner(models.Model):
    _inherit = ["res.partner", "abstract.url"]
    _name = "res.partner"

    def _get_keyword_fields(self):
        return super()._get_keyword_fields() + ["ref"]
