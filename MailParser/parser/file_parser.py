import json
from pathlib import Path
from MailParser.domain.mail import Mail
from MailParser.parser import text_parser

class FileParser:
    def parse(self, path: Path) -> Mail:
        suffix = path.suffix
        text = ""
        if suffix == '.txt' or suffix == '':
            text = path.read_text(encoding='utf-8')
        elif suffix == '.json':
            text = self.read_json(path)
        else:
            raise ValueError(f'Неподдерживаемый формат файла: {suffix}')
        return text_parser.parse(text)

    def read_json(self, path: Path) -> str:
        raw_text = path.read_text(encoding='utf-8')
        try:
            data = json.loads(raw_text)
        except json.decoder.JSONDecodeError as e:
            return raw_text
        if isinstance(data, dict):
            out = ""
            if 'from' in data:
                out += f"from: {data['from']}\n"
            else:
                out += f"от кого: {data.get('от кого', "")}\n"
            if 'to' in data:
                out += f"to: {data['to']}\n"
            else:
                out += f"кому: {data.get('кому', "")}\n"
            if 'date' in data:
                out += f"date: {data['date']}\n"
            else:
                out += f"дата: {data.get('дата', "")}\n"
            if 'subject' in data:
                out += f"subject: {data['subject']}\n"
            else:
                out += f"тема: {data.get('тема', "")}\n"
            if 'body' in data:
                out += f"body: {data['body']}\n"
            else:
                out += f"тело: {data.get('тело', "")}\n"
            return out
        return raw_text

