from sqlalchemy import text
from src.database.connection import engine

def get_lesson(lesson_id):
    query = text("""
            SELECT 
                lesson_id,
                lesson_number,
                title,
                concept
            FROM lessons 
            WHERE lesson_id = :lesson_id""")
    with engine.connect() as connection:
        result = connection.execute(query, {"lesson_id": lesson_id})
        return result.mappings().first()
    
def get_lesson_items(lesson_id):
    query = text("""
            SELECT * 
            FROM lesson_items
            WHERE lesson_id = :lesson_id""")
    with engine.connect() as connection:
        result = connection.execute(query, {"lesson_id": lesson_id})
        return result.mappings().all()
    
def get_exercises(lesson_id):
    query = text("""
            SELECT * 
            FROM exercises
            WHERE lesson_id = :lesson_id""""")
    with engine.connect() as connection:
        result = connection.execute(query, {"lesson_id": lesson_id})
        return result.mappings().all()