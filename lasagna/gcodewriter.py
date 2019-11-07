import os

import numpy as np

gcode_path = os.path.join(os.path.dirname(__file__), 'output/')


def gcodewriter(data: np.ndarray, path: str, name: str, beginning: str = None, end: str = None) -> None:
    """ Converts path information to a format readable by 3D printers

    Parameters
    ----------
    data: (N, 5) np.ndarray
        Contains the data to be written to the gcode file. The array should have each move in the first
        axis and the second axis should have {x, y, z, e, v}. Unless v is changed it should be None.
    path: str
        The path to save the gcode file to
    name: str
        The name to save the file as
    beginning: str, optional
        a string to add to the beginning of the file
    end: str, optional
        a string to add to the end of the file


    Returns
    -------
    None
    """

    data = np.asarray(data, dtype='string_')

    with open(gcode_path + name + '.json', 'w') as file:
        file.write(data)


def path_to_gcode(data: np.ndarray, beginning: str = None, end: str = None) -> str:
    axis_letters = np.asarray([" X", " Y", " Z", " E"], dtype='string_')
    g1 = np.repeat(['G1'], data.shape[0])[:, None]
    new_line = np.repeat(['\n'], data.shape[0])[:, None]

    print(g1.shape)

    # Add X Y Z E before numbers
    data = np.char.add(axis_letters, data)

    # Add G1 to the beginning of every line
    data = np.concatenate((g1, data), axis=1)

    # Add newLine to the beginning of every line
    data = np.concatenate((data, new_line), axis=1)

    data = data.ravel()

    return beginning + ''.join(list(data)) + end
