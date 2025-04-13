import json
import os

class Dish:
    def __init__(self, name, cost, desc):
        self.name = name
        self.cost = cost
        self.desc = desc

    def to_dict(self):
        return {"name": self.name, "cost": self.cost, "desc": self.desc}

    def __repr__(self):
        return f"{self.name}\n{self.cost} ₸\n{self.desc}"


class Menu:
    def __init__(self):
        self.menu = []

    def add(self, obj):
        self.menu.append(obj)

    def from_dict(self, dict):
        self.menu.append(Dish(dict["name"], dict["cost"], dict["desc"]))

    def load_from_file(self, filename):
        if not os.path.exists(filename):
            self.save_to_file(filename)
            return

        with open(filename, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if not content:
                return
            data = json.loads(content)
            for item in data:
                self.from_dict(item)

    def save_to_file(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump([dish.to_dict() for dish in self.menu], f, ensure_ascii=False, indent=2)

