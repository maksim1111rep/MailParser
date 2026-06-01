import pytest, shutil
from pathlib import Path
from MailParser.processor.processor import Processor
from MailParser.classification.classifier import Classifier
from MailParser.parser.file_parser import FileParser


@pytest.fixture
def processor():
    return Processor(Classifier(), FileParser())


class TestProcessorDirectoryHandling:
    def test_missing_input_directory(self, processor):
        with pytest.raises(FileNotFoundError, match="не существует"):
            processor.processFolder("bobobob", "aoaoaoaoa")

    def test_successful_processing(self, processor, tmp_path):
        input_dir = tmp_path / "inbox"
        input_dir.mkdir()
        output_dir = tmp_path / "output"

        (input_dir / "mail_0001.txt").write_text(
            """Subject: браузер Chrome зависает при открытии
    From: s.volkov@partner.ru

    Здравствуйте!

    После обновления системы браузер Chrome не открывает файлы нужного формата. Раньше всё работало.

    Спасибо.""",
            encoding="utf-8",
        )
        (input_dir / "mail_0105.json").write_text(
            """{"from": "test@corp", "subject": "Ваш аккаунт будет заблокирован", "body":""",
            encoding="utf-8",
        )
        processor.processFolder(str(input_dir), str(output_dir))

        assert (output_dir / "incidents" / "mail_0001.txt").exists()
        assert (output_dir / "spam" / "mail_0105.json").exists()


class TestProcessorExceptions:
    def test_unsupported_file_fallback_to_unknown(self, processor, tmp_path):
        input_dir = tmp_path / "inbox"
        input_dir.mkdir()
        output_dir = tmp_path / "output"

        (input_dir / "mail_0104.bin").write_bytes(b"123")

        processor.processFolder(str(input_dir), str(output_dir))

        assert (output_dir / "broken" / "mail_0104.bin").exists()
