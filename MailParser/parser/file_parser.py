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
            text = ""
            try:
                text = json.loads(path.read_text(encoding='utf-8'))
            except json.decoder.JSONDecodeError as e:
                raise ValueError("Не получилось чтение из JSON файла") from e
        else:
            raise ValueError(f'Неподдерживаемый формат файла: {suffix}')
        return text_parser.parse(text)