#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from typing import Union

from pyrogram.types import InlineKeyboardButton

from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from YukkiMusic import app


def start_pannel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"],
                url=f"https://t.me/{app.username}?start=help",
            ),
            InlineKeyboardButton(
                text=_["S_B_2"], callback_data="settings_helper"
            ),
        ],
    ]
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons.append(
            [
                InlineKeyboardButton(text="❰𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎❱", url=f"https://telegra.ph/Lehar-Music-Bot-cOmmANds-06-19",
                ),
                InlineKeyboardButton(text="❰𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎❱", url=f"https://telegra.ph/Lehar-Music-Bot-cOmmANds-06-19",
                ),
            ]
        )
    else:
        if SUPPORT_CHANNEL:
            buttons.append(
                [
                    InlineKeyboardButton(text="❰𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎❱", url=f"https://telegra.ph/Lehar-Music-Bot-cOmmANds-06-19",
                    )
                ]
            )
        if SUPPORT_GROUP:
            buttons.append(
                [
                    InlineKeyboardButton(text="❰𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎❱", url=f"https://telegra.ph/Lehar-Music-Bot-cOmmANds-06-19",
                    )
                ]
            )
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_8"], callback_data="settings_back_helper"
            )
        ]
    ]
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons.append(
            [
                InlineKeyboardButton(text="❰𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎❱", url=f"https://telegra.ph/Lehar-Music-Bot-cOmmANds-06-19",
                ),
                InlineKeyboardButton(text="❰𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎❱", url=f"https://telegra.ph/Lehar-Music-Bot-cOmmANds-06-19",
                ),
            ]
        )
    else:
        if SUPPORT_CHANNEL:
            buttons.append(
                [
                    InlineKeyboardButton(text="❰𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎❱", url=f"https://telegra.ph/Lehar-Music-Bot-cOmmANds-06-19",
                    )
                ]
            )
        if SUPPORT_GROUP:
            buttons.append(
                [
                    InlineKeyboardButton(text="❰𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎❱", url=f"https://telegra.ph/Lehar-Music-Bot-cOmmANds-06-19",
                    )
                ]
            )
    buttons.append(
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ]
    )
    if GITHUB_REPO and OWNER:
        buttons.append(
            [
                InlineKeyboardButton(text=_["S_B_7"], user_id=OWNER),
                InlineKeyboardButton(text="❰𝐆𝐫𝐨𝐮𝐩❱", url=f"https://t.me/+An4yRwJGNq5mZWFl",
                ),
            ]
        )
    else:
        if GITHUB_REPO:
            buttons.append(
                [
                     InlineKeyboardButton(text="❰𝐆𝐫𝐨𝐮𝐩❱", url=f"https://t.me/+An4yRwJGNq5mZWFl",
                    ),
                ]
            )
        if OWNER:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=_["S_B_7"], user_id=OWNER
                    ),
                ]
            )
    buttons.append(
        [InlineKeyboardButton(text=_["ST_B_6"], callback_data="LG")]
    )
    return buttons
