#!/usr/bin/env python3
import dataMovies
import os
from dotenv import load_dotenv
import json

load_dotenv()

base_url = os.getenv('BASE_URL')
image_format = os.getenv('IMAGE_FORMAT')
metadata_output_path = os.getenv('METADATA_OUTPUT_PATH')

reader = open(os.getenv('RAW_ATTRIBUTES_PATH'))
raw_attributes = json.load(reader)
reader.close

for index, attribute in enumerate(raw_attributes):
    metadata = {}
    index_padded = f'{index:04}'
    metadata['name'] = 'Pizza! #'+index_padded
    metadata['image'] = base_url + index_padded + image_format
    metadata['description'] = 'One of the many pizzas waiting for you you to eat it! (Spoiler: it is delicious)'
    metadata['attributes'] = json.loads(attribute)
    metadata_output_file_path = metadata_output_path + index_padded + '.json'
    with open(metadata_output_file_path, 'w', encoding='utf-8') as writer:
        # json.dump(metadata, w)
        writer.write(json.dumps(json.dumps(metadata), ensure_ascii=False, indent=4))
    writer.close()
    print(metadata)
