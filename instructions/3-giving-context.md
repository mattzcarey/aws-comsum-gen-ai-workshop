# 3. Supplying Context

LLMs only `know` data they were trained on. To give an LLM more data we can do one of 3 things: include it in the LLM prompt directly, use a vector search and get relevant context that way ([RAG](<insert RAG link>)) or [fine-tuning](<inswert finetuning link here>) of the actual model itself.

## Modify the prompt

We can include data sources in the actual prompt. The LLM will have access to all the info and can sort through it. We can do this with small data sources up to the limit of the [context window](<insert context window article>).

Go to the `system prompt` and add the following to the end of the prompt before the Answer line:

`Use the context from the user to help answer the question: <Add some random fact here that the LLM can use>`

### Bonus task

Try to add more facts to the prompt. Maybe copy and paste a whole article. What happens to the answers from the chatbot? Do you get any errors?

## RAG

Now we are going to do the fun stuff with RAG.

### Document Upload

1. Uncomment main.py lines 32-37. This allows us to upload files in the frontend.

### Document Loading

1. Split the document into chunks.
2. Create embedings for each split.
3. Store the embeddings in a vector store.

This is all done in the `llm/retriever.py` file.

#### Bonus Task

Read about RAG and try to understand what is happening in the `llm/retriever.py` file.

### Document Retrieval

For this we need to define a Conversation Retrieval Chain in Langchain. Uncomment main.py line 46 and comment out the old basic chain line 44.

We need to give the chain some memory to store internal responses so uncomment main.py line 41.

### Super Bonus

Modify the retriever.py file to allow to upload CSV or Text files. Or go crazy and use a web loader to scrape a webpage.

Then modify the main.py file to allow the user to select that file type.

### Use QA Chain

Uncomment line 67 to use a custom helpful PrintRetrievalHandler callback handler. Langchain callbacks are a handy way to do things while the chain is running but are beyond the scope of this workshop.

Comment main.py lines 71-73 and uncomment line 74 to use the QA chain.

## Try it out

You should now have a functioning personal assistant.

Try it out and see how it works.

You may need to comment out line 61 in main.py to avoid some weird memory issues.

### Bonus Task

Modify the conversational retrieval chain to use a different chain_type. You can find out more about chain_types [here](https://python.langchain.com/docs/use_cases/question_answering/how_to/vector_db_qa#chain-type)

Note the difference in outputs. What is happening?

You can also modify the splitter for your particular document format.
