# Python Implementation of Descretization Algorithm
import math as m

# Bin class
class bin:
    def __init__(self, name_, values_):
        self.name = name_
        self.values = values_
        self.size = len(self.values)
        self.mean = float(sum(self.values)/self.size)
    def add_value(self, value):
        self.values.append(value)
        self.size += 1
        self.mean = float(sum(self.values)/self.size)
        
    def __lt__(self, other):
        return self.values < other.values
        
def create_bins(dim):
    list_of_bins = []
    i = 0
    j = 0
    dim.sort()
    # check for repeated values
    while j < len(dim):
        new_bin = bin(i, [dim[j]])
        while (j+1 < len(dim)) and (dim[j] == dim[j+1]):
            new_bin.add_value(dim[j+1])
            j += 1
        j += 1
        i += 1
        list_of_bins.append(new_bin)
    return list_of_bins

def find_merge(list_of_bins):
    index_1 = 0
    index_2 = 0
    min_mean = m.inf
    for i in range(0, len(list_of_bins)-1):
        for j in range(i+1, len(list_of_bins)):
            diff = abs(list_of_bins[i].mean - list_of_bins[j].mean)
            if diff < min_mean:
                index_1 = i
                index_2 = j
                min_mean = diff
    return index_1, index_2
                
          
def merge_bins(bin1, bin2):
    values = []
    values.extend(bin1.values)
    values.extend(bin2.values)
    name = min(bin1.name, bin2.name)
    merged_bin = bin(name, values)
    return merged_bin

def remove_bins(index_1, index_2, list_of_bins):
    list_of_bins.pop(max(index_1, index_2))
    list_of_bins.pop(min(index_1, index_2))
    return list_of_bins

def calculate_entropy(list_of_bins, N):
    summation = 0
    for bin_ in list_of_bins:
        summation += float(bin_.size / N) * m.log2(float(bin_.size / N))
    return -summation

def descret_manual():
    # automatic for ER values
    '''
    values = [0.166666667,0,0,0,0.285714286,0.058823529,0.714285714,
              0.428571429,0.142857143,1,0.428571429,1,0,0.470588235,
              0.571428571,0.857142857,0.571428571,0.75,0.875,0,
              0.428571429,0.857142857,0,0.857142857,1,0,1,1,0,1,1,0,
              0.285714286,0.857142857,0,0.571428571,0.857142857,0,0.5,
              1,0,1,0.857142857,0.428571429,0,0,0,0.9,0.5,1,0,0,0.833333333,
              0.857142857,0.857142857,1,1,0.714285714,1,1,1,1,0.833333333,1,1,
              1]
    n = len(values)
    min_bins = 2
    '''
    # Manual For user input
    values = []
    n = int(input("Enter number of elements: "))
    print("Manually enter your numbers . . .")
    for i in range(0, n):
        element = float(input())
        values.append(element)
    print(values)
    # prompt user for minimum number of bins
    min_bins = int(input("Enter minimum number of bins: "))
    entropy = []
    information_loss = []
    # create inital bins
    bins = create_bins(values)
    # keep merging bins until minimum number is reached or change in 
    # information loss begins to decrease
    while len(bins) > min_bins:
        i, j = find_merge(bins)
        merged_bin = merge_bins(bins[i], bins[j])
        bins = remove_bins(i, j, bins)
        bins.append(merged_bin)
        if len(entropy) == 0:
            entropy.append(calculate_entropy(bins, n))
            information_loss.append(0)
        elif len(entropy) == 1:
            entropy.append(calculate_entropy(bins, n))
            information_loss.append(abs(information_loss[0] - entropy[-1]))
        else:
            entropy.append(calculate_entropy(bins, n))
            information_loss.append(abs(information_loss[-1] - entropy[-1]))
            change =  abs(information_loss[-1] - information_loss[-2])
            change_prev = abs(information_loss[-2] - information_loss[-3])
            if change <= change_prev:
                print("Bins . . .")
                break
    i = 0
    bins.sort()
    for bin in bins:
        bin.name = i
        i += 1
    for bin in bins:
        print("Bin", bin.name)
        print("Values", bin.values)
        
descret_manual()
        
        
    
    