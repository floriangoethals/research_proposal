from llama_index.llms.ollama import Ollama
from llama_index.core import Settings
from llama_parse import LlamaParse
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, PromptTemplate
from llama_index.core.embeddings import resolve_embed_model
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from prompts import context, context2
from dotenv import load_dotenv
from pubmed_reader import already_researched
import os
import nest_asyncio

# problem in jupyter notebook not allowing nested async
nest_asyncio.apply()
Settings.llm = Ollama(model="deepseek-r1:8b", request_timeout=60) # with 500 it works
llm = Settings.llm

load_dotenv()
api_key = os.getenv("LLAMA_CLOUD_API_KEY")


parser = LlamaParse(result_type='markdown', api_key=api_key)
file_extractor = {'.pdf': parser}
documents = SimpleDirectoryReader('data', file_extractor=file_extractor).load_data()
 
# local model for creating vector
embed_model = resolve_embed_model("local:BAAI/bge-m3")
vector_index = VectorStoreIndex.from_documents(documents, embed_model = embed_model)
query_engine = vector_index.as_query_engine(llm = llm)

tools = [
    QueryEngineTool(
        query_engine = query_engine,
        metadata = ToolMetadata(
            name ="research_context",
            description = "this tool gives acces to the context around the subject, it parses and analyses pdf files about a scientific research field",

        ),
    ),
    already_researched,
]


# verbose will give thought process of the agent, verbose True will give agent's thinking process, False will eliminate that
agent = ReActAgent.from_tools(tools, llm = llm , verbose = True, context = context2)


while(prompt := input("Enter a prompt(q to quit): ")) != "q":
    result = agent.query(prompt)
    print(result)

