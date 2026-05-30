def parse(text):
    data_for_class = {}
    lines = text.splitlines()
    properties = ['To', 'From', 'Date', 'Subject', 'Body']
    for x in properties:
        data_for_class[x] = None
    data_for_class['Body'] = ''
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
            data_for_class['Body'] += line + '\n'
            continue
        if key == 'To' or key == 'Кому':
            data_for_class['To'] = value.strip()
        elif key == 'From' or key == 'От кого':
            data_for_class['From'] = value.strip()
        elif key == 'Date' or key == 'Дата':
            data_for_class['Date'] = value.strip()
        elif key == 'Subject' or key == 'Тема':
            data_for_class['Subject'] = value.strip()
        else:
            data_for_class['Body'] += line + '\n'
    data_for_class['Body'] = data_for_class['Body'].strip()
    return data_for_class
