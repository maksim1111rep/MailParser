import shutil
from pathlib import Path
from MailParser.parser.file_parser import FileParser
from MailParser.classification.classifier import Classifier
from MailParser.domain.category import Category
from dataclasses import dataclass
from MailParser.logger_configuration import logger
@dataclass
class Processor:

    def __init__(self, classifier: Classifier, parser: FileParser):
        self.classifier = classifier
        self.parser = parser

    def processFolder(self, input_path: str, output_path: str):
        logger.info("Начата обработка папки с неклассифицированными письмами}")
        inputDir = Path(input_path)
        outputDir = Path(output_path)

        if not inputDir.exists():
            logger.error("Не передана папка с неклассифицированными письмами")
            raise FileNotFoundError(f"Папка {input_path} не существует")

        if outputDir.exists():
            if inputDir.resolve() == outputDir.resolve():
                logger.error("Папки input и output совпадают")
                raise ValueError("Папки input и output не должны совпадать")
            logger.info(f"Старая папка для отклассифицированных писем удалена: {outputDir}")
            shutil.rmtree(outputDir)
        outputDir.mkdir(parents=True, exist_ok=True)
        logger.info(f"Новая папка для отклассифицированных писем создана: {outputDir}")

        files = [file for file in inputDir.iterdir() if file.is_file()]
        for file in files:
            try:
                logger.info(f"Начата обработка письма {file.name}")
                mail = self.parser.parse(file)
                logger.info(f"Письмо {file.name} обработано")
                category = self.classifier.classify(mail)
                logger.info(f"Письмо {file.name} классифицировано в {category.value}")
                self.copyToCategory(file, category, outputDir)

            except ValueError as e:
                logger.warning(f"Ошибка при обработке файла {file.name}: {e}. Назначена категория broken")
                category =  Category.BROKEN
                self.copyToCategory(file, category, outputDir)

    def copyToCategory(self, sourcePath, category, outputDir):
        categoryDir = outputDir / category.value
        categoryDir.mkdir(exist_ok=True)
        targetPath = categoryDir / sourcePath.name
        shutil.copy2(sourcePath, targetPath)
        logger.info(f"Письмо скопировано {sourcePath} -> {targetPath}")
