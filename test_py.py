import numpy as np

def test_py():
    a = np.array([[0, 1], [2, 3]], order='C')
    a.resize((2, 1))
