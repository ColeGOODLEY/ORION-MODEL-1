"""
ORION State System
"""


class State:

    def __init__(self):

        self.status = "offline"

        self.current_task = None


    def activate(self):

        self.status = "online"


    def get_status(self):

        return {
            "status": self.status,
            "task": self.current_task
        }
