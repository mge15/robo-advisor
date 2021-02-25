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
