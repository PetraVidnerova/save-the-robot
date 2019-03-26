import os
import numpy as np

def read_result_file(fname):
    with open(fname) as file:
        lines = file.readlines()
        
        centroid_line = lines[1]
        centroid = centroid_line.strip().split(',')
        centroid = list(map(float, centroid))

        result = 1 if len(lines) > 2 else 0

    return centroid, result
    

def load_data(data_dir="data"):

    dir_names = [ directory.name for directory in os.scandir(data_dir) if directory.is_dir() ] 
    array_names = [ f"{data_dir}/{name}/{name}_array.txt" for name in dir_names ]
    result_names = [ f"{data_dir}/{name}/{name}.dat" for name in dir_names ]


    # Load X: screenshot numpy arrays 
    x_list = [] 
    for name in array_names:
        x = np.loadtxt(name, delimiter=",")
        x = x[..., np.newaxis]
        x_list.append(x)
    X = np.stack(x_list)

    # normalize 
    X -= np.min(X)
    X /= np.max(X)

    print("Loaded X of shape:", X.shape)

    
    # Load C and y: selected centroids and results
    c_list, y_list = [], [] 
    for name in result_names:
        centroid, y = read_result_file(name)
        c_list.append(np.array(centroid))
        y_list.append(y)
    C = np.stack(c_list)
    Y = np.stack(y_list)

    # normalize 
    C -= np.min(C)
    C /= np.max(C)


    print("Loaded C of shape:", C.shape)
    print("Loaded Y of shape:", Y.shape)
    
    return X, C, Y
