from src.database.lesson_repository import get_lesson, get_lesson_items, get_exercises

lesson = get_lesson(1)
lesson_items = get_lesson_items(1)
exercises = get_exercises(1)

print(lesson)
print(lesson_items)
print(exercises)