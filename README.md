# Python Dropbox File Uploader

This repository contains a Python script for uploading files to Dropbox using the Dropbox API.

## Getting Started

Clone this repository to your local machine

```
git clone https://github.com/rekanos/python-dropbox-file-uploader.git
```

## Prerequisites

Before we dive into the Python script, make sure you have the following:

1. A Dropbox account
2. Python installed on your machine: Download and install Python from [python.org](https://www.python.org/).

## Create an App on Dropbox

To create an app on Dropbox, go to [Dropbox Developer Apps](https://www.dropbox.com/login?cont=https%3A%2F%2Fwww.dropbox.com%2Fdevelopers%2Fapps).

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/2aj6xjnl4b50ipykiqj5.png)

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/3x5j1r2jzxy61uxx7we6.png)

After creating an app you have an **App key**, **App secret** please keep it secret, and generate **Access Token**” by click on Generate button.

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/gxtfy9sm6cs4a6ub961v.png)

After generating **Access Token** now go to permissions section and set the required permissions.

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/p6rtl7vqrcr5zsx3jtyj.png)

## Setting Up the Project

To get started, create a new Python script and install the necessary packages. Open your terminal or command prompt and run the following commands:

```
pip install dropbox
pip install requests
pip install configparser
pip install pybase64
pip install jsonlib
```

## Obtaining Access Code

Open **get_access_code.py** file, replace **APP_KEY** with your Dropbox **App key**. This code will open a browser window prompting you to log in to your Dropbox account and authorize access for your app. After authorization, Dropbox will redirect you to a URL containing the access code.

**Run the Script:** Save the Python script and execute it by running the following command in your terminal or command prompt:

```
python get_access_code.py
```

**Authorize Dropbox Access:** Follow the prompts in your browser to log in to your Dropbox account and authorize access for your app. Once authorized, you will be redirected to a page displaying the access code.

**Copy the Access Code:** Copy the access code from the browser window. We'll use this access code in our Python script to authenticate with Dropbox's API.

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ax3p09025immpkr2voye.png)

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/6md3jxlerg6bus4q2o4j.png)

## Obtaining Refresh Token

Run **get_refresh_token.py** python file, replace **<APP_KEY>**, **<APP_SECRET>**, and **<ACCESS_CODE_GENERATED>** with your Dropbox app key, app secret, and the access code obtained in the previous step.

```
python get_refresh_token.py
```

the output is

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/6kbznp05npdwr0dwnqbk.png)

With the refresh token obtained, we can now proceed to integrate it into our Python script for uploading files to Dropbox.

## Creating Credentials Configuration File

To securely store your Dropbox app's credentials and tokens, we'll create a configuration file named **credentials.ini**.

Open your preferred text editor and create a new file named credentials.ini. Copy the following content into the credentials.ini file:

```
[Authentication]
access_token = <ACCESS_TOKEN>
app_key = <APP_KEY>
app_secret = <APP_SECRET>
refresh_token = <REFRESH_TOKEN>
```

Replace **<ACCESS_TOKEN>**, **<APP_KEY>**, **<APP_SECRET>**, and **<REFRESH_TOKEN>** with the corresponding values:

- **ACCESS_TOKEN:** Your Dropbox app's generated access token.
- **APP_KEY:** Your Dropbox app key.
- **APP_SECRET:** Your Dropbox app secret.
- **REFRESH_TOKEN:** The refresh token obtained from the **get_refresh_token.py** script.

Save the credentials.ini file in the same directory as your Python scripts.

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/hguht2wuytfqk9z9smfp.png)

## Upload Files to Dropbox

Now that your Python script is ready, you can run it to upload a file to your Dropbox account. Execute the following command in your terminal or command prompt:

```
python main.py
```
