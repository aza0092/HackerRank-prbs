
import os
import sys
from datetime import datetime


#
# Complete the timeConversion function below.
#
def timeConversion(s):
    dt=datetime.strptime(s, '%I:%M:%S%p')
    return(dt.strftime('%H:%M:%S'))

'''
INPUT:
07:05:45PM
'''