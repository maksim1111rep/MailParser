import pytest

import json
from file_parser import FileParser

@pytest.fixture
def file_parser():
    return FileParser()

class TestFileParserTxt:
    def test_txt_format(self, file_parser, tmp_path):
        test_file = tmp_path / "invoice.txt"
        test_file.write_text("From: n.lebedeva@corp.local\nSubject: Счёт на оплату\nНаправляем закрывающие документы.")
        mail = file_parser.parse(test_file)
        assert mail.sender == "n.lebedeva@corp.local"
        assert mail.subject == "Счёт на оплату"
        assert mail.body == "Направляем закрывающие документы."

    def test_no_extension_format(self, file_parser, tmp_path):
        test_file = tmp_path / "request_data"
        test_file.write_text("From: k.morozov@company.ru\nSubject: Запрос доступа\nПрошу выдать права.")
        mail = file_parser.parse(test_file)
        assert mail.sender == "k.morozov@company.ru"
        assert mail.subject == "Запрос доступа"

class TestFileParserJson:
    def test_valid_json_english(self, file_parser, tmp_path):
        test_file = tmp_path / "alert.json"
        data = {"from": "alerts@grafana.internal", "subject": "Массовый сбой", "body": "Остановлена работа системы."}
        test_file.write_text(json.dumps(data))
        mail = file_parser.parse(test_file)
        assert mail.sender == "alerts@grafana.internal"
        assert mail.subject == "Массовый сбой"
        assert mail.body == "body: Остановлена работа системы."

    def test_valid_json_russian(self, file_parser, tmp_path):
        test_file = tmp_path / "spam_alert.json"
        data = {"от кого": "a.kozlov@company.ru", "тема": "Вы выиграли iPhone!", "тело": "Срочно перейдите по ссылке."}
        test_file.write_text(json.dumps(data))
        mail = file_parser.parse(test_file)
        assert mail.sender == "a.kozlov@company.ru"
        assert mail.subject == "Вы выиграли iPhone!"
        assert mail.body == "тело: Срочно перейдите по ссылке."

    def test_invalid_json_fallback(self, file_parser, tmp_path):
        test_file = tmp_path / "corrupted.json"
        test_file.write_text("Внимание, сломанный JSON формат\nFrom: unknown@test.com")
        mail = file_parser.parse(test_file)
        assert mail.sender == "unknown@test.com"

class TestFileParserExceptions:
    def test_unsupported_format(self, file_parser, tmp_path):
        test_file = tmp_path / "data.csv"
        test_file.write_text("sender,receiver\ni.petrov@company.ru,it@corp.local")
        with pytest.raises(ValueError, match="Неподдерживаемый формат файла"):
            file_parser.parse(test_file)
