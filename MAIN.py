from pandas import ExcelFile
import web_parser
import data_processor
import all_items_parser
import items_order_parser
import excel_generator


def MAIN():
    print("\nWARFRAME VAULT ITEM PRICE ANALYZER")
    print("\n==================================")
    print("\nPROGRAM STARTED...")
    web_parser.RUN()
    print("\nVaulted items webpage parsed.")
    data_processor.RUN()
    print("\nProcessed raw vault data.")
    all_items_parser.RUN()
    print("\nExtracted vault items data from all items.")
    items_order_parser.RUN()
    print("\nGenerated FINAL data per item.")
    excel_generator.RUN()
    print("\nExcel file generated.")
    print("\nEND")


MAIN()
