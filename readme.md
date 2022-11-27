# PyBank 

## Introduciton

Ths program print the the following things based on the input file. 
   * The total number of months included in the dataset
   * The net total amount of Profit/Losses over the entire period
   * The average of the changes in Profit/Losses over the entire period
   * The greatest increase in profits (date and amount) over the entire period
   * The greatest decrease in losses (date and amount) over the entire period

## The folder structure 

main.ipynb - this is the main python file. 

output_exporter.py - This fild contain the method to write output of the program. The reason that this function is moved to another module is to increase the code reusability. 

resource - the resources directory contain all data files required to execute the programm. 

## How to run the programm

In order to fun this program, is is required to provide the dasa sheet file path as the first parameter. 

## Code comments

For this project, the following commenting syntax has been used. 


```
def add(value1, value2):
    # Calculate the sum of value1 and value2.
    return value1 + value2
```

Reference: https://stackabuse.com/commenting-python-code/


## Output 

The output of this programmis located at ./out.txt. 

Furthermore, this programm prints the output in the console too. 

# PyRamen

PyRamen follows the same folder structures.

However, the custom module of the PyRamen is report_publisher. The reason for this is the purpose of the custom module of the PyRamen component is to publish the generated report.


## Run the program
To run this program, it is required to send the menu and sales data sheet file paths respectively. 
