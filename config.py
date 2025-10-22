import os

# === КОНФИГУРАЦИЯ БОТА ===
BOT_TOKEN = os.getenv("BOT_TOKEN", "8429919809:AAE5lMwVmH86X58JFDxYRPA3bDbFMgSgtsw")
ADMIN_ID = int(os.getenv("ADMIN_ID", "5531546741"))
YANDEX_TOKEN = os.getenv("YANDEX_TOKEN", "y0__xDo1ejABhjblgMgr8ek6xT0N1yRgkT9l_OLaTYIDPPD5wSscA")

# === REPLIT КОНФИГ ===
REPL_OWNER = "timabrilevich"
REPL_SLUG = "KittyCitySuperBot-1"

# === НАСТРОЙКИ ИГРЫ ===
START_COINS = 50
CARE_REWARD = 3
DAILY_CARE_LIMIT = 10
MAX_CAT_STATS = 10
UPGRADE_COST = 10

# === ИЗОБРАЖЕНИЯ КОТОВ ===
CAT_IMAGES = [
    "cat1.jpg", "cat2.jpg", "cat3.jpg", "cat4.jpg", "cat5.jpg",
    "cat6.jpg", "cat7.jpg", "cat8.jpg", "cat9.jpg", "cat10.jpg"
]

# === ИМЕНА КОТОВ ===
CAT_NAME_OPTIONS = [
    "Барсик", "Мурзик", "Васька", "Рыжик", "Снежок", "Пушок", "Кузя", "Тигра", 
    "Луна", "Симба", "Оскар", "Гарфилд", "Том", "Феликс", "Чарли", "Макс"
]

# === ИГРУШКИ ===
TOYS = {
    'i1': {'name': 'i1', 'price': 20, 'emoji': '🎾', 'display_name': 'Мячик'},
    'i2': {'name': 'i2', 'price': 30, 'emoji': '🐟', 'display_name': 'Рыбка'},
    'i3': {'name': 'i3', 'price': 40, 'emoji': '🎯', 'display_name': 'Мишень'},
    'i4': {'name': 'i4', 'price': 50, 'emoji': '🧶', 'display_name': 'Клубок'},
    'i5': {'name': 'i5', 'price': 60, 'emoji': '🐭', 'display_name': 'Мышка'},
}

# === ЛЕЖАНКИ ===
BEDS = {
    'bed1': {'name': 'bed1', 'price': 150, 'emoji': '🛏️', 'display_name': 'Лежанка 1'},
    'bed2': {'name': 'bed2', 'price': 200, 'emoji': '🏠', 'display_name': 'Лежанка 2'},
    'bed3': {'name': 'bed3', 'price': 250, 'emoji': '🛋️', 'display_name': 'Лежанка 3'},
    'bed4': {'name': 'bed4', 'price': 300, 'emoji': '🏰', 'display_name': 'Лежанка 4'},
}

# === URL ДЛЯ ПИНГОВ ===
SELF_URLS = [
    f"https://{REPL_SLUG}.{REPL_OWNER}.repl.co/",
    f"https://{REPL_SLUG}.{REPL_OWNER}.repl.co/ping", 
    f"https://{REPL_SLUG}.{REPL_OWNER}.repl.co/health",
    f"https://{REPL_SLUG}.{REPL_OWNER}.repl.co/status",
    f"https://{REPL_SLUG}.{REPL_OWNER}.repl.co/api/v1/keepalive"
]

EXTERNAL_URLS = [
    "https://www.google.com",
    "https://api.telegram.org",
    "https://yandex.ru",
    "https://github.com",
    "https://stackoverflow.com",
    "https://httpbin.org/get",
    "https://jsonplaceholder.typicode.com/posts/1"
]