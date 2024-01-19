import os
import re

from dotenv import load_dotenv
from telethon import TelegramClient, events
from telethon.tl.types import PeerChat

import seledka

load_dotenv()

if not os.path.exists('ok'):
    os.mkdir('ok')

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

main_group_id = None

chat_ids_for_forwards = [
    -1001396952381,
    -1001298257907,
    -1001162036880,
    -1001755311192,
    -1001583795567,
    -1001321956720,
    -1001678254511,
    -1001509411348,  # Алабуга политех
]


@client.on(events.NewMessage(pattern='/insta'))
async def my_event_handler(event):
    # получение смс на которое отвечают
    message = event.message
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
        seledka.download_video(seledka.get_video_url(link))
    except Exception as ex:
        await client.send_message(
            message.peer_id,
            'Неудачное скачивание через первый источник...'
        )
        raise ex

    await client.send_message(message.peer_id, 'Отправление файла...')
    await client.send_file(message.peer_id, 'video.mp4')


@client.on(
    events.NewMessage(pattern='https://?(www)?.instagram.com/reel/.*?/')
)
async def my_event_handler(event):
    if main_group_id is None:
        return

    if event.message.peer_id.chat_id != main_group_id:
        return

    # получение смс на которое отвечают
    message = event.message

    # поиск ссылки на инсту
    insta_link_obj = insta_reel_link.search(message.text)
    if insta_link_obj is None:
        return

    link = insta_link_obj.group(0)
    await client.send_message(message.peer_id, 'Скачивание файла...')
    try:
        seledka.download_video(seledka.get_video_url(link))
    except Exception as ex:
        await client.send_message(
            message.peer_id,
            'Неудачное скачивание через первый источник...'
        )
        raise ex

    await client.send_message(message.peer_id, 'Отправление файла...')
    await client.send_file(message.peer_id, 'video.mp4')


@client.on(events.NewMessage(pattern='/set_main_group'))
async def my_event_handler(event):
    global main_group_id
    message = event.message

    peer_chat: PeerChat = message.peer_id

    main_group_id = peer_chat.chat_id
    await client.send_message(message.peer_id, 'Главная группа установлена')


# если сообщение из одной из групп для пересылки
@client.on(events.NewMessage(chats=chat_ids_for_forwards))
async def my_event_handler(event):
    message = event.message
    if main_group_id is None:
        return
    await client.send_message(main_group_id, message)


client.run_until_disconnected()
