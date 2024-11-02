Mid Term Calculator Project

Using Read-Evaluate-Print-Loop to continue running the application until user exits.
User can access menu commands to access the different operations, and they can also exit  the application. The plugins can be modified to add more functionality to the calculator.
User can add, subtract, multiply, and divide any 2 numeric values.

Workflows added for project to utilize GitHub actions. Environment variable is used in .env file locally for the development environment and to define the database username as root. Importing the dotenv in the main.py file is critical for managing sensitive information and configuration settings. This is generally use if you have an api key and secret key too, but for the purposes of this project those are not needed.

Logging system is using the logging.conf to establish the configuration for monitoring system actions like user inputs, results, or history manipulation. In main.py file, logger.info is used for displaying the actions of the program and the user. The logger.warning and logger.error both display a warning message for monitoring the user's input.

Pandas implemented for comprehensive data reading and writing to CSV files using DataFrames. User can load, save, or clear calculation history through menu commands.

Look Before You Leap (LBYL) is used to first check if the command the user inputted is valid and in the dictionary of commands then proceeds to evaluation the expression.

Easier to Ask for Forgiveness than Permission (EAFP) is used to attempt the calculation first and  then raise errors to catch exceptions of invalid number inputs and division by zero error.