# 3. Supplying Context

LLMs only `know` data they were trained on. To give an LLM more data we can do one of 3 things: include it in the LLM prompt directly, use a vector search and get relevant context that way ([RAG](<insert RAG link>)) or [fine-tuning](<inswert finetuning link here>) of the actual model itself.

## Modify the prompt

We can include data sources in the actual prompt. The LLM will have access to all the info and can sort through it. We can do this with small data sources up to the limit of the [context window](<insert context window article>).

Go to the `main`
