from src.database.lesson_repository import get_lesson, get_lesson_items, get_exercises

def load_lesson(lesson_id):
    lesson = get_lesson(lesson_id)
    items = get_lesson_items(lesson_id)
    exercises = get_exercises(lesson_id)
    return {"lesson": lesson, "compound_letters": items, "exercises": exercises}
    