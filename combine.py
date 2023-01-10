import os

target_filename = 'combined.jsonl'

with open(target_filename, 'w') as target_file:
    for filename in os.listdir('.'):
        if filename.endswith('.jsonl') and filename != target_filename:
            with open(filename) as src_file:
                target_file.write(src_file.read())
            target_file.write('\n')
