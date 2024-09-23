# Setup

1. Clone the repository.
2. Run the setup script to create the virtual environment and install dependencies.

If using PowerShell, run:
`cmd /c setup.bat`

If using a regular terminal, run:
`setup.bat`

This command will do the following:
- Create a virtual environment in the `venv` directory.
- Activate the virtual environment.
- Install the dependencies listed in `requirements.txt`. (pygame is a dependency)

3. Run the start script to start the game.

If using PowerShell, run:
`cmd /c start.bat`

If using a regular terminal, run:
`start.bat`

## Virtual Environment
This project utilizes a virtual environment to manage dependencies. The virtual environment is located in the `venv` directory. To activate the virtual environment, run the following command:
`activate`

To deactivate the virtual environment and return to the normal environment, run the following command:
`deactivate`