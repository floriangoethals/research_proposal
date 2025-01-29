context = """purpose: the primary role of this agent is to assist professors in the generation of scientific research proposals. 
    By analysing existing research papers in a similar field, the agent will be able to generate research projects.
    These proposals will be validated against a knowledge base of existing scientific papers in the field. 
    """

context2 = """purpose: the role of this agent will be to query the pubmed database to verify whether a research proposal has already been implemented or not.
    By comparing the potential research proposal to what has already been done in pubmed, it will be able to validate and propose a novel, original research proposal or on the 
    contrary refute and say that this research has already been done before. 
    This provised the other LLM with negative result, which it can respond upon by searching for new research proposals.
    """


prompt = """
    propose new research projects based on the current context. validate these research projects against what has already been done in the field. The field you should be focusing on can be found using the research_context tool. My field of reseaerch is coronary heart disease. Please validate that it's original research and that it has not been done before. 
    """


# another Sia project that might be nice to try:
#   generate business proposals based on what has already been done, then try to validate these with what's already in the database. 