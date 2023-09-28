# System prompt

The system prompt is what is sent to the large language model (LLM) before the user question. It normally defines some ground rules for how the LLM will behave.

Things like language choice, format and writing style should be defined here.

### Bonus task

Do a little google about recent advancements in system prompts. DeepMind released a study this month where they found huge improvements by prefixing prompts with one unlikely sentence. What was it?

## a. Speak like a pirate

In `demo/prompts/system_prompt` you will find the system prompt.

Modify the prompt so that your chatbot returns text in the style of a pirate.

Now try get the model to impersonate William Shakespeare.

## b. Randomise the welcome message

The `demo/prompts/welcome_message` defines the welcome message. This makes a nice UX and and also helps define the writing style of the model.

Finish the build_welcome_message function to return one of the supplied mesages at random. 

### Super Bonus

Get the LLM to generate the first message when the app first load. 

## Next Steps
Go to 3.
