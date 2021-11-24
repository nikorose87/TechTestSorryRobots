import json
from main import resfun

list_ = []

def lambda_handler(event, context):
    res = resfun(event, list_)
    return res.result()
