import asyncio
import logging

from aiosmtpd.controller import Controller
from bs4 import BeautifulSoup
from read_emails import handle_email

class Handler:
    async def handle_RCPT(self, server, session, envelope, address, rcpt_options):
        if not address.endswith('@macascript.com'):
            return '550 not relaying to that domain'
        envelope.rcpt_tos.append(address)
        return '250 OK'

    async def handle_DATA(self, server, session, envelope):
        print('Message from %s' % envelope.mail_from)
        print('Message for %s' % envelope.rcpt_tos)
        print('Message data:\n')
        for ln in envelope.content.decode('utf8', errors='replace').splitlines():
            print(f'> {ln}'.strip())
        print()
        print('End of message')
        # TODO: tratamiento del correo
        handle_email(BeautifulSoup(envelope.content.decode('utf8', errors='replace'), "html.parser"))
        # ----------------------------
        return '250 Message accepted for delivery'

async def amain(loop):
    cont = Controller(Handler(), port=8025,hostname="192.168.1.35")
    cont.start()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.create_task(amain(loop=loop))
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        print("User abort indicated")