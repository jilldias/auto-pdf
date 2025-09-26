from telethon import TelegramClient

# --- Suas credenciais do Telegram ---
API_ID = 27608582
API_HASH = "a62236403c55f4161ee313e2e5d9ec90"
PHONE = "+5518997048942"  # exemplo: +5511999999999

client = TelegramClient("sessao", API_ID, API_HASH)

async def main():
    async for dialog in client.iter_dialogs():
        print(f"Nome: {dialog.name} | ID: {dialog.id}")

with client:
    client.loop.run_until_complete(main())
