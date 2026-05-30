from enum import Enum


class Category(Enum):
    CRITICAL = "critical"
    IMPORTANT = "important"
    AVERAGE = "average"
    UNIMPORTANT = "unimportant"

CATEGORY_PRIORITY = {
    Category.CRITICAL: 1,
    Category.IMPORTANT: 2,
    Category.AVERAGE: 3,
    Category.UNIMPORTANT: 4
}

CATEGORY_KEYWORDS = {
    Category.CRITICAL: ["критическое", "ужас", "трагедия"],
    Category.IMPORTANT: ["срочно, помогите", "плохо"],
    Category.AVERAGE: ["доступ, права, договор"],
    Category.UNIMPORTANT: ["скам", "фишинг", "рыбалка"]
}