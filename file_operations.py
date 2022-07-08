import os


def WriteToFile(filename, data):  # Writes text data to file

    with open(os.path.join(os.getcwd(), filename), "w+", encoding="utf-8") as file:
        file.write(str(data))
        print("Data written to ", filename, ".\n")


def ReadFileData(name):  # Reads file and returns as the respective data type
    with open(name, "r") as file:
        fileData = eval(file.read())
    return fileData
