import os
from pathlib import Path
import json

FILE = Path(__file__).resolve()
ROOT = FILE.parents[1]
RANK = int(os.getenv('RANK', -1))
    
def update_options(request):

    if request.method == 'GET':
        source = request.args.get('source')
        save_txt = request.args.get('save_txt')

    if request.method == 'POST':
        json_data = request.get_json() 
        json_data = json.dumps(json_data)
        dict_data = json.loads(json_data)
        source = dict_data['source']
        save_txt = dict_data.get('save_txt', None)        
    
    return source, bool(save_txt)