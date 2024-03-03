import asyncio
import time

async def count(i):
    print(f"count start {i}")
    await asyncio.sleep(1)
    print(f"count finish {i}")

async def main():
    tasks = [ count(i) for i in range(10) ] 
    await asyncio.gather(*tasks)
    await asyncio.gather(count(1), count(2), count(3))

if __name__ == "__main__":
    s = time.perf_counter()

    asyncio.run(main())

    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
