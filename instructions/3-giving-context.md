# 3. Supplying Context

LLMs only `know` data they were trained on. To give an LLM more data we can do one of 3 things:

1. Include data in the prompt directly
2. Use a vector search and get relevant context that way ([RAG](https://www.pinecone.io/learn/retrieval-augmented-generation/))
3. [Fine-tuning](https://platform.openai.com/docs/guides/fine-tuning) of the actual model itself (beyond the scope of this workshop but most useful for domain specific tasks).

## Modify the prompt

We can include data sources in the actual prompt. The LLM will have access to all the info and can sort through it. We can do this with small data sources up to the limit of the [context window](https://cobusgreyling.medium.com/what-does-the-openai-16k-context-window-mean-a0d2e10f7bfa).

Go to the `system prompt` and add the following to the end of the prompt before the Answer line:

`Use the context from the user to help answer the question: <Add some random fact here that the LLM can use>`

### Bonus task

Try to add more facts to the prompt. Maybe copy and paste a whole article. What happens to the answers from the chatbot? Do you get any errors? Keep adding more words until things get weird.

## RAG

Now we are going to do the fun stuff with RAG.

### Document Upload

1. Uncomment main.py lines 32-37. This enables the UX to upload files in the frontend.

### Document Loading

Check out the `llm/retriever.py` file. This does this:

1. Split the document into chunks.
2. Create embeddings for each split.
3. Store the embeddings in a vector store.

Read about RAG from the link above and try to understand what each of the pieces are doing in the `llm/retriever.py` file.

### Document Retrieval

Now we need to define a [Conversation Retrieval Chain](https://python.langchain.com/docs/use_cases/question_answering/how_to/chat_vector_db) in Langchain. This will allow us to perform RAG with alot of the processes setup out of the box by the Langchain Class.

Uncomment main.py line 46 and comment out the old basic chain line 44.

We need to give the chain some memory to store internal chain responses so uncomment main.py line 41.

### Use QA Chain

Uncomment line 67 in main.py to use the PrintRetrievalHandler callback handler. Langchain callbacks are a handy way to do things while the chain is running but are beyond the scope of this workshop.

Comment out main.py lines 71-73 and uncomment line 74 to call the QA chain.

## Try it out

You should now have a functioning personal assistant which can take your documents and answer questions.

Try it out and see how it works.

You may need to comment out line 61 in main.py to avoid some weird memory issues.

### Super Bonus

Modify the retriever.py file to allow to upload CSV or Text files. Or go crazy and use a web loader to scrape a webpage. Check out the loaders you can use [here](https://python.langchain.com/docs/modules/data_connection/document_loaders/).

Then modify line 33 in the main.py file to allow the user to select that file type in the doc uploader.

### Super Super Bonus

Make a code review tool which scrapes public github repos and allows you to ask questions about the code.

You can use this [loader](https://python.langchain.com/docs/integrations/document_loaders/git) to scrape the repos.

### Super Super Super Bonus

Make an agent which can search for answers on the internet. See an example repo [here](https://github.com/langchain-ai/streamlit-agent/blob/main/streamlit_agent/search_and_chat.py). Can you integrate it into your personal assistant?

## Next Steps

Everything from now on is a bonus and is run by you. Go as far with this as you would like. Have a look at 4. for improving the retrieval chain. Then have a look at 5. for improving the storage of vectors and 6. for modifying the LLM.
