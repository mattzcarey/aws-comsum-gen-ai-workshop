# 1. Running the app

The `demo` folder contains all the code for the project.

[Streamlit](https://streamlit.io/) is a framework for writing quick apps in Python.

That makes it perfect for building our personal assistant.

## Set up env variables

Copy the .env_example file to .env

Replace the OpenAI API key with your own.

If you don't have one you can get it [here](https://platform.openai.com/).

Leave the other variables as is for the moment.

## Running the Streamlit app

To run the Streamlit app, run the following command from the root of the project:

```bash
PYTHONPATH=. streamlit run demo/main.py
```

## Use the app

If all has gone well you will now be able to navigate to `http://localhost:8501` and see your very own chatbot.

Try and ask it some questions.

Is it connected to the internet?

How up to date is it's knowledge?

## Next Steps

In these instructions, `Bonus` section are fun little challenges. `Super Bonus` sections are much more challenging and will require some googling. You can skip them if you like and come back later.
