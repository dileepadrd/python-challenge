# -----------------------------------------------------------
# PyBank
#
#  This programm calculate the following values
#   1. The total number of months included in the dataset
#   2. The net total amount of Profit/Losses over the entire period
#   3. The average of the changes in Profit/Losses over the entire period
#   4. The greatest increase in profits (date and amount) over the entire period
#   5. The greatest decrease in losses (date and amount) over the entire period
#
# (C) 2022 Dileep Dharmasiri, Toronto, Canada
# email dileepadrd@gmail.com
# -----------------------------------------------------------

# importing required libraries
import sys
import os.path
import csv
import output_exporter


def is_valid_file(file_name):
    # is_valid_file check whether the given file is valid or not
    # @param file_name = the file name to be tested
    return os.path.exists(file_name)


def process_file(file_name):
    # process_file function open the data file and iterate through all line
    # and do the calculations
    # If there is any error while processing the file, thsi function returns False
    # If the file has been processed succsssfully, this function returns True

    # declaring variables
    months = 0
    total = 0
    max_profit = 0
    max_profit_month = ""
    min_profit = 0
    min_profit_month = ""

    # check the file exists or not
    # if the file does not exist, return the function with a error
    if not is_valid_file(file_name):
        print(f"invalid file - {file_name}")
        return False

    # open the file to process
    with open(file_name) as file:
        reader = csv.reader(file, delimiter=',')
        header = next(reader)

        month_index = header.index('Date')
        if month_index < 0:
            print("Unable to find 'Date' colum in the data sheet")
            return False

        profit_index = header.index('Profit/Losses')
        if profit_index < 0:
            print("Unable to find 'Profit/Losses' in the data sheet")
            return False

        for row in reader:
            profit_str = row[profit_index]

            if profit_str == "":  # check whether the profiel is empty in the data sheet
                print(f"empty profit in index {months} in the data sheet")
                return False

            # check whether the profit is a valid integer
            if not is_int(profit_str):
                print(f"invalid value format in the data sheet - {profit_str}")

            profit = int(profit_str)

            month = row[month_index]
            if month == "":  # to check whether the month is an empty string
                print(f"empty month name in index {months} in the data sheet")
                return False

            months += 1  # calculating the total months
            total += profit  # calculating the total profit

            if profit > max_profit:  # getting the max profit
                max_profit = profit
                max_profit_month = month
            elif profit < min_profit:  # getting the miminum profit
                min_profit = profit
                min_profit_month = month

    average = round(total / months, 2)  # calculating the average

    # writing the output into the file
    # output_exporter is a custom module which is implemented specifically for this program
    # plus, this custom module could be reused in the future to get the same functionalities.
    try:
        output_exporter.export_output(months, total, average, max_profit,
                                      max_profit_month, min_profit,
                                      min_profit_month)
    except OSError:  # This part is executed if there is any error while writing the file
        print("Unable to write to the file")
        return False

    return True


def is_int(val):
    # To check whether the value is valid integer or not
    # if this is valid int, return True
    # otherwise, this returns False
    try:
        int(val)
    except ValueError:
        return False

    return True


def main():
    # This is the main function of the programm
    # This function is called as the fist step

    # check whether the there are required number of command line args
    if len(sys.argv) == 1:
        print("Please enter the data file name as the fist argument")
        return

    # getting the file name from the command line args
    file_name = sys.argv[1]

    # check the file is valid or not
    if not is_valid_file(file_name):
        print(f"unable to find file - {file_name}")
        return

    if not process_file(file_name):
        print("Error while processing the file.")


# calling the main function
main()