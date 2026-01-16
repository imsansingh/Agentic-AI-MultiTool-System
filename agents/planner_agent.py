class PlannerAgent:
    def plan(self, query: str):
        return ["retrieve_context", "generate_answer", "verify"]
