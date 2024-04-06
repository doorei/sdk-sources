import json
import os
import glob

input_dir = 'external'
output_dir = 'current'

for file_path in glob.glob(os.path.join(input_dir, '*.json')):
  classified_data = {
          "windows": {},
          "linux": {},
          "darwin": {}
  }
  with open(file_path, 'r') as f:
    data = json.load(f)
    for k,v in data.items():
          version_data = {
          "windows": [],
          "linux": [],
          "darwin": []
          }
          if k.startswith('v'):
            k = k.lstrip('v')
          for vv in v:
            o = vv["Os"]
            if o in version_data:
                del vv["Extra"]
                version_data[o].append(vv)
          if version_data['windows']:
            classified_data['windows'][k] = version_data['windows']
          if version_data['linux']:
            classified_data['linux'][k] = version_data['linux']
          if version_data['darwin']:
            classified_data['darwin'][k] = version_data['darwin']
  base_name = os.path.basename(file_path)
  output_file_name = base_name.replace('.version.json', '.json')
 
  output_file_path = os.path.join(output_dir, output_file_name)
  print(output_file_path)
  with open(output_file_path, 'w') as f:
    json.dump(classified_data, f)
