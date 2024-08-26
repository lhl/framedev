# https://docs.brilliant.xyz/frame/building-apps/

import asyncio
from frame_sdk import Frame
from frame_sdk.display import Alignment
import datetime

async def main():
    async with Frame() as f:
        # take a photo and save to disk
        await f.display.show_text("Test Unicode: 🙂今日は!", align=Alignment.MIDDLE_CENTER)

asyncio.run(main())
