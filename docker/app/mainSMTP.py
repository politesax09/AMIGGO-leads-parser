import asyncio
import logging

from aiosmtpd.controller import Controller
from read_emails import handle_email
import urllib
import quopri

from chepy import Chepy

class Handler:
    async def handle_RCPT(self, server, session, envelope, address, rcpt_options):
        if not address.endswith('@macascript.com'):
            return '550 not relaying to that domain'
        envelope.rcpt_tos.append(address)
        return '250 OK'

    async def handle_DATA(self, server, session, envelope):
        f = open("./salida.txt", "wb")
        f.write(envelope.content)
        f.close()

        f = open("./salida.txt","r")
        entrada = f.read()
        salida = urllib.parse.unquote(quopri.decodestring(entrada).decode("utf-8",errors="ignore"))
        # data = urllib.parse.unquote(quopri.decodestring(str(envelope.content)).decode("utf-8",errors="ignore"))
        handle_email(salida)
        # print(data)
        # print('Message from %s' % envelope.mail_from)
        # print('Message for %s' % envelope.rcpt_tos)
        # print('Message data:\n')
        # for ln in envelope.content.decode('utf8', errors='replace').splitlines():
        #     print(f'> {ln}'.strip())
        # print()
        # print('End of message')
        # data = base64.b64decode(base64.b64encode(envelope.content))
        # data = envelope.content
        # data_decoded = quopri.decodestring(data.decode("utf-8"),header=True)
        # handle_email(data_decoded.decode("utf-8"))
        
        # Chepy(envelope.content).

        # print(f"ESTA ES LA CODIFICACION: {chardet.detect_all(envelope.content)}")
        # data = quopri.decodestring(envelope.content.decode("ascii"))
        # f.write(data)
        # f.write(message.as_string().encode("utf-8").decode("utf-8"))
        # message = message_from_bytes(envelope.content, policy=default)
        # handle_email(message.as_string())
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