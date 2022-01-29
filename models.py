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

    def get_time(self):
        return self.time_lesson

class Attends:
    def __init__(self, user, date, count_children_attends):
        self.user_id = user.user_id
        self.name = user.name
        self.date = date
        self.count_children_attends = count_children_attends
    
    def to_json(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "date": self.date,
            "count_child": self.count_children_attends
        }