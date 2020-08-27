# The BashOperator

In order to execute bash commands in Apache Airflow, we will use the BashOperator.
By using this operator, we can execute any arbitrary bash command such as `mv`, `ls`, 
`echo`, `rm`, `sudo`, `pip`, etc.

In this example, we will define a Directed Acyclic Graph (DAG) with three task that
print different messages to the bash shell using `echo`. We will then define the
dependices between this three task to specify the order the task are executed. 
So open `bash_dag.py` with your favorite editor and let's go through the code
in detail.
