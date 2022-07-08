import pandas
# Will need to update this when xlwt is deprecated


def RUN():
    read_json = pandas.read_json("files/FINAL_OUTPUT.json")

    read_json.to_excel(
        "files/FINAL_OUTPUT.xls", sheet_name="Warframe Vault Item Prices")
