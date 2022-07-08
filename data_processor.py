
import re
import file_operations as fop


def process_vault_data(data):
    processed_data = []

    for items in data:
        # print(items)
        if(items.find("Conclave") != -1 or items.find("Prime") == -1):
            # print("%s removed from raw data." % items)
            pass
        else:
            processed_data.append(items)

    # print("Processed data: %s" % processed_data)
    fop.WriteToFile("files/processed_vault_data.txt", processed_data)


def regex_process(data):
    regex_data = []
    for items in data:
        prime_filter = re.match('(.+?)(\s|\\/)Prime', items)
        regex_data.append(prime_filter.group(1))
        # print(prime_filter.group(1))

    fop.WriteToFile("files/regex_vault_data.txt", regex_data)


def RUN():
    process_vault_data(fop.ReadFileData("files/raw_vault_data.txt"))
    regex_process(fop.ReadFileData("files/processed_vault_data.txt"))
