import pandas
import sys
# Will need to update this when xlwt is deprecated


def RUN():
    read_json = pandas.read_json("files/FINAL_OUTPUT.json")

    read_json.to_excel(
        "files/FINAL_OUTPUT.xlsx", sheet_name="Warframe Vault Item Prices")


# RUN()

if sys.argv[1] == "run":
    print("Manual override: run recieved.")
    RUN()
    