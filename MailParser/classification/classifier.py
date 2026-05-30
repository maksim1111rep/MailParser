from MailParser.domain.category import Mail
from dataclasses import dataclass
from typing import Dict, List
@dataclass
class Classifier:
    weightSubject = 5
    weightBody = 1

    def __init__(self, keywords: Dict[str, List[str]],
                 categoryPriority: Dict[str, int]):
        self.keywords = keywords
        self.categoryPriority = categoryPriority

    def classify(self, mail: Mail):
        if not mail.subject and not mail.body:
            return 'Пустое'
        scores = {category: 0 for category in self.keywords.keys()}
        if mail.subject:
            subjectLower = mail.subject.lower()
        else:
            subjectLower = ''
        if mail.body:
            bodyLower = mail.body.lower()
        else:
            subjectLower = ''
        for category, markers in self.keywords.items():
            for marker in markers:
                markerLower = marker.lower()
                if markerLower in subjectLower:
                    scores[category] += self.weightSubject
                if markerLower in bodyLower:
                    scores[category] += self.weightBody
        max_score = max(scores.values()) if scores else 0
        if max_score == 0:
            return "Не классифицировано"
        bestCategories = [category for category, score in scores.items() if score == max_score]
        if len(bestCategories) == 1:
            return bestCategories[0]
        return self.getHighestPriorityCategory(bestCategories)

    def getHighestPriorityCategory(self, categories):
        if not categories:
            return "Не классифицировано"
        return max(categories, key=lambda category: self.categoryPriority.get(category, 0))
