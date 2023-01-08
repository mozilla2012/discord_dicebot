#!/usr/bin/env python3

import pyfiglet

from dicebot.core.register_command import register_command
from dicebot.data.types.message_context import MessageContext
from dicebot.data.types.greedy_str import GreedyStr


@register_command
async def fancy(ctx: MessageContext, text: GreedyStr) -> None:
    """Print text in a fancy style"""
    await ctx.channel.send(pyfiglet.figlet_format(text))
