# Introduction

In this example, we will define a Directed Acyclic Graph (DAG) with three task that
print different messages to the bash shell using bash `echo` command. We will then define the
dependices between this three task to specify the order the task are executed. 
So open `bash_dag.py` with your favorite editor and let's go through the code
in detail.

Notice that `bash_dag.py` is broken into the following sections:

1. [Importing Libraries]()
2. [Setting Default Variables]()
3. [Define DAG]()

Let this discuss this in further detail below

## Importing Libraries

In this section we import all the packages we need to create our DAG.

```python
###############################################################################
#                          1. Importing Libraries                             #
###############################################################################
import datetime as dt 
from airflow import DAG # Use to create an instance of the DAG object
from airflow.operators.bash_operator import BashOperator # Use to create task that run bash commands
```

As you can see, we import `datetime`, `DAG`, and `BashOperator`.
The `DAG` class will be used to create an instance of a `DAG` object. Inside the `DAG` instance,
we can add task using Operators. In this case, we will use the `BashOperator` to 
create task that run bash commands. 


## Setting Default Values
We will now define a dictionary that will used to set some of the parameters
of the DAG instance that will be created in the next section.

```python
###############################################################################
#                        2. Setting Default Variables                         #
###############################################################################
default_args = {
        'owner': 'airflow',
        'description': 'A DAG that runs bash commands',
        'start_date': dt.datetime(2018, 1, 1),
        'concurrency': 1,
        'retries': 3
}
```

Let's discuss the contents of this dictionary:

* `owner`: (str) - the owner of the DAG
* `description`:(str) - this is a string describing the DAG
* `start_date`: (datetime.datetime) – the timestamp from which the scheduler will attempt to backfill
* `concurrency`: (int) – the number of task instances allowed to run concurrently
* `retries`: (int) – the number of retries that should be performed before failing the task