import argparse
import sys
from pathlib import Path
from MailParser.processor.processor import Processor
from MailParser.classification.classifier import Classifier
from MailParser.parser.file_parser import FileParser
from MailParser.domain.category import Category
from MailParser.logger_configuration import logging_settings
from MailParser.logger_configuration import logger
def create_parser():
    parser=argparse.ArgumentParser(
        prog="MailParser",
        description="Система обработки почты. Получает на вход множество писем, обрабатывает их и направляет по категориям, которым они соответствуют по смыслу")
    parser.add_argument("-i", "--input",
                        default="inbox",
                        type=Path,
                        help="Папка с письмами, которые нужно классифицировать")
    parser.add_argument("-o", "--output",
                        default="output",
                        type=Path,
                        help="Папка с письмами, разбитыми на категории")
    parser.add_argument("-st", "--stats",
                        action="store_true",
                        help="Вывод количества писем по каждой категории")
    parser.add_argument("-cnt", "--count",
                    choices=[category.value for category in Category],
                        help="Вывод количества писем в выбранной категории")
    return parser
def count_mails_in_category(output: Path, category: str)->int:
    path_category=output/category
    count = 0
    logger.info(f"Начат подсчет писем в категории {category}")
    for path in path_category.iterdir():
        count += 1
    return count
def get_stats(output: Path):
    for category in Category:
        count=count_mails_in_category(output, category.value)
        print(f"{category.value}: {count}")
def get_paths(input: Path)->list[Path]:
    mail_path=[]
    for file in input.iterdir():
        mail_path.append(file)
    return mail_path
def run():
    logging_settings()
    logger.info("Программа запущена")
    parser=create_parser()
    args=parser.parse_args()
    if len(sys.argv)==1:
        logger.info("Отсутствуют аргументы. Выведено описание команд")
        print("Доступные команды:")
        parser.print_help()
        return 0
    print("Запуск системы обработки почты")
    print(f"Источник необработанных писем: {args.input}")
    print(f"Источник отклассифицированных писем: {args.output}")
    classifier=Classifier()
    file_parser=FileParser()
    p=Processor(classifier,file_parser)
    logger.info("Начата обработка писем через процессор")
    p.processFolder(args.input, args.output)
    if args.stats:
        logger.info("Запрашивается статистика по всем категориям")
        get_stats(args.output)
        logger.info("Статистика выведена")
        return 0
    if args.count:
        logger.info(f"Запрашивается количество писем в {args.count}")
        count=count_mails_in_category(args.output, args.count)
        print(f"В категории {args.count}: {count} писем")
        return 0
    mail_path = get_paths(args.input)
    for path in mail_path:
        print(f"Письмо:{path}")
    return 0
if __name__=="__main__":
    run()



