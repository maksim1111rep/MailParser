from dataclasses import dataclass

@dataclass
class Mail:
    sender: str
    receiver: str
    date: str
    subject: str
    body: str
    path: str
    format: str