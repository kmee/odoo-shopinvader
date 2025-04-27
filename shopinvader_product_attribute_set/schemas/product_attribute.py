# Copyright 2023 ACSONE SA/NV
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from __future__ import annotations

from datetime import date, datetime
from enum import Enum

import pydantic
from extendable_pydantic import StrictExtendableBaseModel
from shapely.geometry import Point, Polygon  # Importando suporte para geometria

from odoo.addons.product.models.product_product import ProductProduct

from ..models.attribute_attribute import AttributeAttribute


class ProductAttributeType(Enum):
    """Enum for product attribute type"""

    char = "char"
    text = "text"
    select = "select"
    multiselect = "multiselect"
    boolean = "boolean"
    integer = "integer"
    float = "float"
    date = "date"
    datetime = "datetime"
    binary = "binary"
    geo_point = "geo_point"
    geo_polygon = "geo_polygon"

    @classmethod
    def safe_get(cls, value: str) -> ProductAttributeType:
        """Retorna um tipo válido ou um valor padrão caso o recebido seja inválido."""
        try:
            return cls(value)
        except ValueError:
            return cls.char  # Define um valor padrão seguro


class ProductAttribute(StrictExtendableBaseModel):
    name: str
    key: str
    # Use strict types para evitar conversões implícitas de valores
    value: pydantic.StrictInt | pydantic.StrictStr | pydantic.StrictFloat | bool | list[
        str
    ] | str
    type: ProductAttributeType
    is_filterable: bool = False

    @classmethod
    def _get_value_for_attribute(
        cls,
        product: ProductProduct,
        attr: AttributeAttribute,
        string_mode: bool = False,
    ) -> str | bool | int | float | list[str]:
        value = product[attr.name]

        if isinstance(value, Point):
            return f"{value.y}, {value.x}"
        elif isinstance(value, Polygon):
            coords = []
            for x, y in value.exterior.coords:
                coords.append(f"{y}, {x}")
            return coords

        if attr.attribute_type == "select":
            return value.display_name or ""
        elif attr.attribute_type == "multiselect":
            return value.mapped("display_name")
        elif string_mode and attr.attribute_type == "boolean":
            return "true" if value else "false"
        elif isinstance(value, (date, datetime)):
            return value.isoformat() or ""
        elif string_mode or attr.attribute_type in ("char", "text"):
            return "%s" % (value or "")
        return value or ""

    @classmethod
    def from_product_attribute(
        cls, product: ProductProduct, attribute: AttributeAttribute
    ) -> ProductAttribute:
        return cls.model_construct(
            name=attribute.field_description,
            key=attribute.export_name,
            value=cls._get_value_for_attribute(product, attribute, string_mode=True),
            type=ProductAttributeType.safe_get(
                attribute.attribute_type or attribute.ttype
            ),
            is_filterable=attribute.attribute_usage == "filter",
        )
