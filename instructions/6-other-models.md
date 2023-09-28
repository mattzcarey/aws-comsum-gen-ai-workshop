# 6. Using Other Models (Bonus Section)

## Local Models: GPT4ALL

Change the llm to use the [GPT4All model](https://python.langchain.com/docs/integrations/llms/gpt4all). You will need to download the model locally and performance will probably be quite bad locally.

## Cloud/AWS Deployment: Hugging Face

You will have to make an account on the website. Then add you access key and inference url to the .env file.

Change the ChatOpenAI over to [HuggingFaceHub](https://python.langchain.com/docs/integrations/llms/huggingface_hub) class and change the model name to the model you want to use. You can use GPT2 for free. Other fun models to try will be phi-1.5, Llama2.

You can easily deploy models to AWS with one click using the Hugging Face UX.
