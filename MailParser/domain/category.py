from enum import Enum


class Category(Enum):
    CRITICAL = "critical"
    IMPORTANT = "important"
    AVERAGE = "average"
    UNIMPORTANT = "unimportant"
    SPAM = "spam"
    UNKNOWN = "unknown"

CATEGORY_PRIORITY = {
    Category.CRITICAL: 4,
    Category.IMPORTANT: 3,
    Category.AVERAGE: 2,
    Category.UNIMPORTANT: 1,
    Category.UNKNOWN: 0,
    Category.SPAM: -1
}

CATEGORY_KEYWORDS = {
    Category.CRITICAL: ["критическое", "ужас", "трагедия"],
    Category.IMPORTANT: ["срочно, помогите", "плохо"],
    Category.AVERAGE: ["доступ", "права", "договор"],
    Category.UNIMPORTANT: ["приколы", "игра", "рыбалка"],
    Category.SPAM: ["фишинг", "скам"]
}