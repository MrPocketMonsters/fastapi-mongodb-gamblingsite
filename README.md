# Simple REST API service with FastAPI and MongoDB

This is my first time using FastAPI and MongoDB. With this project, I aim to understand and have a first approach to these tools. It will also help as a first approach to documentation for a project.

## What's up with the "Gambling" thing?

The proposed system was that of a Database API Service for a Gambling site that allows:
* Create and edit users with
    * Name
    * Age
    * Balance
    * Bet History
* Manage Sports Event Information
* Adding and removing funds
* Check of funds before moving them
* Query open events and selecting bet type
* Logic for processing results and solving open bets moving funds
* Personal statistics endpoint
    * Winning bets percentage
    * Total won bets
    * Total lost bets
    * Most common type of events

## How to install this project

This project runs on [Python 3.11.10](https://www.python.org/downloads/release/python-31110/), so the first thing is getting it.

1. Navigate to the desired containing folder using the terminal.
2. Clone this project using `git clone https://github.com/MrPocketMonsters/fastapi-mongodb-gamblingsite.git`.
A new folder `/fastapi-mongodb-gamblingsite` with the project will be created.
3. Navigate to the project folder using `cd fastapi-mongodb-gamblingsite`.
4. Install all required Python libraries using `pip install -r requirements.txt`.
This will install on your PC:
    * The official MongoDB Python client.
    * The FastAPI library for RestAPIs.
    * The Uvicorn Web Server.
    * Dependencies for these libraries.

## Environment Variables

This project was made using the MongoDB cloud service *Atlas*. The `envvar-example` file contains an `export` instruction for the variable `MONGODB_URI`, which is an URI that grants access to some database running MongoDB.
1. Copy the `envvar-example` file to `envvar`.
The `envvar` file is ignored by Git.
2. Replace the value for the `MONGODB_URI` variable with a valid URI that grants access to some MongoDB database.

## Running the Project

To run the project on localhost, on port 8000, use the `source envvar` command to load the environment variables to the current terminal session, then use the command `uvicorn main:app --reload`. A new process will then start running on `http://127.0.0.1:8000`.
