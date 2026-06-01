import shutil
from pathlib import Path
from MailParser.parser.file_parser import FileParser
from MailParser.classification.classifier import Classifier
from MailParser.domain.category import Category
from dataclasses import dataclass
@dataclass
class Processor:

    def __init__(self, classifier: Classifier, parser: FileParser):
        self.classifier = classifier
        self.parser = parser

    def processFolder(self, input_path: str, output_path: str):
        inputDir = Path(input_path)
        outputDir = Path(output_path)

        if not inputDir.exists():
            raise FileNotFoundError(f"Папка {input_path} не существует")

        if outputDir.exists():
            if inputDir.resolve() == outputDir.resolve():
                raise ValueError("Папки input и output не должны совпадать")
            shutil.rmtree(outputDir)
        outputDir.mkdir(parents=True, exist_ok=True)

        files = [file for file in inputDir.iterdir() if file.is_file()]
        for file in files:
            try:
                mail = self.parser.parse(file)
                category = self.classifier.classify(mail)
                self.copyToCategory(file, category, outputDir)

            except ValueError as e:
                category =  Category.BROKEN
                self.copyToCategory(file, category, outputDir)

    def copyToCategory(self, sourcePath, category, outputDir):
        categoryDir = outputDir / category.value
        categoryDir.mkdir(exist_ok=True)
        targetPath = categoryDir / sourcePath.name
        shutil.copy2(sourcePath, targetPath)
