from telethon import TelegramClient, events
from telethon.tl.types import Message
import re
from dotenv import load_dotenv
import os
import downloaders

load_dotenv()

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
client = TelegramClient(
    'bot_session', api_id, api_hash,
    system_version='4.16.30-vxCUSTOM',
    device_model='POCO M4 Pro',
    app_version='1.0'
)

insta_reel_link = re.compile(r'https://?(www)?.instagram.com/reel/.*?/')

client.start()


@client.on(events.NewMessage(pattern='/insta'))
async def my_event_handler(event):
    # получение смс на которое отвечают
    message: Message = event.message
    if message.reply_to is None:
        return
    message_reply_obj = await message.get_reply_message()
    text = message_reply_obj.text
    if text is None:
        return

    # поиск ссылки на инсту
    insta_link_obj = insta_reel_link.search(text)
    if insta_link_obj is None:
        return

    link = insta_link_obj.group(0)
    await client.send_message(message.peer_id, 'Скачивание файла...')
    try:
        downloaders.download_1(link)
    except Exception as ex:
        await client.send_message(message.peer_id,
                                  'Неудачное скачивание через первый источник...')
        try:
            downloaders.download_2(link)
        except Exception as ex:
            await client.send_message(message.peer_id, 'Через второй тоже...')
            raise ex

    await client.send_message(message.peer_id, 'Отправление файла...')
    await client.send_file(message.peer_id, 'video.mp4')


client.run_until_disconnected()
