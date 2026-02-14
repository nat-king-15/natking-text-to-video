from config import Config
from pyrogram import Client, idle
import asyncio
from logger import LOGGER
from modules.retasks import recover_incomplete_batches
from modules.scheduler import start_daily_schedulers
##Code Written By @ItsMeMaster
##Code Written By @ItsMeMaster
if __name__ == "__main__":
    bot = Client(
        "Bot",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        sleep_threshold=30,
        plugins=dict(root="plugins"),
        workers=1000,
    )
    
    # Monkeypatch send_message to handle list of chat_ids (fix for scheduler.so error)
    original_send_message = Client.send_message

    async def patched_send_message(self, chat_id, text, *args, **kwargs):
        if isinstance(chat_id, list):
            last_msg = None
            for cid in chat_id:
                try:
                    last_msg = await original_send_message(self, cid, text, *args, **kwargs)
                except Exception as e:
                    LOGGER.error(f"Failed to send message to {cid}: {e}")
            return last_msg
        return await original_send_message(self, chat_id, text, *args, **kwargs)

    Client.send_message = patched_send_message
    
    async def main():
        await bot.start()
        bot_info = await bot.get_me()
        LOGGER.info(f"<--- @{bot_info.username} Started --->")
        asyncio.create_task(recover_incomplete_batches(bot))
        asyncio.create_task(start_daily_schedulers(bot))
        LOGGER.info("Daily update schedulers started")
        await idle()
    
    asyncio.get_event_loop().run_until_complete(main())
    LOGGER.info("<--- Bot Stopped --->")
