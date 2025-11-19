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
#### Use Git to extract all the commit messages after 2023-01-01.
<i>Note: The cutoff date is chosen for computational reasons and will be used for the rest of the tasks as well!</i>

```

```
#### Analyze these messages to detect the presence of specific keywords of your choice related to defect fixes.

#### Calculate and plot the number of defects per month for the two files with the highest number of defects. 
* In which month were the most defects introduced?

* How would you explain it?

* Manually examine the repository for that month (e.g. change logs, releases, commit messages) and come up with a hypothesis. 

#### What are the limitations of this method for finding defective hotspots?

## Task 2: Complexity Analysis
#### Select two complexity metrics of your choice. 

#### Calculate the complexity of all .py files in the repository using the selected metrics.

#### Visualize the complexity hotspots. The visualization should effectively convey which parts of the code are more complex or change more frequently. Feel free to use any visualization of your choice and explain the rationale behind your decision. 

#### What can you say about the correlation between the two complexity measures in this repository? 
<i>For example, if you selected CC and LoC, what can you say for the statement "Files with more lines of code tend to have higher cyclomatic complexity"?</i>

#### A colleague of yours claims that "Files with higher complexity tend to be more defective". What evidence can you present to support or reject this claim for the selected complexity measures in this repository?

## Task 3: Coupling Analysis

#### Calculate the logical coupling for each file pair in this repository. Visualize the 10 most coupled file pairs using a visualization of your choice that effectively conveys the coupling relationships. Select one of these 10 most coupled file pairs and comment on their relationship. 

#### Repeat the steps of the task above, but consider only file pairs where one file is a Python test file (i.e. starts with "test_") and the other is a Python non-test file. How would you explain this type of coupling? Is it a code smell that requires attention and signals potential refactoring opportunities or is it something different?

#### Writing tests is a time-consuming task and developers often omit it, thus, automated test generation tools have been implemented and are widely used. One of the most popular test generation tools for Python is Pynguin, that takes as input a .py file and generates passing tests for that file. Pynguin writes the generated tests to a new file in a separate folder, isolated from the project’s test suite. Suppose that you are tasked with implementing an option for Pynguin to place the tests directly in the project’s test suite, specifically in the test file that is most closely “related” with the input .py file. Discuss at least three (3) methods for selecting the most “related” test file given a (non-test) .py file. You do not have to implement these methods at this stage.

#### Select two of the three test placement methods you proposed above and implement them in Python. The implementation should take one non-test .py file and return one test_*.py file. Where would the two methods place automatically-generated tests for src/transformers/generation/utils.py?