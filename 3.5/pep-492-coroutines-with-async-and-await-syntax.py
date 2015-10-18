#! /usr/bin/env python
# -*- coding: utf-8 -*-
import asyncio


async def http_get(domain, port):
    reader, writer = await asyncio.open_connection(domain, port)
    writer.write(b'\r\n'.join([
        b'GET / HTTP/1.1',
        b'Host: %b' % domain.encode(),
        b'Connection: close',
        b'', b'',
    ]))

    async for line in reader:
        print('>>>', line)

    writer.close()


loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(http_get('127.0.0.1', 8000))
finally:
    loop.close()
