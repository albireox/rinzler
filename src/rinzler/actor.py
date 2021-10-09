#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: José Sánchez-Gallego (gallegoj@uw.edu)
# @Date: 2021-10-09
# @Filename: actor.py
# @License: BSD 3-clause (http://www.opensource.org/licenses/BSD-3-Clause)

from __future__ import annotations

import os

from typing import TypeVar

from clu.legacy import LegacyActor

from rinzler import __version__


__all__ = ["RinzlerActor"]


T = TypeVar("T", bound="RinzlerActor")


class RinzlerActor(LegacyActor):
    """Rinzler actor."""

    def __init__(self, *args, **kwargs):

        schema = kwargs.pop("schema", None)
        schema = schema or os.path.join(os.path.dirname(__file__), "etc/schema.json")

        super().__init__(*args, schema=schema, **kwargs)

        self.observatory = os.environ.get("OBSERVATORY", "APO")
        self.version = __version__
