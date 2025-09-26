import sys
print("✅ Python iniciado com versão:", sys.version)
from telethon import TelegramClient, events
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

# --- Suas credenciais do Telegram ---
API_ID = 27608582  # substitua pelo seu
API_HASH = "a62236403c55f4161ee313e2e5d9ec90"
PHONE = "+5518997048942"  # exemplo: +5511999999999

# --- Sua pasta no Google Drive ---
FOLDER_ID = "12q8Nhm6-ccm6WaOGQxTiYMe_YxevaMQ4"  # copie da URL da pasta

# --- Login no Google Drive ---
gauth = GoogleAuth()
gauth.LocalWebserverAuth()  # primeira vez vai abrir o navegador
drive = GoogleDrive(gauth)

# --- Login no Telegram ---
client = TelegramClient("sessao", API_ID, API_HASH)

@client.on(events.NewMessage(chats=-4800005168))
async def handler(event):
    if event.message.document and event.message.file.mime_type == "application/pdf":
        file_name = event.message.file.name
        path = f"./{file_name}"
        await event.message.download_media(file=path)

        # Enviar para o Google Drive
        file_drive = drive.CreateFile({'title': file_name, 'parents':[{'id': FOLDER_ID}]})
        file_drive.SetContentFile(path)
        file_drive.Upload()
        print(f"✅ Enviado: {file_name}")

        os.remove(path)

print("🔄 Iniciando...")
client.start(PHONE)  # primeira vez vai pedir o código do Telegram
client.run_until_disconnected()

