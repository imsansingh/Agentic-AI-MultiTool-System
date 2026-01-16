from agents.planner_agent import PlannerAgent
from agents.retriever_agent import RetrieverAgent
from agents.executor_agent import ExecutorAgent
from agents.verifier_agent import VerifierAgent

def run_workflow(query: str):
    planner = PlannerAgent()
    retriever = RetrieverAgent()
    executor = ExecutorAgent()
    verifier = VerifierAgent()

    plan = planner.plan(query)
    context = retriever.retrieve(query)
    answer = executor.execute(context)
    return verifier.verify(answer)
