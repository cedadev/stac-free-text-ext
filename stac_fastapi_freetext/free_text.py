# encoding: utf-8
"""Free-text Extension"""

__author__ = 'Richard Smith'
__date__ = '05 Aug 2021'
__copyright__ = 'Copyright 2018 United Kingdom Research and Innovation'
__license__ = 'BSD - see LICENSE file in top-level package directory'
__contact__ = 'richard.d.smith@stfc.ac.uk'

from typing import List, Optional

import attr
from fastapi import FastAPI
from pydantic import BaseModel

from stac_fastapi.types.extension import ApiExtension
from stac_fastapi.types.search import APIRequest

CONFORMANCE_CLASSES = [
    'https://api.stacspec.org/v1.0.0-beta.2/item-search#free-text-search'
]


@attr.s
class FreeTextExtensionGetRequest(APIRequest):
    """Free text extension GET request model."""
    q: Optional[str] = attr.ib(default=None)


class FreeTextExtensionPostRequest(BaseModel):
    """Free text extension POST request model."""
    q: Optional[str] = None


@attr.s
class FreeTextExtension(ApiExtension):
    """Free-text search extension


    The Free-text extension adds functionality to the `/search` endpoint
    and allows the caller perform free-text queries against item properties.

    https://github.com/cedadev/stac-freetext-search

    Attributes:
        conformance_classes (list): Defines the list of conformance classes
                                    for the extension.
    """

    conformance_classes: List[str] = attr.ib(
        default=CONFORMANCE_CLASSES
    )

    GET = FreeTextExtensionGetRequest
    POST = FreeTextExtensionPostRequest

    def register(self, app: FastAPI) -> None:
        ...
