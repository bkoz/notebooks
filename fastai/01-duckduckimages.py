# Numpy and pandas by default assume a narrow screen - this fixes that
# from fastai.vision.all import *
# from nbdev.showdoc import *
# from ipywidgets import widgets
# from pandas.api.types import CategoricalDtype

# import matplotlib as mpl
# mpl.rcParams['figure.dpi']= 200
# mpl.rcParams['savefig.dpi']= 200
# mpl.rcParams['font.size']=12

# set_seed(42)
# torch.backends.cudnn.deterministic = True
# torch.backends.cudnn.benchmark = False
# pd.set_option('display.max_columns',999)
# np.set_printoptions(linewidth=200)
# torch.set_printoptions(linewidth=200)

# def get_image_files_sorted(path, recurse=True, folders=None): return get_image_files(path, recurse, folders).sorted()

# from fastbook import *

import requests
import re

def search_images_ddg(key,max_n=200):
     """Search for 'key' with DuckDuckGo and return a unique urls of 'max_n' images
        (Adopted from https://github.com/deepanprabhu/duckduckgo-images-api)
     """
     url        = 'https://duckduckgo.com/'
     params     = {'q':key}
     res        = requests.post(url,data=params)
     searchObj  = re.search(r'vqd=([\d-]+)\&',res.text)
     if not searchObj: print('Token Parsing Failed !'); return
     requestUrl = url + 'i.js'
     headers    = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0'}
     params     = (('l','us-en'),('o','json'),('q',key),('vqd',searchObj.group(1)),('f',',,,'),('p','1'),('v7exp','a'))
     urls       = []
     while True:
         try:
             res  = requests.get(requestUrl,headers=headers,params=params)
             data = json.loads(res.text)
             for obj in data['results']:
                 urls.append(obj['image'])
                 max_n = max_n - 1
                 if max_n < 1: return L(set(urls))     # dedupe
             if 'next' not in data: return L(set(urls))
             requestUrl = url + data['next']
         except:
             pass


urls = search_images_ddg('grizzly bear', max_n=100)
len(urls),urls[0]

