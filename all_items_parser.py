
import json
import file_operations as fop

items_file = open("files/all_items.json")

items_json = json.load(items_file)

items_data = items_json["payload"]["items"]


def get_vaulted_item_url(data):
    item_url_names = []
    for name in data:
        for item in items_data:
            if(item["item_name"].find(name) != -1):
                item_url_names.append(item["url_name"])

    fop.WriteToFile("files/item_url_names.txt", item_url_names)
    # print(item_url_names)


def generate_urls_data(data):
    # reference api url: "https://api.warframe.market/v1/items/chroma_prime_set/orders"
    # reference web url: "https://warframe.market/items/ember_prime_set"
    generated_urls = []
    for item in data:
        url_dict = {}
        combined_api_url = "https://api.warframe.market/v1/items/%s/orders" % item
        combined_web_url = "https://warframe.market/items/%s" % item
        url_dict["name"] = item
        url_dict["api_url"] = combined_api_url
        url_dict["web_url"] = combined_web_url
        generated_urls.append(url_dict)

    fop.WriteToFile("files/parsed_item_urls.txt", generated_urls)


def RUN():
    get_vaulted_item_url(fop.ReadFileData("files/regex_vault_data.txt"))
    generate_urls_data(fop.ReadFileData("files/item_url_names.txt"))
