import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AnonX import app  

photo = [
    "https://telegra.ph/file/c7b551119ea15dc365f68.jpg",
    "https://telegra.ph/file/1d19bdc70cb7ef3d60001.jpg",
    "https://telegra.ph/file/cb746616b6189e00fec71.jpg",
    "https://telegra.ph/file/71f57ec08d362b2247c6b.jpg",
    "https://telegra.ph/file/aef32840b7c2943031ad6.jpg",
    "https://telegra.ph/file/005f3268e52de060eab78.jpg",
    "https://telegra.ph/file/c04036447f2936ee4dd75.jpg",
    "https://telegra.ph/file/5cf94672c06083e36773f.jpg",
    "https://telegra.ph/file/952bac570b471a4243c8d.jpg",
    "https://telegra.ph/file/661da902ca073202ad4ba.jpg",
    "https://telegra.ph/file/89b49320d979989548003.jpg",
    "https://telegra.ph/file/01a5eab9744506eff3f83.jpg",
    "https://telegra.ph/file/eb38913e41771d1a16847.jpg",
    "https://telegra.ph/file/26f34e070431a858d31f5.jpg",
    "https://telegra.ph/file/e0c01f79896a32022c6ca.jpg",
    "https://telegra.ph/file/d424fcf4a72ec8e1a28c7.jpg",
    "https://telegra.ph/file/922e7ce9c5e0bafafeb34.jpg",
    "https://telegra.ph/file/f82d044b2f3133cec48c2.jpg",
    "https://telegra.ph/file/0f424d0824900939bb32a.jpg",
    "https://telegra.ph/file/0e84310ec975e8e6ebca9.jpg",
    "https://telegra.ph/file/1646ddc99a7c77f51b3a0.jpg",
    "https://telegra.ph/file/3c5ac8d87b622260445be.jpg",
    "https://telegra.ph/file/dfa43563bd68849a46a39.jpg",
    "https://telegra.ph/file/4506a375b415971355ff2.jpg",
    "https://telegra.ph/file/0d0cdfda3b9dac9730476.jpg",
    "https://telegra.ph/file/4d2c9229c567f9416143f.jpg",
    "https://telegra.ph/file/77ba544ccfb6bf8ba7b03.jpg",
    "https://telegra.ph/file/0387d64a44d76e0d53deb.jpg",
    "https://telegra.ph/file/9e346de01cb863b30367f.jpg",
    "https://telegra.ph/file/26a0d446102c63a1bbcca.jpg",

]


@app.on_message(filters.new_chat_members, group=3)
async def join_watcher(_, message):    
    chat = message.chat

    for members in message.new_chat_members:

            count = await app.get_chat_members_count(chat.id)

            msg = (
                f"**🥀𝐇ᴇʏ {message.from_user.mention} 𝐖ᴇʟᴄᴏᴍᴇ 𝐈ɴ 𝐀 𝐍ᴇᴡ 𝐆ʀᴏᴜᴘ🥳**\n\n"
                f"**☘️𝐂ʜᴀᴛ 𝐍ᴀᴍᴇ:** {message.chat.title}\n➖➖➖➖➖➖➖➖➖➖➖\n"
                f"**⚡️𝐂ʜᴀᴛ 𝐔.𝐍:** @{message.chat.username}\n➖➖➖➖➖➖➖➖➖➖➖\n"
                f"**💖𝐔ʀ 𝐈d:** {message.from_user.id}\n➖➖➖➖➖➖➖➖➖➖➖\n"
                f"**✨️𝐔ʀ 𝐔.𝐍:** @{message.from_user.username}\n➖➖➖➖➖➖➖➖➖➖➖\n"
                f"**🌠𝐂ᴏᴍᴘʟᴇᴛᴇᴅ {count} 𝐌ᴇᴍʙᴇʀ𝐬🎉**"
            )
            await app.send_photo(message.chat.id, photo=random.choice(photo), caption=msg, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"🥳 ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴄʜᴀᴛ 🥳", url=f"https://t.me/{app.username}?startgroup=true")]
         ]))
