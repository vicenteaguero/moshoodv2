# Refactoring Jupyter Notebook into modular code

This repository shows a notebook. The goal is to refactor it into modular code by thinking about how to split the code into scripts and each script into functions. Remember to think of the [base working guidelines](https://docs.google.com/document/d/12a6RzFVADjZ1CWfNUQOVFGaW6Dmsqb6KwgbHH1MfHKg/edit#heading=h.hzmv5aaafu8b) and for guidance on the structure check out the [template project](https://git.opendfki.de/dssgxdfki/dssg23-template-project)!



## How to install dependencies

Create a new virtual environment with your favorite tool (conda, pyenv virtualenv, etc.) and activate it.
Then, install the dependencies with pip:

```bash
pip install -r requirements.txt
```

## How to run the notebook

After installing the dependencies, you can add your virtual environment to Jupyter:

```bash
python -m ipykernel install --user --name=your-env-name
```

Then, you can run the notebook (or go to VS Code and run it from there):

```bash
jupyter notebook
```

