import asyncio
from frame_sdk import Frame
from frame_sdk.display import Alignment
import datetime

async def main():
    async with Frame() as f:
        # Generate the filename with the current date and time
        current_time = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        filename = f"photo-{current_time}.jpg"
        
        # Take a photo and save to disk
        await f.display.show_text("Taking photo...", align=Alignment.MIDDLE_CENTER)
        await f.camera.save_photo(filename)
        await f.display.show_text("DONE", align=Alignment.MIDDLE_CENTER)

# Run the main function
asyncio.run(main())
