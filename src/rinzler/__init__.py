#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: José Sánchez-Gallego (gallegoj@uw.edu)
# @Date: 2021-10-09
# @Filename: __init__.py
# @License: BSD 3-clause (http://www.opensource.org/licenses/BSD-3-Clause)

from sdsstools import get_config, get_logger, get_package_version


NAME = "rinzler"


config = get_config("rinzler")
log = get_logger(NAME)


__version__ = get_package_version(path=__file__, package_name=NAME)


from .actor import RinzlerActor
