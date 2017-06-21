# This is free and unencumbered software released into the public domain.

import asyncio

class AsyncClient:
    """An asynchronous client connection."""

    def __init__(self):
        pass

    async def answer(self):
        await asyncio.sleep(3)
        return 42

class Client(AsyncClient):
    """A synchronous client connection."""

    def __init__(self):
        super().__init__()
        self.loop = asyncio.get_event_loop()

    def wait(self, future):
        return self.loop.run_until_complete(future)

    def answer(self):
        return self.wait(super().answer())
