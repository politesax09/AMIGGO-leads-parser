from smtpd import SMTPServer, _Address

class MainSMTPServer(SMTPServer):
    def process_message(self, peer: _Address, mailfrom: str, rcpttos: list[str], data: bytes | str, **kwargs) -> str | None:
        
        return super().process_message(peer, mailfrom, rcpttos, data, **kwargs)