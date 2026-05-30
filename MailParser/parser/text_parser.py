from MailParser.domain.mail import Mail


def parse(text: str) -> Mail:
    mail = Mail()
    lines = text.splitlines()
    mail.body = ''
    for i in range(len(lines)):
        line = lines[i]
        if line.count(':') == 1:
            line_split = line.split(':')
            key = line_split[0]
            value = line_split[1]
        elif line.count(':') == 2:
            line_split = line.split(':')
            key = line_split[0]
            value = line_split[1] + ':' + line_split[2] 
        else:
            mail.body += line + '\n'
            continue
        if key == 'To' or key == 'Кому':
            mail.receiver = value.strip()
        elif key == 'From' or key == 'От кого':
            mail.sender = value.strip()
        elif key == 'Date' or key == 'Дата':
            mail.date = value.strip()
        elif key == 'Subject' or key == 'Тема':
            mail.subject = value.strip()
        else:
            mail.body += line + '\n'
    mail.body = mail.body.strip()
    return mail
