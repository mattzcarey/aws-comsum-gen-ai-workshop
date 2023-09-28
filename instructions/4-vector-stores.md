# 4. Vector stores (this is a bonus)

## In Memory Chroma DB

When the file is uploaded, we currently save the embeddings in an in memory vector store with ChromaDB.

This is not persistent across sessions or multiple users. 

# Bonus: Pinecone

Make a pinecone account and use the pinecone vector store. You will need to change the vector store in the retriever.py file.

## Super Bonus: Supabase Vector Store 

You can store embeddings in any postgres db which suports pgvector. Have a go with Supabase. 

## Super Bonus: Aurora Serverless Vector Store

Lets go AWS and use Aurora. 