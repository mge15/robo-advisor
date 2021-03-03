# robo-advisor
## Repo Setup

***Credit to Prof Rossetti's "Robo Advisor" Read Me File for the setup information

Use the GitHub online interface to create a new remote project repository called "robo-advisor". When prompted add a "README.md" file and a Python-flavored ".gitignore" file during the repo creation process. After this process is complete, you should be able to view the repo on GitHub.com at an address like https://github.com/YOUR_USERNAME/robo-advisor.

After creating the remote repo, use GitHub Desktop software or the command-line to "clone" it onto your computer. Choose a familiar download location.

After cloning the repo, navigate there from the command-line:

```sh
cd ~/Desktop/robo-advisor
```

Using your text editor or the command-line, create a new sub-directory called "app" with a file called "robo_advisor.py", and then place the following example print statements inside:

```sh
# this is the "app/robo_advisor.py" file

print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print("LATEST DAY: 2018-02-20")
print("LATEST CLOSE: $100,000.00")
print("RECENT HIGH: $101,000.00")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")
```

Using your text editor or the command-line, create a new file called "requirements.txt" in the root director of your repository and then place the following inside:

```sh
requests
python-dotenv
```

## Environment Setup

Create and activate a new Anaconda virtual environment

```sh
conda create -n stocks-env python=3.8 # (first time only)
conda activate stocks-env
```

Within the virtual environment, install the required packages in the "requirements.txt" file you created

```sh
pip install -r requirements.txt
```

Within the virtual environment, demonstrate your ability to run the Python script from the command-line:

```sh
python app/robo_advisor.py
```

If you see the example output i.e. the print statements we put inside robo_advisor.py earlier, then you are ready to move on to project development

## Security Requirements

This program will need an API Key to issue request to the AlphaVantage API {https://www.alphavantage.co/}

The program's source could should not include the secret API Key value so you need to set an environment variable called ALPHAVANTAGE_API_KEY, and your program should read the API Key from this environment variable at run-time

We are going to be using the dotenv Package to do this. First, install the package

```sh
pip install python-dotenv # note: NOT just "dotenv"
```

Second, create a file in your director named ".env" and place the following contents inside

```sh
#robo-advisor/.env

ALPHAVANTAGE_API_KEY=" "
```

Next, use the link above to get your free API key. Copy the key and paste it in the quotation marks in the .env file

In robo_advisor.py, add the following code

```sh
import os
from dotenv import load_dotenv

load_dotenv() #> loads contents of the .env file into the script's environment

api_key = os.environ.get("ALPHAVANTAGE_API_KEY") # reads the variable from the environment
# puts the key into a variable that can be used in your code
```

You will also need to ignore ".env" files from version control. To do this, create a file in the "robo-advisor" directory named ".gitignore" and place inside the following contents:

```sh
# robo-advisor/.gitignore

# ignore the ".env" file:
.env
```
