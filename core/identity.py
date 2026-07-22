"""
ORION Identity System
"""


class Identity:

    def __init__(self):

        self.name = "ORION"

        self.version = "Model 1.0"

        self.purpose = (
            "A personal AI assistant "
            "designed to grow through "
            "reasoning, memory, and tools."
        )


    def describe(self):

        return {
            "name": self.name,
            "version": self.version,
            "purpose": self.purpose
        }
