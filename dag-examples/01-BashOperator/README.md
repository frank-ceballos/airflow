# Introduction

In this example, we will define a Directed Acyclic Graph (DAG) with three task that
print different messages to the bash shell using bash `echo` command. We will then define the
dependices between this three task to specify the order the task are executed. 
So open `bash_dag.py` with your favorite editor and let's go through the code
in detail.

Notice that `bash_dag.py` is broken into the following sections:

1. Importing Libraries
2. Setting Default Variables
3. Define DAG 

We will discuss this in further detail below

# Importing Libraries


```python {.line-numbers}
import datetime as dt 
from airflow import DAG # Use to create an instance of the DAG object
from airflow.operators.bash_operator import BashOperator # Use to create task that run bash commands
```