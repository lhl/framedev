# https://docs.brilliant.xyz/frame/building-apps/

import asyncio
from frame_sdk import Frame
from frame_sdk.display import Alignment
import datetime

async def main():
    async with Frame() as f:
        await f.sleep()

asyncio.run(main())
