import os
import sys
import asyncio
from pyrogram import filters
from pyrogram.types import Message
from bot import Bot
from database.database import add_1, add_2, get_forcesub_channels
from config import OWNER_ID


async def restart_bot(client: Bot, message: Message):
    await message.reply_text("🔄 Bot is restarting...")
    await asyncio.sleep(1)
    os.execv(sys.executable, ['python'] + sys.argv)


async def check_membership(client: Bot, user_id: int, channel_id: int) -> bool:
    try:
        member = await client.get_chat_member(channel_id, user_id)
        return member.status not in ["left", "kicked"]
    except Exception:
        return False


@Bot.on_message(filters.command("forcesub1"))
async def force_subscribe_command_1(client: Bot, message: Message):
    user_id = message.from_user.id

    if user_id != OWNER_ID:
        await message.reply_text("❌ Only the Owner can use this command!")
        return

    if len(message.command) != 2:
        await message.reply_text("<b>Incorrect format.</b>\n\nUse: <code>/forcesub1 {channel_id}</code>")
        return

    try:
        channel_id = int(message.command[1])
    except ValueError:
        await message.reply_text("❌ Invalid channel ID. Please check again!")
        return

    await add_1(channel_id)
    await message.reply_text(f"✅ Channel ID <code>{channel_id}</code> has been set for Forcesub 1.")
    await restart_bot(client, message)


@Bot.on_message(filters.command("forcesub2"))
async def force_subscribe_command_2(client: Bot, message: Message):
    user_id = message.from_user.id

    if user_id != OWNER_ID:
        await message.reply_text("❌ Only the Owner can use this command!")
        return

    if len(message.command) != 2:
        await message.reply_text("<b>Incorrect format.</b>\n\nUse: <code>/forcesub2 {channel_id}</code>")
        return

    try:
        channel_id = int(message.command[1])
    except ValueError:
        await message.reply_text("❌ Invalid channel ID. Please check again!")
        return

    await add_2(channel_id)
    await message.reply_text(f"✅ Channel ID <code>{channel_id}</code> has been set for Forcesub 2.")
    await restart_bot(client, message)


@Bot.on_message(filters.command("forcesub"))
async def force_subscribe(client: Bot, message: Message):
    user_id = message.from_user.id
    forcesub_channels = await get_forcesub_channels() or []

    if not forcesub_channels:
        await message.reply_text("⚠️ No Forcesub channels have been set.")
        return

    not_joined_channels = []
    for channel_id in forcesub_channels:
        if not await check_membership(client, user_id, channel_id):
            not_joined_channels.append(channel_id)

    if not not_joined_channels:
        await message.reply_text("🎉 You have joined all required channels. Thank you!")
        return

    channels_links = "\n".join(
        [f"• <a href='https://t.me/{await client.get_chat(channel_id).username}'>{await client.get_chat(channel_id).title}</a>"
         for channel_id in not_joined_channels]
    )

    await message.reply_text(
        f"🚫 To use this bot, please join the required channels:\n\n{channels_links}",
        disable_web_page_preview=True
    )


@Bot.on_message(filters.command("start"))
async def start(client: Bot, message: Message):
    user_id = message.from_user.id
    forcesub_channels = await get_forcesub_channels() or []

    not_joined_channels = []
    for channel_id in forcesub_channels:
        if not await check_membership(client, user_id, channel_id):
            not_joined_channels.append(channel_id)

    if not not_joined_channels:
        await message.reply_text(
            "✅ Welcome back! You have access to the bot.",
            disable_web_page_preview=True
        )
        # Add file-sharing logic here (e.g., display files or options)
        await message.reply_document(
            "path/to/file.txt",  # Replace with your file path
            caption="Here is your requested file."
        )
    else:
        channels_links = "\n".join(
            [f"• <a href='https://t.me/{await client.get_chat(channel_id).username}'>{await client.get_chat(channel_id).title}</a>"
             for channel_id in not_joined_channels]
        )
        await message.reply_text(
            f"⚠️ You need to join the following channels before accessing the bot:\n\n{channels_links}",
            disable_web_page_preview=True
        )
        
