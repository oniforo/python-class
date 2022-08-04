# Programming

A repository for storing every code proposed in the Programming and Machine Learning class.

## Installation

Start a virtual environment, activate it, clone the repository and install the packages in the requirements.txt file using venv's [pip](https://pip.pypa.io/en/stable/) package manager.

### Windows PowerShell

Create a virtual environment.

```powershell
python -m venv virtualenv
```

A directory called virtualenv should be created. Within it, scripts to activate the virtual environment. Now, activate it.

```powershell
cd virtualenv
./Scripts/Activate.ps1
```

On Windows, it may be required to enable this Activate.ps1 script by setting the
execution policy for the user. You can do this by issuing the following PowerShell command.

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

If properly activated you should see the name of the virtual environment in parentheses in the command line. Now, commands such as ```python``` and ```pip``` will be run using the executables from the virtual environment, meaning they're isolated.

Download the files to the current directory.

```bash
git clone https://github.com/oniforo/python-class.git
```

Use virtual environment's pip to download the packages in the ```requirements.txt``` file. Remember to check for the cue indicating environment's activation, such as below.

```bash
(virtualenv) pip install -r requirements.txt
```

If you intend to use Jupyter, the python kernel needs to be configured. The next section explains how. If not, the configuration is done.

### Jupyter

Assuming installation was successful using ```requirements.txt``` file, ipykernel should be installed. To add the virtual environment to Jupyter and, consequently, have access to the packages downloaded inside it, run the following.

```bash
(virtualenv) python -m ipykernel install --name=virtualenv
```

After that, the virtual environment should be available in the kernel dropdown on the Jupyter GUI.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate (to be implemented)

## License
[MIT](https://choosealicense.com/licenses/mit/)