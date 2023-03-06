from pyrogram import Client, filters
from plugins.Ban Tools.admin_check import admin_check
from plugins.Ban Tools.extract_user import extract_user
from plugins.Ban Tools.string_handling import extract_time


@Client.on_message(filters.command("ban"))
async def ban_user(_, message):
    is_admin = await admin_check(message)
    if not is_admin:
        return

    user_id, user_first_name = extract_user(message)

    try:
        await message.chat.kick_member(
            user_id=user_id
        )
    except Exception as error:
        await message.reply_text(
            str(error)
        )
    else:
        if str(user_id).lower().startswith("@"):
            await message.reply_text(
                "Someone else is dusting off..! "
                f"{user_first_name}"
                " Is forbidden."
            )
        else:
            await message.reply_text(
                "😂 Kᴀᴛʜᴀᴍ / Tᴀᴛᴀ / Bʏᴇ Bʏᴇ / Gᴏᴏᴅ-ᴜʜ Bᴏʏ / Gᴀʏᴀ 😂 ..! "
                f"<a href='tg://user?id={user_id}'>"
                f"{user_first_name}"
                "</a>"
                " Is Fᴏʀʙɪᴅᴅᴇɴ."
            )


@Client.on_message(filters.command("tban"))
async def temp_ban_user(_, message):
    is_admin = await admin_check(message)
    if not is_admin:
        return

    if not len(message.command) > 1:
        return

    user_id, user_first_name = extract_user(message)

    until_date_val = extract_time(message.command[1])
    if until_date_val is None:
        await message.reply_text(
            (
                "Iɴᴠᴀʟɪᴅ Tɪᴍᴇ Sᴩᴇᴄɪғɪᴇᴅ. "
                "Exᴩᴇᴄᴛᴇᴅ m, h, or d, Gᴏᴛ Iᴛ: {}"
            ).format(
                message.command[1][-1]
            )
        )
        return

    try:
        await message.chat.kick_member(
            user_id=user_id,
            until_date=until_date_val
        )
    except Exception as error:
        await message.reply_text(
            str(error)
        )
    else:
        if str(user_id).lower().startswith("@"):
            await message.reply_text(
                "Someone else is dusting off..! "
                f"{user_first_name}"
                f" Rᴇᴀsᴏɴ Fᴏʀ Bᴀɴɴᴇᴅ {message.command[1]}!"
            )
        else:
            await message.reply_text(
                "😂 Kᴀᴛʜᴀᴍ / Tᴀᴛᴀ / Bʏᴇ Bʏᴇ / Gᴏᴏᴅ-ᴜʜ Bᴏʏ / Gᴀʏᴀ 😂 ..! "
                f"<a href='tg://user?id={user_id}'>"
                "Lavane"
                "</a>"
                f" Rᴇᴀsᴏɴ Fᴏʀ Bᴀɴɴᴇᴅ {message.command[1]}!"
            )
