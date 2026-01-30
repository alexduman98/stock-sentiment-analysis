#File responsible for data, HOW moves
#check if directories exists
#one function to write dataFrame
#one function to read a dataFrame
#one function to append
#one function to dedupe

from pathlib import Path
from typing import Union , Optional, List 
import pandas as pd

#Union = allows to specify that a variable can be one of several types(int or str )
PathLike = Union[str, Path] #accepts a string or a PathObject 
def ensure_directories_exist(path:PathLike):
    p = Path(path) #p is now a Path object
    #folder that containts the data is the parent /data/processed
    #if the parrent directory does not exist create it 
    p.parent.mkdir(parents=True,exist_ok=True) 
    return p 

def write_parquet(df:pd.DataFrame, ):
    ensure_directories_exist()


