import pytest

from MailParser.classifier import Classifier
from MailParser.domain.mail import Mail
from MailParser.domain.category import Category


@pytest.fixture
def classifier():
    return Classifier()


class TestCategoryKeywords:
    def test_spam(self, classifier):
        mail = Mail(
            sender="unknown@test.com",
            subject="Привет",
            body="Срочно перейдите по ссылке и введите данные, чтобы ваш аккаунт не немедленно заблокировали. К тому же вы стали победителем розыгрыша!"
        )
        assert classifier.classify(mail) == Category.SPAM

    def test_incidents(self, classifier):
        mail = Mail(
            sender="user@corp.local",
            subject="Проблема",
            body="После обновления у меня совсем сервис перестал работать, часто появляется ошибка и потом всё падает. Пишет что сервер недоступен, произошел сбой."
        )
        assert classifier.classify(mail) == Category.INCIDENTS

    def test_request(self, classifier):
        mail = Mail(
            sender="manager@company.ru",
            subject="Заявка",
            body="Прошу подготовить доступ и выдать мне права."
        )
        assert classifier.classify(mail) == Category.REQUEST

    def test_finance(self, classifier):
        mail = Mail(
            sender="vendor@partner.ru",
            subject="Документы",
            body="Направляем счёт и акт. Просим подтвердить оплату. Вложение: invoice.pdf"
        )
        assert classifier.classify(mail) == Category.FINANCE

    def test_unknown(self, classifier):
        mail = Mail(
            sender="news@company.ru",
            subject="Новости",
            body="Свежий дайджест и новый выпуск! Наш клиент посетил портал. Итоги квартала в статье."
        )
        assert classifier.classify(mail) == Category.UNKNOWN


class TestCategorySubjects:
    def test_spam(self, classifier):
        mail = Mail(
            sender="unknown@test.com",
            subject="Срочно! Пройдите верификацию вашего аккаунта, вы выиграли iPhone 17 pro, только сегодня exclusive offer",
            body="Текст сообщения"
        )
        assert classifier.classify(mail) == Category.SPAM

    def test_incidents(self, classifier):
        mail = Mail(
            sender="user@corp.local",
            subject="URGENT: критический инцидент, никак не могу войти, ничего не запускается",
            body="Помогите починить"
        )
        assert classifier.classify(mail) == Category.INCIDENTS

    def test_request(self, classifier):
        mail = Mail(
            sender="manager@company.ru",
            subject="Запрос доступа, неисправность оборудования, заявка на отпуск, нет доступа после перевода",
            body="Тело письма"
        )
        assert classifier.classify(mail) == Category.REQUEST

    def test_finance(self, classifier):
        mail = Mail(
            sender="vendor@partner.ru",
            subject="Счёт на оплату, закрывающие документы, уточнение по оплате, договор",
            body="Во вложении"
        )
        assert classifier.classify(mail) == Category.FINANCE


class TestCategorySenders:
    def test_spam(self, classifier):
        mail = Mail(
            sender="a.kozlov@company.ru",
            subject="Подтвердите личность",
            body="Угроза блокировки! http://phishing-site.com/login"
        )
        assert classifier.classify(mail) == Category.SPAM

    def test_incidents(self, classifier):
        mail = Mail(
            sender="alerts@grafana.internal",
            subject="Массовый сбой",
            body="Работа остановлена у всех отдела. GitLab и Confluence лежат, BI и AD не отвечают."
        )
        assert classifier.classify(mail) == Category.INCIDENTS

    def test_request(self, classifier):
        mail = Mail(
            sender="k.morozov@company.ru",
            subject="Новый сотрудник",
            body="Для нового сотрудника нужен доступ к VPN, 1C и Confluence."
        )
        assert classifier.classify(mail) == Category.REQUEST

    def test_finance(self, classifier):
        mail = Mail(
            sender="t.andreev@company.ru",
            subject="Счёт",
            body="Оплата по счёту № 12345 от 10.10.2023. Даты оплаты согласованы. Прошу передать в бухгалтерию."
        )
        assert classifier.classify(mail) == Category.FINANCE

    def test_unknown(self, classifier):
        mail = Mail(
            sender="monitoring@internal",
            subject="Системное уведомление",
            body="[INFO] Общие уведомления, дайджесты. [WARNING] Незначительные ошибки."
        )
        assert classifier.classify(mail) == Category.UNKNOWN


class TestUnknownMail:
    def test_empty_mail(self, classifier):
        mail = Mail()
        assert classifier.classify(mail) == Category.UNKNOWN

    def test_unknown_words(self, classifier):
        mail = Mail(
            sender="random@email.com",
            subject="Просто сообщение",
            body="Здесь нет никаких триггерных слов из наших словарей."
        )
        assert classifier.classify(mail) == Category.UNKNOWN
