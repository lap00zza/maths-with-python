# Using python for Maths

This repository contains a bunch of programs to help with learning how use
python for Maths. The programs are aimed at students from Grades 7 to 12.

## How do I run these programs?

* Clone this repository
* Make sure python is setup in your system
* run the program as follows:

  ```sh
  cd maths-with-python

  # create a new virutal environment if this is the first time
  python3 -m venv "venv"

  # Active the virtual environment
  # this will change for other shells
  # Windows PS C:\> <venv>\Scripts\Activate.ps1
  source venv/bin/activate.fish

  # install the required packages
  pip install -r requirements.txt

  # run the programs
  python3 program_name.py

  # when you are done, deactive the virtual environment
  deactivate
  ```
