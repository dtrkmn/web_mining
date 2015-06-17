import json
import codecs

input_file  = file("episode.json", "r")

output_file = codecs.open("episode1.json", "w", encoding="utf-8")
j = json.loads(input_file.read().decode("utf-8-sig"))
json.dump(j, output_file, indent=4, sort_keys=True, ensure_ascii=False)


input_file  = file("oyuncular.json", "r")

output_file = codecs.open("oyuncular1.json", "w", encoding="utf-8")
j = json.loads(input_file.read().decode("utf-8-sig"))
json.dump(j, output_file, indent=4, sort_keys=True, ensure_ascii=False)

input_file  = file("anasayfa.json", "r")

output_file = codecs.open("anasayfa1.json", "w", encoding="utf-8")
j = json.loads(input_file.read().decode("utf-8-sig"))
json.dump(j, output_file, indent=4, sort_keys=True, ensure_ascii=False)
