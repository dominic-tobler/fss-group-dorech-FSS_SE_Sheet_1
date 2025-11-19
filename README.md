# fss-group-dorech-FSS_SE_Sheet_1

## Prerequisites
### Setting up the assignment environment
* Cloning the HuggingFace Transformers repo & checking out release tag v4.57.0: <br>
    From inside the assignment repo, I ran the following in the terminal:
    ```
    git clone https://github.com/huggingface/transformers.git
    cd transformers
    git checkout v4.57.0
    ```
* Creating a Python virtual environment: <br>
    To create a virtual environment using Python 3.12, each team member must run the following command in the root of the repo once (the .gitginore file ensures that the environment isn't pushed to github):
    ```
    python3.12 -m venv .venv
    ```
    Then, to active the virtual environment:
    ```
    (macOS/linux)   source .venv/bin/activate
    (PowerShell)    .\.venv\Scripts\Activate
    ```
    And to deactivate, run:
    ```
    deactivate
    ```
    Any packages that are installed while the virtual environment is activated will be installed inside the environment. They can be manually added to the ```requirements.txt``` file or added using the command (run in the directory root):
    ```
    pip freeze > requirements.txt
    ```
    To install packages from the ```requirements.txt``` file, run the followng while the virtual environment is activated:
    ```
    pip install -r requirements.txt
    ```

## Task 1: Defect Analysis


## Task 2: Complexity Analysis

## Task 3: Coupling Analysis