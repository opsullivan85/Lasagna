import json
import os

#dirname = os.path.dirname(__file__)
settings_path = os.path.join(os.path.dirname(__file__), 'settings\\')


class printersettings:
    """ Manages printer settings

    """

    def __init__(self, path: str = None) -> None:
        """ Initializes a new PrinterSettings object

        Parameters
        ----------
        path : str, optional
            settings are loaded from here if included

        See Also
        --------
        PrinterSettings.load
        """
        self._settings = None
        if path is not None:
            self.load(path)

    def load(self, name: str) -> None:
        """ Loads settings from a file

        Parameters
        ----------
        name : str
            Filename to load settings from

        Returns
        -------
        None
        """
        with open(settings_path + name, 'r') as file:
            self._settings = json.load(file);

    def save(self, name: str = None) -> None:
        """ Saves settings to a file

        Parameters
        ----------
        name : str, optional
            Filename to save to. If not provided the printer name is used

        Returns
        -------
        None
        """

        if name is None:
            name = self._settings['Printer Name']

        assert name != 'defaultsettings', 'You cannot overwrite the default settings'

        with open(settings_path + name + '.json', 'w') as file:
            file.write(json.dumps(self._settings))

    def __str__(self):
        s = ''
        for key in self._settings.keys():
            s += key + ': ' + str(self._settings[key]) + '\n'
        return s

    def __getitem__(self, item):
        return self._settings[item]

    def __setitem__(self, key, value) -> None:
        self._settings[key] = value
