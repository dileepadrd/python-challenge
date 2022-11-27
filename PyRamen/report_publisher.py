# -----------------------------------------------------------
# PyRamen
# To write putput into a file
# The report publisher converts the given dictionary to a string and writes it
# It writes to both stdout and output files
# (C) 2022 Dileep Dharmasiri, Toronto, Canada
# email dileepadrd@gmail.com
# -----------------------------------------------------------


def publish_report(data):
    # publish_report function write the output into the ./out.txt file

    out = ""
    for key in data:
        val = data[key]
        out += key + " " + str(val) + "\n"

    # printing the output into the console
    print(out)

    # writing the output into file
    # please note that the 'a' in the followign function call parameter indicates that we are going to append to the file
    # so if the file already exists the output will be added to the file
    file = open("./out.txt", "a")
    file.write(out)
    file.close()

    return True
