import numpy as np

def calculate(list):

  #change the shape of the list to a 3 x 3 matrix
  try:
    matrix = np.array(list).reshape(3, 3)

  #create the dictionary that holds the calculations
    calculations = {
      'mean': [],
    'variance': [], 
    'standard deviation': [], 
    'max': [], 
    'min': [], 
    'sum': []
    }

    #calculate the mean for axis1, axis2 & flattened matrix
    calculations['mean'].append(np.mean(matrix, axis = 0).tolist())
    calculations['mean'].append(np.mean(matrix, axis = 1).tolist())
    calculations['mean'].append(np.mean(matrix.flatten()).tolist())

    #calculate the variance for axis1, axis2 & flattened matrix
    calculations['variance'].append(np.var(matrix, axis = 0).tolist())
    calculations['variance'].append(np.var(matrix, axis = 1).tolist())
    calculations['variance'].append(np.var(matrix.flatten()).tolist())

    #calculate the standard deviation for axis1, axis2 & flattened matrix
    calculations['standard deviation'].append(np.std(matrix, axis = 0).tolist())
    calculations['standard deviation'].append(np.std(matrix, axis = 1).tolist())
    calculations['standard deviation'].append(np.std(matrix.flatten()).tolist())

    #calculate the min for axis1, axis2 & flattened matrix
    calculations['min'].append(np.amin(matrix, axis = 0).tolist())
    calculations['min'].append(np.amin(matrix, axis = 1).tolist())
    calculations['min'].append(np.amin(matrix.flatten()).tolist())

    #calculate the max for axis1, axis2 & flattened matrix
    calculations['max'].append(np.amax(matrix, axis = 0).tolist())
    calculations['max'].append(np.amax(matrix, axis = 1).tolist())
    calculations['max'].append(np.amax(matrix.flatten()).tolist())

    #calculate the sum for axis1, axis2 & flattened matrix
    calculations['sum'].append(np.sum(matrix, axis = 0).tolist())
    calculations['sum'].append(np.sum(matrix, axis = 1).tolist())
    calculations['sum'].append(np.sum(matrix.flatten()).tolist())

    return calculations

  #add a custom message if the list doesn't have nine elements.
  except ValueError:
    raise ValueError("List must contain nine numbers.") 