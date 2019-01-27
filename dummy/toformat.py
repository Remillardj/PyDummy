#!/usr/local/bin/python3

def write_to_file(data = [], filename="data.sql"):
    with open(filename, "a") as file:
        for insert in data:
            file.write(insert)

def sql_delete_query(table, column, pk):
    return ("DELETE FROM `" + table + "` WHERE " + column + "=" + pk + ";")

def sql_insert_query(table, columns=[], values=[]):
    insertQuery = []
    numCol = len(columns)
    numValues = len(values)
    if (numValues < numCol):
        print ("Why is there more values than columns? Returning this you silly goose.")
        return False
    x = 0
    while (x < numValues):
        i = 0
        insert = "INSERT INTO `" + table + "` ("
        for v in columns:
            insert += "`" + v + "`, "
        insert += ") VALUES ("
        while (i < numCol):
            for _ in range(numCol):
                insert += "`" + values[x] + "`, "
                x += 1
                i += 1
        insert += ");"
        insertQuery.append(insert)
    write_to_file(insertQuery)

# Create insert statements by default
def to_sql(output, delete=False):
    if (delete):
        pass
    else:
        pass

def to_json(output, delete=False):
    if (delete):
        pass
    else:
        pass