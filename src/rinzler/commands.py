#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: José Sánchez-Gallego (gallegoj@uw.edu)
# @Date: 2021-10-10
# @Filename: commands.py
# @License: BSD 3-clause (http://www.opensource.org/licenses/BSD-3-Clause)

from __future__ import annotations

import asyncio

from typing import TYPE_CHECKING

import click

from clu.parsers.click import command_parser as rinzler_commands


if TYPE_CHECKING:
    from clu import Command

    from .actor import RinzlerActor


@rinzler_commands.command()
@click.argument("TIMEOUT", type=float)
async def wait(command: Command[RinzlerActor], timeout: float):

    command.info(text=f"Starting {timeout} second timeout.")
    await asyncio.sleep(timeout)

    return command.finish(text="Timeout complete")
