from telethon import TelegramClient

# --- Suas credenciais do Telegram ---
API_ID = 
API_HASH = ""
PHONE = ""  # exemplo: +5511999999999

client = TelegramClient("sessao", API_ID, API_HASH)

async def main():
    async for dialog in client.iter_dialogs():
        print(f"Nome: {dialog.name} | ID: {dialog.id}")

with client:
    client.loop.run_until_complete(main())

