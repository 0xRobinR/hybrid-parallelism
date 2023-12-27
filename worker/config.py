import os
import json


MIN_WORKERS = 2
MAX_WORKERS = 10


worker_index = 1
os.environ['TF_CONFIG'] = json.dumps({
    'cluster': {
        'worker': ["localhost:12345", "localhost:23456"]
    },
    'task': {'type': 'worker', 'index': worker_index}
})



print(os.environ['TF_CONFIG'])