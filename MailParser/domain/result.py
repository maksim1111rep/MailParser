from dataclasses import dataclass

from MailParser.domain.category import Category


@dataclass
class ClassificationResult:
    category: Category
    score: int
    reason: str