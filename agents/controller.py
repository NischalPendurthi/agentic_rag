from agents.retriever import Retriever
from agents.reasoner import reasoner
from agents.summarizer import Summarizer

class Controller:
    def __init__(self):
        self.retriever = Retriever()
        self.summarizer = Summarizer()

    def process_query(self, query):
        # Retrieve relevant documents
        documents = self.retriever.retrieve(query)
        context = "\n".join(documents)
        
        # Reason with context
        reasoner_input = f"Query: {query}\nContext: {context}"
        reasoner_response = reasoner(reasoner_input)
        
        # Summarize the response
        summary = self.summarizer.summarize(reasoner_response)
        return summary