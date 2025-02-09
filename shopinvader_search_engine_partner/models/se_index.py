# Copyright 2025 KMEE SA/NV
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import _, api, fields, models
from odoo.exceptions import ValidationError

from ..tools.partner_serializer import PartnerShopinvaderSerializer


class SeIndex(models.Model):

    _inherit = "se.index"

    serializer_type = fields.Selection(
        selection_add=[
            ("shopinvader_partner_exports", "Shopinvader Partner"),
        ],
        ondelete={
            "shopinvader_partner_exports": "cascade",
        },
    )

    @api.constrains("model_id", "serializer_type")
    def _check_model(self):
        partner_model = self.env["ir.model"].search(
            [("model", "=", "res.partner")], limit=1
        )
        for se_index in self:
            if (
                se_index.serializer_type == "shopinvader_partner_exports"
                and se_index.model_id != partner_model
            ):
                raise ValidationError(_("'Serializer Type' must match 'Model'"))

    def _get_serializer(self):
        self.ensure_one()
        if self.serializer_type == "shopinvader_partner_exports":
            return PartnerShopinvaderSerializer()
        else:
            return super()._get_serializer()
