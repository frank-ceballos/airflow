""" ***************************************************************************
# * File Description:                                                         *
# * An example of a Directed Acyclic Graph (DAG) that shows an example on     *
# * how to use the PythonOperator. The PythonOperator is used to execute      *
# * Python code. In this example, we import a Python function define elsewhere*
# * and feed into the PythonOperator to define a task. Use the PythonOperator *
# * to execute any arbitrary Python function.                                 *
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
from airflow.operators.python_operator import PythonOperator # Use to create tasks that run Python code

# Get Python Functions
from scripts import create_data
from scripts import clean_data


###############################################################################
#                        2. Setting Default Variables                         #
###############################################################################
default_args = {
        'owner': 'airflow',
        'description': 'A DAG that executes Python code',
        'start_date': dt.datetime(2018, 1, 1),
        'concurrency': 1,
        'retries': 0
}


###############################################################################
#                                3. Define DAG                                #
###############################################################################
with DAG('db-maintance', schedule_interval = '@daily', catchup = False, default_args = default_args) as dag:

        # -------- First Define Task -------- #

        # Here we define a task using the PythonOperator to execute a Python function
        create_data = PythonOperator(task_id="create=data", python_callable = create_data.main)

        # Another Python related task
        clean_data = PythonOperator(task_id="clean_data", python_callable = clean_data.main)


        # -------- Adding Dependencies -------- #
        
        create_data >> clean_date

