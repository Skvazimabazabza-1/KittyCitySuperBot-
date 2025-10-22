import json
import os
from datetime import datetime, timedelta
import requests

def format_time(seconds):
    """Форматирует время в читаемый вид"""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"

def format_coins(coins):
    """Форматирует количество монет"""
    return f"{coins:,}".replace(",", " ")

def is_new_day(last_date):
    """Проверяет, наступил ли новый день"""
    if not last_date:
        return True
    last = datetime.fromisoformat(last_date).date()
    return last < datetime.now().date()

def calculate_level(exp, current_level):
    """Рассчитывает уровень на основе опыта"""
    required_exp = current_level * 5
    if exp >= required_exp:
        return current_level + 1, 0
    return current_level, exp

def get_cat_status(cat_data):
    """Определяет статус котика по показателям"""
    hunger = cat_data.get('hunger', 0)
    cleanliness = cat_data.get('cleanliness', 0)
    mood = cat_data.get('mood', 0)
    health = cat_data.get('health', 0)
    
    if any(stat <= 1 for stat in [hunger, cleanliness, mood, health]):
        return "😨 Опасно!"
    elif any(stat <= 3 for stat in [hunger, cleanliness, mood, health]):
        return "😐 Нужен уход"
    else:
        return "😊 Отлично"

def test_yandex_connection(token):
    """Тестирует подключение к Яндекс Диску"""
    try:
        url = "https://cloud-api.yandex.net/v1/disk/"
        headers = {"Authorization": f"OAuth {token}"}
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            return True, {
                "user": data.get('user', {}).get('display_name', 'Unknown'),
                "total_space": data.get('total_space', 0),
                "used_space": data.get('used_space', 0),
                "free_space": data.get('total_space', 0) - data.get('used_space', 0)
            }
        else:
            return False, f"Ошибка: {response.status_code}"
            
    except Exception as e:
        return False, f"Исключение: {str(e)}"

def create_default_user(user_id, username):
    """Создает данные нового пользователя"""
    from config import CAT_NAME_OPTIONS, CAT_IMAGES, START_COINS
    
    return {
        "user_id": user_id,
        "username": username,
        "coins": START_COINS,
        "rating": 0,
        "created_at": datetime.now().isoformat(),
        "cat": {
            "name": CAT_NAME_OPTIONS[user_id % len(CAT_NAME_OPTIONS)],
            "hunger": 5,
            "cleanliness": 5,
            "mood": 5,
            "health": 5,
            "last_update": datetime.now().isoformat(),
            "level": 1,
            "exp": 0,
            "care_count": 0,
            "photo_index": user_id % len(CAT_IMAGES)
        },
        "inventory": [],
        "tasks": {},
        "used_promocodes": [],
        "daily_care_count": 0,
        "last_care_date": datetime.now().date().isoformat()
    }