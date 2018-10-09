# This is free and unencumbered software released into the public domain.

import asyncio
import grpc

class AsyncClient:
    """An asynchronous client connection."""

    def __init__(self):
        self.conn = None

    async def connect(self, **kwargs):
        return self.conn

    async def disconnect(self):
        if self.conn is not None:
            await self.conn.close()
            self.conn = None

    async def execute(self, query_text):
        assert self.conn is not None
        return await self.conn.fetch(query_text)

class Client(AsyncClient):
    """A synchronous client connection."""

    def __init__(self, **kwargs):
        super().__init__()
        self.loop = asyncio.get_event_loop()
        self.connect(**kwargs)

    def wait(self, future):
        return self.loop.run_until_complete(future)

    def connect(self, **kwargs):
        return self.wait(super().connect(**kwargs))

    def disconnect(self):
        return self.wait(super().disconnect())

    def execute(self, query_text):
        return self.wait(super().execute(query_text))
