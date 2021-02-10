#    Projects, Some Open Source Projects/Plugins of Jayant Kageri
#    Copyright (C) 2020 - 2021 Jayant Kageri
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.


# PLUGIN TO CHECK USER IS BANNED IN SOME POPULAR FED OR NOT

import re

import html

import asyncio
import datetime

from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon import *

from . import *

cbot = '@MissRose_Bot'
rbot = '@rSophieBot'

conversation_hack = dict()


@borg.on(admin_cmd(outgoing=True, pattern="ginfo (.*)"))
@borg.on(sudo_cmd(outgoing=True, pattern="ginfo (.*)", allow_sudo=True))
async def _(event):
  ok = await event.edit("Searching...")
  # Anonymous Army
 
   async with borg.conversation(cbot) as conv:
     await conv.send_message("/start")
     await conv.get_response()
     sysarg = event.pattern_match.group(1)
     await conv.send_message(f"/fbanstat {sysarg} 21029270-28da-425c-9a4a-8f0514624ef0")
     msg = await conv.get_response()
     anony = await msg.text
     
  except YouBlockedUserError

# CAS

casurl = f"https://api.cas.chat/check?user_id={sysarg}"

r = request.get(casurl)
json = r.json
if json['ok']
cas = return f'''
- <b>True</b>
- <b>Offenses:</b> {json["result"]["offenses"]}
'''

# Spam Protector

spurl = f'https://api.intellivoid.net/spamprotection/v1/lookup?query={sysarg}'
r = request.get(spurl)
json = r.json
if json['success']:
  text = ''
  if json['results']['private_telegram_id']:
    text += f'- <b>PTID:</b> <code>'
    +
    json['results']['private_telegram_id'] + "</code>\n"
    if json['results']['attributes']['is_potential_spammer']:
    text += '- <b>Potential Spammer:</b> Yes\n'
    if json['results']['language_prediction']['language']:

            text += f'''\n- <b>Language Prediction:</b> {json["results"]["language_prediction"]["language"]}

- <b>Language Prediction Probability:</b> {json["results"]["language_prediction"]["probability"]}'''
    if json['results']['attributes']['is_blacklisted']:

            text += f'''\n- <b>Blacklist Flag:</b> {json["results"]["attributes"]["blacklist_flag"]}

- <b>Blacklist Reason:</b> {json["results"]["attributes"]["blacklist_reason"]}'''

    if json['results']['attributes']['original_private_id']:
            text += f'\n- <b>Original Private ID:</b> {json["results"]["attributes"]["original_private_id"]}'

spamprotection = text

# Dahua Engine
async with borg.conversation(rbot) as conv:
 await conv.send_message("/start")
 await conv.get_response()
 sysarg = event.pattern_match.group(1)
 await conv.send_message(f"/fcheck {sysarg} 845d33d3-0961-4e44-b4b5-4c57775fbdac")
 msg = await conv.get_response()
 dahuaengine = await msg.text

except YouBlockedUserError

# SpamWatch

import spamwatch

SW_API = os.environ.get('SW_API')
client = spamwatch.Client(SW_API)
swban = client.get_ban({sysarg})

LAST_MSG = f"""
USER : {sysarg}

@TheAnonymoysArmy : {anony}

@SpamWatch {swban}

CAS : {cas}

Spam Protection : {spamprotection}

Dahua Engine : {dahuaengine}
"""
await ok.edit(LAST_MSG)
