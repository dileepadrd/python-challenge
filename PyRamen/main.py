# -----------------------------------------------------------
# PyBank
#
#  This programm calculate the following values
#   1. Load the data into menus and sales arrays
#   2. Analyse the data and do the calculations
#   3. Validate the data
#   4. Write the output in a out file
#
# (C) 2022 Dileep Dharmasiri, Toronto, Canada
# email dileepadrd@gmail.com
# -----------------------------------------------------------

# importing required libraries
import sys
import os.path
import csv
import report_publisher


class Sale:
    # Sale class contasin all fileds of a sale
    item_id = 0
    date = ""
    credit_card = ""
    quantity = 0
    menu_item = ""


menus = []
sales = []
report = {}


def is_valid_file(file_name):
    # is_valid_file check whether the given file is valid or not
    # @param file_name = the file name to be tested
    return os.path.exists(file_name)


def load_data(menu_file, sales_file):
    # process_file function open the data file and iterate through all menu lines and the sale lines
    # and load the data
    # If there is any error while processing the file, thsi function returns False
    # If the file has been processed succsssfully, this function returns True

    global menus
    global sales

    menus = csv_to_arr(menu_file)

    item_id_index = 0
    date_index = 1
    credit_card_index = 2
    quantity_index = 3
    menu_item_index = 4

    sales_arr = csv_to_arr(sales_file)
    for sale in sales_arr:
        if not is_int(sale[quantity_index]):
            print("invalid value in the data sheet")
            return False

        sale_object = Sale()
        sale_object.item_id = sale[item_id_index]
        sale_object.date = sale[date_index]
        sale_object.credit_card = sale[credit_card_index]
        sale_object.quantity = int(sale[quantity_index])
        sale_object.menu_item = sale[menu_item_index]
        sales.append(sale_object)

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


def csv_to_arr(file_path):
    # This function converts a csv file into an array of row
    # If there is any error occurs, this function returns False
    # Otherwise this returns the array which contains the all rows of the csv file

    arr = []

    # check the file exists or not
    # if the file does not exist, return the function with a error
    if not is_valid_file(file_path):
        print(f"invalid file - {file_path}")
        return False

    # check the file exists or not
    # if the file does not exist, return the function with a error
    if not is_valid_file(file_path):
        print(f"invalid file - {file_path}")
        return False

    # open the file to process
    with open(file_path) as file:
        reader = csv.reader(file, delimiter=',')
        # skipping the header
        next(reader)

        for row in reader:
            arr.append(row)

    return arr


def process_data():
    # process_data function process the data and do the calculations
    # it iterates through all sales and menus and generate the report dict

    # getting the global variables
    global sales
    global menus

    for sale in sales:
        quantity = sale.quantity
        menu_item = sale.menu_item

        if menu_item not in report:
            report[menu_item] = {
                "01-count": 0,
                "02-revenue": 0,
                "03-cogs": 0,
                "04-profit": 0,
                "05-number-of-records": 0,
            }

        item_index = 0
        price_index = 3
        cost_index = 4
        for menu in menus:
            item = menu[item_index]
            if not is_int(menu[price_index]):
                print("invalid menu price")

            price = int(menu[price_index])

            if not is_int(menu[cost_index]):
                print("invalid const in the menu data sheet")

            cost = int(menu[cost_index])

            if item == menu_item:
                report[item]["01-count"] += quantity
                report[item]["02-revenue"] += price * quantity
                report[item]["03-cogs"] += cost * quantity
                report[item]["04-profit"] += (price - cost) * quantity
                report[item]["05-number-of-records"] += 1
                break
    #        else:
    #            print(f"{menu_item} does not equal {item}! NO MATCH!")

    return True


def export_report():
    # export the report
    # write the report into a output file
    try:
        report_publisher.publish_report(report)
    except OSError:
        print("Error while publishing the report")
        return False

    return True


def main():
    # This is the main function of the programm
    # This function is called as the fist step

    # variable declaration
    menu_file = ""
    sales_file = ""

    # check whether the there are required number of command line args
    if len(sys.argv) < 3:
        sales_file = "resources/sales_data.csv"
        menu_file = "resources/menu_data.csv"
    else:
        # getting the file name from the command line args
        menu_file = sys.argv[1]
        sales_file = sys.argv[2]

    # check the file is valid or not
    if not is_valid_file(menu_file):
        print(f"unable to find file - {menu_file}")
        return

    # check the file is valid or not
    if not is_valid_file(sales_file):
        print(f"unable to find file - {sales_file}")
        return

    if not load_data(menu_file, sales_file):
        print("Error while processing the file.")
        return

    if not process_data():
        print("Error while data processing.")
        return

    if not export_report():
        print("exporting report error")
        return


# calling the main function
main()