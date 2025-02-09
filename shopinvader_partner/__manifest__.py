# Copyright 2025 KMEE
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Shopinvader Membership",
    "summary": """
        Shopinvader membership""",
    "version": "16.0.1.0.0",
    "license": "AGPL-3",
    "author": "KMEE",
    "website": "https://github.com/shopinvader/odoo-shopinvader",
    "depends": [
        "base",
        # Shopinvader
        "shopinvader_base_url",
        "shopinvader_product_seo",  # seo.title.mixin
    ],
    "data": ["views/res_partner.xml"],
    "external_dependencies": {"python": ["extendable_pydantic>=1.2.0"]},
    "development_status": "Alpha",
}
