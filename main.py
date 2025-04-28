from telethon import TelegramClient, events

# Điền thông tin API bạn tạo ở my.telegram.org/apps
api_id = 22534620  # <-- Thay bằng API_ID của bạn
api_hash = 'b07d6de2c7647072120e274b9c71a214'  # <-- Thay bằng API_HASH của bạn

# Tên file session (giữ đăng nhập)
session_name = 'session'

client = TelegramClient(session_name, api_id, api_hash)

@client.on(events.NewMessage(pattern='/menu'))
async def menu(event):
    menu_text = """📋 *Menu tính năng*
/levea - Rời nhóm
/admin - Xem admin bot
/muteuse - Mute user
/unmuteuse - Unmute user
/checkad - Check admin nhóm
/checkgr - Check thông tin nhóm
/gemini - Gemini
/resetgemini - Reset lịch sử gemini
/dich - Dịch ngôn ngữ
/menu - Hiển thị menu này
"""
    await event.reply(menu_text)

@client.on(events.NewMessage(pattern='/levea'))
async def leave_group(event):
    if event.is_group:
        await event.reply("Tạm biệt mọi người!")
        await client.kick_participant(event.chat_id, 'me')

import requests
from telethon import events

@client.on(events.NewMessage(pattern='/gemini'))
async def gemini_ask(event):
    try:
        # Lấy nội dung người dùng gửi sau lệnh /gemini
        user_text = event.raw_text.split(' ', 1)
        if len(user_text) < 2:
            await event.reply("Bạn cần nhập nội dung sau /gemini")
            return
        question = user_text[1]

        # Gọi API
        url = f"https://dichvukey.site/apishare/hoi.php?text={question}"
        response = requests.get(url)
        if response.status_code == 200:
            answer = response.text
            await event.reply(f"**Trả lời:**\n{answer}")
        else:
            await event.reply("API lỗi, vui lòng thử lại sau.")
    except Exception as e:
        await event.reply(f"Lỗi: {str(e)}")


@client.on(events.NewMessage(pattern='/admin'))
async def admin_info(event):
    me = await client.get_me()
    await event.reply(f"Admin hiện tại: {me.first_name} (ID: {me.id})")

# Các lệnh khác bạn có thể tự thêm dựa vào mẫu trên

print("Bot đang chạy...")
client.start()
client.run_until_disconnected()
