from logic import *
import asyncio

async def main():
    await game()

    return

if __name__ == "__web__":
    asyncio.run(main())
