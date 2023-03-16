
import inspect
import pprint
pp = pprint.PrettyPrinter(indent=2)
import os


try:
    DBG_ATTRS = os.environ['DBG_ATTRS']
except Exception as e:
    DBG_ATTRS = False
try:
    DBG_ODICT = os.environ['DBG_ODICT']
except Exception as e:
    DBG_ODICT = False

doc = f"""
You can change setup OS Envrionment like below :

1. export DBG_ATTRS=True/False
    - Debug an object's attributes.
2. export DBG_ODICT=True/False
    - Debug an object's __dict__.

Default setup values are :

DBG_ATTRS={DBG_ATTRS}\nDBG_ODICT={DBG_ODICT}
"""

def print_dict(d):
    whoami = f"{'-'*50} {__name__} | {inspect.stack()[0][3]}"
    if isinstance(d, dict):
        print(whoami)
        pp.pprint(d)
    else:
        print(f"{whoami}\n Given d ({d}) is not 'dict'.")

def attrs(obj):
    try:
        os.environ['DBG_ATTRS']
    except Exception as e:
        print(f"{'#'*50} {__name__} | {inspect.stack()[0][3]}\nException : {e}\nGuide :{doc}")
        pass
    else:
        if os.environ['DBG_ATTRS']:
            for attr in dir(obj):
                v = getattr(obj, attr)
                if isinstance(v, dict):
                    print(f"{'-'*50} {attr}\n type : {type(v)}")
                    print_dict(d=v)
                else:
                    print(f"{'-'*50} {attr}\n value : {v}\n type : {type(v)}")

def odict(obj):
    try:
        os.environ['DBG_ODICT']
    except Exception as e:
        print(f"Exception : {e}\nGuide :{doc}")
        pass
    else:
        if os.environ['DBG_ODICT']:
            whoami = f"{'-'*50} {__name__} | {inspect.stack()[0][3]}"
            if hasattr(obj, '__dict__'):
                for k,v in obj.__dict__.items():
                    if isinstance(v, dict):
                        print(f"{whoami}")
                        print_dict(d=v)
                    else:
                        print(f"{whoami}\n{k} : {v}")
            else:
                print(f"{whoami}\n Given obj ({obj}) does not have '__dict__'.")

def cframe(cf):
    odict(obj=cf)
    attrs(obj=cf)
