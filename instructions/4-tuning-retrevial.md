# 4. Tuning Retrieval

## Chain types

Modify the conversational retrieval chain to use a different chain_type. You can find out more about chain_types [here](https://python.langchain.com/docs/use_cases/question_answering/how_to/vector_db_qa#chain-type)

Note the difference in outputs. What is happening?

## Splitter and Chunking

You can also modify the splitter for your particular document format. Super interesting and can get much better retrieval results. See this doc for more info on splitters [here](https://python.langchain.com/docs/use_cases/question_answering/how_to/document-context-aware-QA)

## Embeddings Models

Up to now we have been using OpenAI embeddings. You can find a good leaderboard on embeddings [here](https://huggingface.co/spaces/mteb/leaderboard).

Try use using this example:

`embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")`
