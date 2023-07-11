import os
from codementor.agent.agent import Agent


def main():

    print("test")
    print(os.environ.get("OPENAI_API_KEY"))
    Agent().start_interaction_loop()

