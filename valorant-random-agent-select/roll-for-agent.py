import json
import random
import os

# Agent object
class Agent():
    def __init__(self, name, role, owned):
        self.name = name
        self.role = role
        self.owned = owned

clear = lambda: os.system('cls')
clear()

with open('available-agents.json', 'r') as file:
    jsonFile = json.load(file)
    agent_list = jsonFile["agents"]
    agents = [Agent(**agent) for agent in agent_list]

candidates = []

for agent in agents:
    if agent.owned is True:
        candidates.append(agent)
        
random_agent = random.choice(candidates)
print("{0} as {1}".format(random_agent.name, random_agent.role))