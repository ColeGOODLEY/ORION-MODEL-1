"""
ORION MODEL 1
Central Intelligence Controller
"""

from core.identity import Identity
from core.personality import Personality
from core.state import State


class Orion:

    def __init__(self):

        self.identity = Identity()

        self.personality = Personality()

        self.state = State()


    def initialize(self):

        self.state.activate()

        print("Identity loaded.")
        print("Personality loaded.")
        print("State system loaded.")


    def process(self, message):

        message = message.lower()


        if "who are you" in message:

            identity = self.identity.describe()

            return (
                f"I am {identity['name']} "
                f"{identity['version']}. "
                f"{identity['purpose']}"
            )


        if "status" in message:

            return str(
                self.state.get_status()
            )


        return (
            "I received your request. "
            "My reasoning and memory systems "
            "will expand in future phases."
        )
