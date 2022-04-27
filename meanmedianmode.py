from collections import Counter
import csv
def mean(total_weight,total_entries):
     mean=total_weight/total_entries
     print(mean)

def getmedian(total_entries,sorted_data):
    if total_entries%2==0:
        median1=float(sorted_data[total_entries//2])
        median2=float(sorted_data[total_entries//-1])
        median=(median1+median2)/2
    else:
        median=float(sorted_data[total_entries//2])
    print(median)
def mode(sorted_data):
    data=Counter(sorted_data)
    range={"75-85":0,
    "85-95":0,"95-105":0,"105-115":0,"115-125":0,"125-135":0,"135-145":0,"145-155":0,"155-165":0,"165-175":0}