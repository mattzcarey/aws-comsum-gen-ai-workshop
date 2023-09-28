# 5. Vector stores (Bonus Section)

When the file is uploaded, we currently save the embeddings in an in memory vector store with ChromaDB.

This is not persistent across sessions or multiple users. Lets change that.

## Bonus: Pinecone

Make a pinecone account and use the pinecone vector store. You will need to change the vector store in the retriever.py file.

Follow the instructions in the [docs](https://python.langchain.com/docs/integrations/vectorstores/pinecone) to set up the vector store.

## Super Bonus: PGVector

You can store embeddings in any postgres db which suports pgvector. Have a go at using Aurora Serverless DB as a vector store. You will need your own AWS Account.

Otherwise use Supabase. They have a great free tier.

