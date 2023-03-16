
import os
current_filepath = os.path.abspath(__file__)
PJT_PATH = os.path.dirname(os.path.dirname(current_filepath))
print(f" Current-filepath : {current_filepath}\n PJT_PATH : {PJT_PATH}")
import sys
sys.path.append(f"{PJT_PATH}/env/lib/python3.7/site-packages")
