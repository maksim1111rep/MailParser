import pytest, shutil
from pathlib import Path
from processor import Processor

@pytest.fixture
def processor():
    return Processor()

class TestProcessorDirectoryHandling:
    def test_missing_input_directory(self, processor):
        with pytest.raises(FileNotFoundError, match="не существует"):
            processor.processFolder("bobobob", "aoaoaoaoa")

    def test_successful_processing(self, processor, tmp_path):
        input_dir = tmp_path / "inbox"
        input_dir.mkdir()
        output_dir = tmp_path / "output"
        
        base_path = Path(__file__).parent
        shutil.copy(base_path / "inbox" / "mail_0001.txt", input_dir / "mail_0001.txt")
        shutil.copy(base_path / "inbox" / "mail_0105.json", input_dir / "mail_0105.json")
        
        processor.processFolder(str(input_dir), str(output_dir))
        
        assert (output_dir / "incidents" / "mail_0001.txt").exists()
        assert (output_dir / "finance" / "mail_0105.json").exists()

class TestProcessorExceptions:
    def test_unsupported_file_fallback_to_unknown(self, processor, tmp_path):
        input_dir = tmp_path / "inbox"
        input_dir.mkdir()
        output_dir = tmp_path / "output"
        
        base_path = Path(__file__).parent
        shutil.copy(base_path / "inbox" / "mail_0104.bin", input_dir / "mail_0104.bin")
        
        processor.processFolder(str(input_dir), str(output_dir))
        
        assert (output_dir / "unknown" / "mail_0104.bin").exists()
