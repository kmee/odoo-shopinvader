# Copyright 2025 KMEE (https://www.kmee.com.br).
# @author Luis Felipe Miléo <mileo@kmee.com.br>

from odoo.addons.shopinvader_partner.schemas.partner import Partner as BasePartner


class Partner(BasePartner, extends=True):
    url_key: str | None = None
    redirect_url_key: list[str] = []

    @classmethod
    def from_partner(cls, odoo_rec):
        obj = super().from_partner(odoo_rec)
        # ensure url is up to date
        odoo_rec._update_url_key(lang=odoo_rec.env.context.get("lang"))
        obj.url_key = odoo_rec.url_key or None
        obj.redirect_url_key = odoo_rec.redirect_url_key or []
        return obj
