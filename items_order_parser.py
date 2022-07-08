import json
import requests
import file_operations as fop


def parse_orders(data):
    # variables
    data_dict = {}
    sellers = 0
    buyers = 0

    sell_prices = []
    buy_prices = []
    # sell_sum = 0
    # buy_sum = 0
    ##############

    # Get and parse JSON data
    api_data = requests.get(
        data["api_url"])

    json_data = json.loads(api_data.content)

    orders_list = json_data["payload"]["orders"]
    #############

    # parsing sellers or buyers that are ingame and getting set platinum price
    for item in orders_list:
        if(item["order_type"] == "sell" and item["user"]["status"] == "ingame"):
            sellers += 1
            sell_prices.append(item["platinum"])
        elif(item["order_type"] == "buy" and item["user"]["status"] == "ingame"):
            buyers += 1
            buy_prices.append(item["platinum"])
    ############

    # # summing up all the prices
    # for items in sell_prices:
    #     sell_sum += items
    # for items in buy_prices:
    #     buy_sum += items
    # ############

    # variables
    # avg_sell = sell_sum/sellers if sellers != 0 else 0
    # avg_buy = buy_sum/buyers if buyers != 0 else 0
    min_sell = sorted(sell_prices)[0] if len(sell_prices) != 0 else 0
    max_buy = sorted(buy_prices)[-1] if len(buy_prices) != 0 else 0
    median_price = (min_sell+max_buy)/2
    ############

    # Create dictionary
    data_dict["item_name"] = data["name"]
    data_dict["median_price"] = median_price
    data_dict["min_sell"] = min_sell
    data_dict["max_buy"] = max_buy
    # data_dict["avg_sell"] = round(avg_sell, 2)
    data_dict["sellers"] = sellers
    data_dict["buyers"] = buyers
    # data_dict["avg_buy"] = round(avg_buy, 2)
    data_dict["web_url"] = data["web_url"]

    print("\n%s item data parsed and processed." % (data["name"]))
    return data_dict


# parse_orders({'name': 'telos_akbolto', 'api_url': 'https://api.warframe.market/v1/items/telos_akbolto/orders',
#               'web_url': 'https://warframe.market/items/telos_akbolto'})

def RUN():
    items_data_output = []
    for items in fop.ReadFileData("files/parsed_item_urls.txt"):
        data = parse_orders(items)
        items_data_output.append(data)

    fop.WriteToFile("files/FINAL_OUTPUT.json",
                    json.dumps(items_data_output, indent=4))


# RUN()
