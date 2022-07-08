import json
import file_operations

txt_file = file_operations.ReadFileData("FINAL_OUTPUT.txt")

json_convert = json.dumps(txt_file, indent=4)

file_operations.WriteToFile("FINAL_OUTPUT.json", json_convert)
