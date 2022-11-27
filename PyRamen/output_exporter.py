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

def export_output(months, total, average, max_profit, max_profit_month,
                  min_profit, min_profit_month):
    # write_output function write the output into the ./out.txt file
    # if there is any errors occurred during the file writting process, there would be an error printed and return
    # This function not only write the output into the file but it also prints the results.

    out = "Financial Analysis\n"
    out += "----------------------------\n"
    out += "Total Months: " + str(months) + "\n"
    out += "Total: $" + str(total) + "\n"
    out += "Average  Change: $" + str(average) + "\n"
    out += "Greatest Increase in Profits: " + max_profit_month
    out += "($" + str(max_profit) + ")\n"
    out += "Greatest Decrease in Profits: " + min_profit_month
    out += "($" + str(min_profit) + ")\n"

    # printing the output into the console
    print(out)

    # writing the output into file
    # please note that the 'a' in the followign function call parameter indicates that we are going to append to the file
    # so if the file already exists the output will be added to the file
    file = open("./out.txt", "a")
    file.write(out)
    file.close()

