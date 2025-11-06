import importlib
import os
import traceback


class EscapeRoom:

    def __init__(self, response):
        self.response = response
        self.levels = []
        self.room_name = "Unknown"
        self.author = "Unknown"

    def add_level(self, level):
        self.levels.append(level)

    def get_levels(self):
        return self.levels

    def get_level(self, number):
        return self.levels[number]

    def get_name(self):
        return self.room_name

    def set_metadata(self, author, room_name):
        self.room_name = room_name
        self.author = author

    def get_metadata(self):
        return {"author": self.author, "room_name": self.room_name, "levels": len(self.levels)}

    def check_solution(self, solution_filename, correct_function, data):
        solution = self.run_code(solution_filename, data)
        correct = solution == correct_function(data)
        return {"correct": correct, "solution": solution}

    def run_code(self, filename, data):
        try:
            mod = importlib.import_module(filename)
            importlib.reload(mod)
            return mod.run(data)
        except ModuleNotFoundError:
            print(f"Couldn't find: {os.getcwd()}/{filename}.")
            return False
        except Exception as e:
            print(traceback.print_exc())
            print(f"Error in solution check")
            print(e)

            return False
