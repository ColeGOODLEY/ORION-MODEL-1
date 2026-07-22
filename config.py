"""
ORION MODEL 1
Configuration System
"""

import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """
    Central configuration manager.
    """

    ORION_NAME = "ORION"

    VERSION = "Model 1.0"

    CREATOR = "Cole"

    DEBUG = True

    MEMORY_PATH = "data/memories.json"

    LOG_PATH = "logs/orion.log"

    def display(self):
        return {
            "name": self.ORION_NAME,
            "version": self.VERSION,
            "creator": self.CREATOR
        }


config = Config()
