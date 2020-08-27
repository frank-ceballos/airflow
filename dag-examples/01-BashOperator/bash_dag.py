""" ***************************************************************************
# * File Description:                                                         *
# * An example of a Directed Acyclic Graph (DAG) that shows an example on how *
# * to use the BashOperator. The BashOperator is used to execute arbitrary    *
# * bash commands. In this example, we define three task using the            *
# * the BashOperator. Each task prints a message to the terminal.             *
# *                                                                           *
# * The contents of this script are:                                          *
# * 1. Importing Libraries                                                    *
# * 2. Setting Default Variables                                              *
# * 3. Define DAG                                                             *
# *                                                                           *
# * --------------------------------------------------------------------------*
# * AUTHORS(S): Frank Ceballos <frank.ceballos123@gmail.com>                  *
# * --------------------------------------------------------------------------*
# * DATE CREATED: 8/26/2020                                                   *
# * --------------------------------------------------------------------------*
# * NOTES: None                                                               *
# * ************************************************************************"""


###############################################################################
#                          1. Importing Libraries                             #
###############################################################################
import datetime as dt 
from airflow import DAG # Use to create an instance of the DAG object
from airflow.operators.bash_operator import BashOperator # Use to create task that run bash commands


###############################################################################
#                        2. Setting Default Variables                         #
###############################################################################
default_args = {
        'owner': 'airflow',
        'description': 'A DAG that runs bash commands',
        'start_date': dt.datetime(2018, 1, 1),
        'concurrency': 1,
        'retries': 0
}


###############################################################################
#                                3. Define DAG                                #
###############################################################################
with DAG('hello-world!', schedule_interval = '@daily', catchup = False, default_args = default_args) as dag:

        # -------- First Define Task -------- #

        # Here we define a task using the BashOperator to execute a bash_command
        task_hello = BashOperator(task_id='hello-world', bash_command='echo "Hello World!"')

        # Here we define another task using the BashOperator to execute a bash command
        task_bye = BashOperator(task_id='bye-world!', bash_command='echo "Bye Bye World!"')

        # A third task that executes a bash command
        task_eat = BashOperator(task_id='bye-world!', bash_command='echo "Eat Tacos"')

        # -------- Adding Dependencies -------- #
        # For example, we will first execute task_hello, followed by task_eat, and finally task_bye
        task_hello >> task_bye >> task_eat