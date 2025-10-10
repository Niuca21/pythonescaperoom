import random
import string
from EscapeRoom import EscapeRoom

class CyberHackRoom(EscapeRoom):
    def __init__(self):
        super().__init__()
        self.set_metadata("CyberHackRoom", __name__)
        self.add_level(self.level_1)
        self.add_level(self.level_2)
        self.add_level(self.level_3)
        self.add_level(self.level_4)
        self.add_level(self.level_5)
        self.add_level(self.level_6)

    def level_1(self, secret):
        return "Level 1 Platzhalter"

    def level_2(self, secret):
        return "Level 2 Platzhalter"

    def level_3(self, secret):
        return "Level 3 Platzhalter"

    def level_4(self, secret):
        return "Level 4 Platzhalter"

    def level_5(self, secret):
        return "Level 5 Platzhalter"

    def level_6(self, secret):
        return "Level 6 Platzhalter"
