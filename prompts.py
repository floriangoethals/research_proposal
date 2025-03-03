context = """purpose: the primary role of this agent is to assist professors in the generation of scientific research proposals in the context of medical research. 
    By analysing existing research papers in a similar field, the agent will be able to generate research projects.
    These proposals will be validated against a knowledge base of existing scientific papers in the field. 
    """

context2 = """purpose: the role of this agent will be to query the pubmed database to verify whether a research proposal has already been implemented or not.
    By comparing the potential research proposal to what has already been done in pubmed, it will be able to validate and propose a novel, original research proposal or on the 
    contrary refute and say that this research has already been done before. 
    This provised the other LLM with negative result, which it can respond upon by searching for new research proposals.
    """


prompt = """
    you are assisting a professor which needs to make new research proposals, please generate novel research projects based on the given context and verify that these are novel projects by looking your proposals in the already_researched tool. 
    """

