"""
ORION MODEL 1
Main Startup System
"""

from core.orion import Orion


def startup():

    print("""
====================================
        ORION MODEL 1 ONLINE
====================================
""")

    orion = Orion()

    orion.initialize()

    print("\nORION is ready.\n")

    while True:

        user_input = input("YOU: ")

        if user_input.lower() in [
            "exit",
            "shutdown",
            "quit"
        ]:
            print("\nORION shutting down.")
            break

        response = orion.process(user_input)

        print(f"\nORION: {response}\n")


if __name__ == "__main__":
    startup()
