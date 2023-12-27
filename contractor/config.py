import os
import json


MIN_WORKERS = 2
MAX_WORKERS = 10


os.environ['TF_CONFIG'] = json.dumps({
    'cluster': {
        'worker': ["localhost:12345", "localhost:23456"]
    },
    'task': {'type': 'worker', 'index': 0}
})


print(os.environ['TF_CONFIG'])