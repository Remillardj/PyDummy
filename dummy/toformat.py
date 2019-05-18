#!/usr/local/bin/python3

# Verify the length of each element in a 2D array
def verify_array(row):
    len00 = len(row[0])
    i = 0
    len0 = len(row)
    while (i < len0):
        leni = len(row[i])
        if (leni != len00):
            print("Index %d does not match Index 0" % i)
            return False
        return True

# Write to a file
def write_to_file(data = [], statement=False, filename="insert.sql"):
    if (statement):
        with open(filename, "a") as file:
            file.write(statement)
    else:
        with open(filename, "a") as file:
            for insert in data:
                file.write(insert + "\n")

def sql_delete_query(table, column, pk, filename="delete.sql"):
    return ("DELETE FROM `" + table + "` WHERE " + column + "=" + pk + ";")

def sql_insert_query_multiprocessing(table, columns, values):
    insertQuery = []
    print (columns)
    print (len(values))

def sql_insert_query(table, columns=[], values=[]):
    insertQuery = []
    numCol = len(columns)
    numValues = len(values)
    if (numValues < numCol):
        print ("Why is there more values than columns? Returning false you silly goose.")
        return False
    
    if (verify_array(values)):
        # Length of row already verified
        len00 = len(values[0]) #5
        i = 0
        while (i < len00):
            insert = "INSERT INTO `" + table + "` ("
            for col in columns[:-1]:
                insert += "`" + col + "`, "
            insert += "`" + columns[-1] + "`"
            insert += ") VALUES ("
            c = 0
            while (c < numValues):
                if ( c == (numValues-1)):
                    insert += "`" + values[c][i] + "`"
                    break
                insert += "`" + values[c][i] + "`, "
                c += 1
            insert += ");"
            insertQuery.append(insert)
            i += 1
        write_to_file(insertQuery)

# Eventually...
def to_json(output, delete=False):
    if (delete):
        pass
    else:
        pass