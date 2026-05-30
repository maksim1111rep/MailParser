from MailParser.domain.mail import Mail
from MailParser.domain.category import CATEGORY_KEYWORDS, CATEGORY_PRIORITY, Category
from dataclasses import dataclass

@dataclass
class Classifier:
    weightSubject = 5
    weightBody = 1

    def __init__(self):
        self.keywords = CATEGORY_KEYWORDS
        self.categoryPriority = CATEGORY_PRIORITY

    def classify(self, mail: Mail) -> Category:
        if not mail.subject and not mail.body:
            return Category.UNKNOWN
        scores = {category: 0 for category in self.keywords.keys()}
        if mail.subject:
            subjectLower = mail.subject.lower()
        else:
            subjectLower = ''
        if mail.body:
            bodyLower = mail.body.lower()
        else:
            bodyLower = ''
        for category, markers in self.keywords.items():
            for marker in markers:
                markerLower = marker.lower()
                if markerLower in subjectLower:
                    scores[category] += self.weightSubject
                if markerLower in bodyLower:
                    scores[category] += self.weightBody
        max_score = max(scores.values()) if scores else 0
        if max_score == 0:
            return Category.UNKNOWN
        bestCategories = [category for category, score in scores.items() if score == max_score]
        if len(bestCategories) == 1:
            return bestCategories[0]
        return self.getHighestPriorityCategory(bestCategories)

    def getHighestPriorityCategory(self, categories):
        if not categories:
            return Category.UNKNOWN
        return max(categories, key=lambda category: self.categoryPriority.get(category, 0))
