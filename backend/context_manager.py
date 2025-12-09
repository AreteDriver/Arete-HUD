class ContextManager:
    def __init__(self):
        self.contexts = {}

    def set_context(self, key, value):
        self.contexts[key] = value

    def get_context(self, key):
        return self.contexts.get(key)

    def clear_context(self):
        self.contexts.clear()
