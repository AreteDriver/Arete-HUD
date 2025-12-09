class Agent:
    def __init__(self, name):
        self.name = name

    def act(self, context):
        # Agent logic goes here
        return f"Agent {self.name} acts on context {context}"

class AgentManager:
    def __init__(self):
        self.agents = {}

    def add_agent(self, name):
        self.agents[name] = Agent(name)

    def get_agent(self, name):
        return self.agents.get(name)
