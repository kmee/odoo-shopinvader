# Copyright 2023 ACSONE SA/NV
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from enum import Enum

from extendable_pydantic import StrictExtendableBaseModel

from .product_attribute import ProductAttribute


class GroupType(Enum):
    """Enum for attribute group type"""

    NORMAL = "normal"
    GENERATOR = "generator"


class ProductAttributeGroup(StrictExtendableBaseModel):
    group_name: str
    fields: list[ProductAttribute]
    group_type: GroupType = GroupType.NORMAL
