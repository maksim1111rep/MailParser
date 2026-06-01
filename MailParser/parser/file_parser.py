import json
from pathlib import Path
from MailParser.domain.mail import Mail
from MailParser.parser import text_parser
from MailParser.logger_configuration import logger
class FileParser:
    def parse(self, path: Path) -> Mail:
        suffix = path.suffix
        text = ""
        logger.info(f"Формат файла {suffix if suffix else 'без расширения'}")
        if suffix == '.txt' or suffix == '':
            text = path.read_text(encoding='utf-8')
            logger.info(f"Файл {path.name} в текстовом формате обработан")
        elif suffix == '.json':
            text = self.read_json(path)
            logger.info(f"Файл {path.name} в JSON формате обработан")
        else:
            logger.error(f"Встречен неподдерживаемый формат файла {suffix}")
            raise ValueError(f'Неподдерживаемый формат файла {suffix}')
        logger.info("Файл отправлен в текстовый парсер")
        return text_parser.parse(text)

    def read_json(self, path: Path) -> str:
        raw_text = path.read_text(encoding='utf-8')
        try:
            data = json.loads(raw_text)
        except json.decoder.JSONDecodeError as e:
            logger.warning(f"Файл {path.name} не является корректным JSON")
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

