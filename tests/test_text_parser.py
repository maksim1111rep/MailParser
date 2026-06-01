import pytest
from MailParser.parser.text_parser import parse

class TestTextParserSender:
    def test_english_from(self):
        mail = parse("From: a.fedorova@company.ru")
        assert mail.sender == "a.fedorova@company.ru"
        
    def test_russian_from(self):
        mail = parse("От кого: i.petrov@company.ru")
        assert mail.sender == "i.petrov@company.ru"

class TestTextParserReceiver:
    def test_english_to(self):
        mail = parse("To: it-support@corp.local")
        assert mail.receiver == "it-support@corp.local"
        
    def test_russian_to(self):
        mail = parse("Кому: helpdesk@company.ru")
        assert mail.receiver == "helpdesk@company.ru"

class TestTextParserDate:
    def test_english_date(self):
        mail = parse("Date: 27.12.2023 15:17")
        assert mail.date == "27.12.2023 15:17"
        
    def test_russian_date(self):
        mail = parse("Дата: 25.10.2023 14:15")
        assert mail.date == "25.10.2023 14:15"

class TestTextParserSubject:
    def test_english_subject(self):
        mail = parse("Subject: Критический инцидент")
        assert mail.subject == "Критический инцидент"
        
    def test_russian_subject(self):
        mail = parse("Тема: Заявка на отпуск")
        assert mail.subject == "Заявка на отпуск"

class TestTextParserBody:
    def test_body_content(self):
        mail = parse("Subject: Уточнение по оплате\n\nНаправляем счёт и акт.\nПросим подтвердить оплату.")
        assert mail.body == "Направляем счёт и акт.\nПросим подтвердить оплату."
