# https://docs.brilliant.xyz/frame/building-apps/

import asyncio
from frame_sdk import Frame
from frame_sdk.display import Alignment
import datetime

async def main():
    async with Frame() as f:
        # take a photo and save to disk
        await f.display.show_text("Taking photo...", align=Alignment.MIDDLE_CENTER)
        await f.camera.save_photo("frame-test-photo.jpg")

        # display battery level, time, and date
        text_to_display = f"{await f.get_battery_level()}%\n"+datetime.datetime.now().strftime("%-I:%M %p\n%a, %B %d, %Y")
        await f.display.show_text(text_to_display, align=Alignment.MIDDLE_CENTER)

asyncio.run(main())
