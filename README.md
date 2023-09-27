# AWS Comsum GenAI Workshop

> Workshop to build a personal assistant with Langchain, Streamlit and AWS

## Project requirements

### Pyenv and `Python 3.11.4` (Optional but highly recommended)

- Install [pyenv](https://github.com/pyenv/pyenv) to manage your Python versions and virtual environments:

  ```bash
  curl -sSL https://pyenv.run | bash
  ```

  - If you are on MacOS and experiencing errors on python install with pyenv, follow this [comment](https://github.com/pyenv/pyenv/issues/1740#issuecomment-738749988)
  - Add these lines to your `~/.bashrc` or `~/.zshrc` to be able to activate `pyenv virtualenv`:
    ```bash
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"
    eval "$(pyenv init --path)"
    ```
  - Restart your shell

- Install the right version of `Python` with `pyenv`:
  ```bash
  pyenv install 3.11.4
  ```

### Poetry

- Install [Poetry](https://python-poetry.org) to manage your dependencies and tooling configs:
  ```bash
  curl -sSL https://install.python-poetry.org | python - --version 1.5.1
  ```
  _If you have not previously installed any Python version, you may need to set your global Python version before installing Poetry:_
  ```bash
  pyenv global 3.11.4
  ```

## Installation

### Create a virtual environment

Create your virtual environment and link it to your project folder:

```bash
pyenv virtualenv 3.11.4 aws-comsum-gen-ai-workshop
pyenv local aws-comsum-gen-ai-workshop
```

Now, every time you are in your project directory your virtualenv will be activated thanks to `pyenv`!

### Install Python dependencies through poetry

```bash
poetry install --no-root
```

## Formatting and static analysis

### Code formatting with `black` (Optional)

To check code formatting, run `black` with:

```bash
black . --check
```

or

```bash
make black
```

You can also [integrate it to your IDE](https://black.readthedocs.io/en/stable/integrations/editors.html) to reformat
your code each time you save a file.

### Static analysis with `ruff` (Optional)

To run static analysis, run `ruff` with:

```bash
ruff check src tests
```

or

```bash
make ruff
```

To run static analysis and to apply auto-fixes, run `ruff` with:

```bash
make fix-ruff
```

### Type checking with `mypy`

To type check your code, run `mypy` with:

```bash
mypy src --explicit-package-bases --namespace-packages
```

or

```bash
make mypy
```

## Streamlit

The project includes a Streamlit app.

This is where you will build your personal assistant.

## Next Steps

Please insure you have set up a virtual environment and installed the dependencies before moving on.

Continue the workshop by navigating to `instructions/1-running-the-app.md`
