from llama_index.core.tools import FunctionTool
from Bio.Entrez import efetch
from Bio import Entrez
import certifi
import ssl
from dotenv import load_dotenv

ssl._create_default_https_context = ssl._create_unverified_context

def pubmedsearch(query):
    """
    This function can search the pubmed database using keywords and find matching articles
    It can therefore know if the presented keywords have a match, 
    read the description of the article and see if there is an article that ressembles the research idea.
    """
    Entrez.email = "MAIL"
    #return a pubmed article based on the query of some keywords (query)
    handle = Entrez.esearch(db="pubmed", term=query, retmax=5)  # Retrieve 5 results
    record = Entrez.read(handle)
    handle.close()
    pmids = record["IdList"]
    print("PMIDs:", pmids)

    return pmids


def pubmed_summary(pmid):
    """
    this tool takes a pubmed article ID and returns the abstract of the research document.
    """
    handle = efetch(db='pubmed', id=pmid, retmode='text', rettype='abstract')
    return print(handle.read())
    


def research_in_context(query):
    articles = pubmedsearch(query=query)
    field = []
    for i in articles: 
        pubmed_summary(i)
        field.append(i) 
    
    return field


already_researched = FunctionTool.from_defaults(
    fn = research_in_context,
    name= "science_field_retriever",
    description= """ This tool can research what is already known about a topic,
        use this to retrieve information about what has already been researched in this
        field of study"""
        )