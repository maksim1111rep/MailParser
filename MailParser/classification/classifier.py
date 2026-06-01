from MailParser.domain.mail import Mail
from MailParser.domain.category import CATEGORY_KEYWORDS, CATEGORY_PRIORITY, CATEGORY_SENDERS, CATEGORY_SUBJECTS, CATEGORY_WEIGHTS_BODY, CATEGORY_WEIGHTS_SUBJECT, Category
from dataclasses import dataclass
from MailParser.logger_configuration import logger

@dataclass
class Classifier:
    weightSender = 1

    def __init__(self):
        self.keywords = CATEGORY_KEYWORDS
        self.senders = CATEGORY_SENDERS
        self.subjects = CATEGORY_SUBJECTS
        self.categoryPriority = CATEGORY_PRIORITY
        self.weightSubject = CATEGORY_WEIGHTS_SUBJECT
        self.weightBody = CATEGORY_WEIGHTS_BODY

    def classify(self, mail: Mail) -> Category:
        logger.info("Начало классификации письма")
        if not mail.subject and not mail.body:
            logger.warning("У письма отсутствуют тема и текст. Назначена категория: unknown")
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
        if mail.sender:
            senderLower = mail.sender.lower()
        else:
            senderLower = ''
        for category, markers in self.keywords.items():
            weight = self.weightBody.get(category, 0)
            for marker in markers:
                markerLower = marker.lower()
                if markerLower in bodyLower:
                    scores[category] += weight
        for category, markers in self.subjects.items():
            weight = self.weightSubject.get(category, 0)
            for marker in markers:
                markerLower = marker.lower()
                if markerLower in subjectLower:
                    scores[category] += weight
        for category, markers in self.senders.items():
            for marker in markers:
                markerLower = marker.lower()
                if markerLower in senderLower:
                    scores[category] += self.weightSender
        max_score = max(scores.values()) if scores else 0
        if max_score == 0:
            logger.info(f"Нет совпадений с ключевыми словами категорий. Назначена категория: unknown")
            return Category.UNKNOWN
        bestCategories = [category for category, score in scores.items() if score == max_score]
        if len(bestCategories) == 1:
            logger.info(f"Письмо классифицировано в {bestCategories[0].value}")
            return bestCategories[0]
        logger.info(f"Несколько категорий с одинаковыми баллами: {[category.value for category in bestCategories]}")
        return self.getHighestPriorityCategory(bestCategories)

    def getHighestPriorityCategory(self, categories):
        if not categories:
            logger.warning("Список категорий для выбора по приоритету пуст. Назначена категория: unknown")
            return Category.UNKNOWN
        logger.info("Назначена категория с наибольшим приоритетом")
        return max(categories, key=lambda category: self.categoryPriority.get(category, 0))
