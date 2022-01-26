class User:
    def __init__(self, user_id=0, name="") -> None:
        self.user_id = user_id
        self.name = name
        self.times = []
    def to_json(self):
        return {
            "name": self.name,
            "times": []
        }

    def __repr__(self) -> str:
        return f"User(name={self.name})"

class Time_Lesson:

    def __init__(self, time_lesson, user_id):
        self.time_lesson = time_lesson
        self.user_id = user_id
    
    def to_json(self):
        return {
            # "time_id": self.id,
            "time": self.time_lesson.strftime("%H:%M")
        }

    def __repr__(self) -> str:
        return f"Time(user_id={self.user_id}, time={self.time_lesson})"