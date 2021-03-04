# robo-advisor
## Installation

***Credit to Prof Rossetti's "Robo Advisor" Read Me File for the setup information

For this remote repository under your own control, then "clone" or download your remote copy ont your local computer. Choose a familiar download location so that it is easy to find.

After cloning the repo, navigate there from the command-line. The following commands assume that you are running the commands from the local repository's root directory:

```sh
cd robo-advisor
```

Create and activate a new Anaconda virtual environment. You can call it stocks-env

```sh
conda create -n stocks-env python=3.8
conda activate stocks-env
```

Within the virtual environment, install the package dependencies

```sh
pip install -r requirements.txt
```

## Setup

This program will need an API Key to issue request to the AlphaVantage API {https://www.alphavantage.co/}

The program's source could should not include the secret API Key value so you need to set an environment variable called ALPHAVANTAGE_API_KEY, and your program should read the API Key from this environment variable at run-time

In the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file to include your API Key value

```sh
#robo-advisor/.env

ALPHAVANTAGE_API_KEY="Your API Key Value Here"
```

## Usage

Within the virtual environment, demonstrate your ability to run the Python script from the command-line:

```sh
python app/robo_advisor.py
```
