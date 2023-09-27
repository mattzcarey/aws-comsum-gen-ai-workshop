from demo.constants.settings import SETTINGS

"""
Configure the LLM Chain to use for this personal assistant.
"""

# Configure LLM to use
llm = ChatOpenAI(
    openai_api_key=SETTINGS.openai_api_key.get_secret_value(),
    model=SETTINGS.model,  # type: ignore
)


#LLM Chain 
llm_chain = LLMChain()

#Conversational Revieval Chain. 


