from MailParser.domain.mail import Mail
from MailParser.logger_configuration import logger

def parse(text: str) -> Mail:
    logger.info("Начат анализ текста письма")
    mail = Mail()
    lines = text.splitlines()
    mail.body = ''
    for i in range(len(lines)):
        line = lines[i]
        if line.count(':') == 1:
            line_split = line.split(':')
            key = line_split[0].lower()
            value = line_split[1]
        elif line.count(':') == 2:
            line_split = line.split(':')
            key = line_split[0].lower()
            value = line_split[1] + ':' + line_split[2]
        else:
            mail.body += line + '\n'
            logger.debug(f"В тело письма добавлено {line}")
            continue
        if key == 'to' or key == 'кому':
            mail.receiver = value.strip()
        elif key == 'from' or key == 'от кого':
            mail.sender = value.strip()
        elif key == 'date' or key == 'дата':
            mail.date = value.strip()
        elif key == 'subject' or key == 'тема':
            mail.subject = value.strip()
        else:
            mail.body += line + '\n'
    mail.body = mail.body.strip()
    logger.info("Разбор письма завершён")
    return mail
