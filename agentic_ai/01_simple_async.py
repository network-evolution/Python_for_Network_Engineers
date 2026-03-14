import asyncio
import datetime

def now():
    return datetime.datetime.now().strftime("%H:%M:%S")

async def sleep_async_func(seconds: int):
    """A simple function that sleeps for a given number of seconds."""
    print(f"{now()} Sleeping for {seconds} seconds...")
    await asyncio.sleep(seconds)
    print(f"{now()} Slept for {seconds} seconds")
    return f"{now()} Slept for {seconds} seconds"

# await sleep_async_func(2)

async def main():
    await asyncio.gather(
        sleep_async_func(4),
        sleep_async_func(2),
        sleep_async_func(3)
    )
    
asyncio.run(main())