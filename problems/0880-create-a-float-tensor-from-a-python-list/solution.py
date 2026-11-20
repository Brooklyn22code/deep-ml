import torch

def to_float_tensor(values):
    dim = 1
    try:
        dim = 2
        x = values[0][0]
    except TypeError:
        dim = 1

    float_tensor = []

    if dim == 1:
        
        for integer in values:
            float_tensor.append(float(integer))

    else:

        for list_of_int in values:
            l = []
            for integer in list_of_int:
                l.append(float(integer))
            float_tensor.append(l)


    return torch.tensor(float_tensor)
