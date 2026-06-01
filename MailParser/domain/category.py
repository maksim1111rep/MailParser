from enum import Enum


class Category(Enum):
    SPAM = "spam"
    INCIDENTS = "incidents"
    REQUEST = "request"
    FINANCE = "finance"
    UNKNOWN = "unknown"


CATEGORY_PRIORITY = {
    Category.SPAM: 4,
    Category.INCIDENTS: 3,
    Category.REQUEST: 2,
    Category.FINANCE: 1,
    Category.UNKNOWN: 0,
}

CATEGORY_KEYWORDS = {
    Category.SPAM: ['перейдите', 'введите', 'ссылке', 'через', 'аккаунт', 'немедленно', 'поздравляем', 'карты',
                    'банковской',
                    'данные', 'http://totally-not-spam.ru/prize', 'приза', 'получения', 'розыгрыша', 'победителем',
                    'стали'],
    Category.INCIDENTS: ['после', 'обновления', 'уже', 'отдела', 'при', 'ошибка',
                         'появляется', 'перестал', 'утреннего', 'открываться'],
    Category.REQUEST: ['прошу', 'доступ', 'нужно', 'подготовить', 'наталья'],
    Category.FINANCE: ['оплата', 'оплаты', 'за', 'направляем']
}

CATEGORY_SENDERS = {
    Category.SPAM: ['a.kozlov@company.ru', 't.andreev@company.ru'],
    Category.INCIDENTS: ['Елена Новикова <e.novikova@corp.local>', 'a.fedorova@company.ru',
                         'alerts <alerts@grafana.internal>', 'a.fedorova@company.ru', 's.volkov@partner.ru',
                         'Иван Петров <i.petrov@company.ru>', 'alerts@grafana.internal', 'p.sokolov@vendor.net'],
    Category.REQUEST: ['Светлана Попова <s.popova@company.ru>', 'Людмила Захарова <l.zaharova@corp.local>',
                       'no-reply <no-reply@monitoring.internal>', 'alerts', 'Елена Новикова <e.novikova@corp.local>',
                       'o.belova@client.biz',
                       'Михаил Сидоров <m.sidorov@company.ru>', 'Анна Фёдорова <a.fedorova@company.ru>',
                       'k.morozov@company.ru', 'Kate Brown <k.brown@extern.org>',
                       'v.gromov@partner.ru', 'Дмитрий Орлов <d.orlov@corp.local>'],
    Category.FINANCE: ['Юлия Кириллова <yu.kirillova@company.ru>', 'Kate Brown <k.brown@extern.org>',
                       'n.lebedeva@corp.local', 'yu.kirillova@company.ru', 'Наталья Лебедева <n.lebedeva@corp.local>',
                       'Тимур Андреев <t.andreev@company.ru>',
                       'Анна Фёдорова <a.fedorova@company.ru>']
}

CATEGORY_SUBJECTS = {
    Category.SPAM: ['подтвердите', 'срочно', '15!', 'iphone', 'выиграли',
                    'вы', 'exclusive', 'верификация', 'time', 'limited', 'offer', 'личность'],
    Category.INCIDENTS: ['не', 'ошибка', 'обновления', 'остановлена', 'работа', 'падает',
                        'отдела', 'у', 'войти', 'могу', 'антивирус', 'критический', 'при', 'запускается', 'недоступен',
                          'bi-система', 'инцидент', 'авторизации', 'массовый', 'сбой', 'reader', 'браузер', 'chrome', 'зависает'],
    Category.REQUEST: ['к', 'доступа', 'запрос', 'оборудования:', 'сотрудника', 'нового', 'для',
                             'неисправность', 'права', 'нужны', 'vpn', 'гарнитура', 'нет', 'после', 'перевода', 'проблема', 'почта',
                             'ноутбук', 'заявка', 'отпуск', 'лист', 'больничный', 'изменение', 'работы', 'графика'],
    Category.FINANCE: ['уточнение', 'по', 'оплате', 'договора', 'за', 'документы', 'закрывающие', 'правки', 'финальная', 'инструкция',
                            'оплату', 'счёт', '№','fwd:', 'декабрь', 'апрель', 'работ', 'выполненных',
                            'акт', 'согласование', 'инструкцияу', 'техническое', 'договор']
}

CATEGORY_WEIGHTS_BODY = {
    Category.SPAM: 0.23,
    Category.INCIDENTS: 0.36,
    Category.REQUEST: 0.64,
    Category.FINANCE: 0.94,
    Category.UNKNOWN: 0
}

CATEGORY_WEIGHTS_SUBJECT = {
    Category.SPAM: 0.5,
    Category.INCIDENTS: 0.48,
    Category.REQUEST: 0.37,
    Category.FINANCE: 0.365,
    Category.UNKNOWN: 0
}
