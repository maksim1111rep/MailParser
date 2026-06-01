import argparse
from pathlib import Path
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
    parser.add_argument("-st", "--status",
                        action="store_true",
                        help="Вывод статистики по категориям")
    parser.add_argument("-cnt", "--count",
                    choices=["CRITICAL", "IMPORTANT", "AVERAGE", "UNIMPORTANT"])
    return parser
def count_mails_in_category(output: Path, path: str, category: str)->int:
    path_category=output/category
    count = 0
    for path in path_category.iterdir():
        count += 1
    return count

def get_paths(input: Path)->list[Path]:
    mail_path=[]
    for file in input.iterdir():
        mail_path.append(file)
    return mail_path
def run():
    parser=create_parser()
    args=parser.parse_args()
    print("Запуск системы обработки почты")
    print(f"Ввод: {args.input}")
    print(f"Вывод: {args.output}")
    mail_path=get_paths(args.input)
    for path in mail_path:
        print(f"Письмо:{path}")
    return 0
if __name__=="__main__":
    run()



