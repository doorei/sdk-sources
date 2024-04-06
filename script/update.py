import json
import os
import glob

input_dir = 'external'
output_dir = 'current'

for file_path in glob.glob(os.path.join(input_dir, '*.json')):
  classified_data = {
          "windows": [],
          "linux": [],
          "darwin": []
  }
  with open(file_path, 'r') as f:
    data = json.load(f)
    for k,v in data.items():
          print(k)
          for vv in v:
            o = vv["Os"]
            if o in classified_data:
                del vv["Extra"]
                classified_data[o].append(vv)
  base_name = os.path.basename(file_path)
  output_file_name = base_name.replace('.version.json', '.json')
 
  output_file_path = os.path.join(output_dir, output_file_name)
  print(output_file_path)
  with open(output_file_path, 'w') as f:
    json.dump(classified_data, f)
