from telethon import TelegramClient, events, sync, utils
from cryptg import *
import time

api_id = API_ID
api_hash = API_HASH

mensaje={}
download= MAIN_CHANNEL_ID

client = TelegramClient('anon', api_id, api_hash).start()

print("Bot working!")
@client.on(events.NewMessage(chats=[download]))
async def my_event_handler(event):
    messages= await client.get_dialogs()
    chat_from = event.chat if event.chat else (await event.get_chat())
    chat_title = utils.get_display_name(chat_from)

    if event.media==None:
        try:
            if event.message.message!='Path uploaded!' and event.message.message!='An error has ocurred' and event.message.message!='Downloading file..':
                if event.message.message=="alive?":
                    await client.send_message(download, f"I'm ON!")
                else:
                    mensaje["path"]=event.message.message
                    await client.send_message(download, f"{'Path uploaded!'}")
        except Exception as e:
            await client.send_message(download, f"{'An error has ocurred'}")
            print(e)
    if event.media:
        try:
            foto=event.media
            await client.download_media(foto, f'{mensaje["path"]}')
            client.send_message(download, f"{'Downloading file..'}")
        except Exception as e:
            client.send_message(download, f"{'An error has ocurred'}")
            print(e)
client.start()
client.run_until_disconnected()

