import asyncio


# Simulating time delay!!
async def delay():
    await asyncio.sleep(5)
    return "Done"


async def main():
    try:
        result = await asyncio.wait_for(delay(), timeout=2)
        print(result)
    except asyncio.TimeoutError:
        print("Time limit exceeded!")


asyncio.run(main())


"""
This is where async really shines in real-world backends, because external APIs, DB queries, or sockets can hang forever if we don’t guard them.
"""
