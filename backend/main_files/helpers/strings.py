# By
# ████████╗██╗   ██╗ █████╗ ███╗   ██╗    ██╗  ██╗ ██████╗ 
# ╚══██╔══╝██║   ██║██╔══██╗████╗  ██║    ██║  ██║██╔═══██╗
#    ██║   ██║   ██║███████║██╔██╗ ██║    ███████║██║   ██║
#    ██║   ██║   ██║██╔══██║██║╚██╗██║    ██╔══██║██║   ██║
#    ██║   ╚██████╔╝██║  ██║██║ ╚████║    ██║  ██║╚██████╔╝
#    ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝    ╚═╝  ╚═╝ ╚═════╝ 

# Email: ttuan.ho@outlook.com                                                         

import re
import time, datetime
from main_files.exceptions import InvalidTypeError
import pytest

def checkDBType(input, type='str', strLength=None):
    if strLength != None and (not isinstance(strLength, int)):
        raise ValueError(f"Invalid type of {strLength}")
    if type(input) == 'int' and str(type) == 'int':
        return True
    if type(input) == 'str' and str(type) == 'str':
        return len(input) <= strLength
    
if __name__ == '__main__':
    with pytest.raises(InvalidTypeError, match='*'):
        checkDBType('asfds', strLength='asfsdf')



