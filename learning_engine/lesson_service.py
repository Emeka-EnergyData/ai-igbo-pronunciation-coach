from database.lesson_repository import get_lesson

def load_lesson(lesson_id):
    return get_lesson(lesson_id)
    