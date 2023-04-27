
# Working with YouTube Data.

We will be building a Python Project where we will utilize the YouTube API to gather data from YouTube, load the data into a Pandas DataFrame, and visualize the data using the Seaborn Python Library.

## Section to be covered

- [Creating the Youtube API Key.](https://console.cloud.google.com/)
- Documentations for how to access the data.
- Build the project


## Documentation

**Creating API KEY**

- So the very first thing that we need to do is to create our api key. In order to do that you need to go to your browser and then just type google developer console now this will show you a website [Google developers console](https://console.cloud.google.com/). Just click on that and you will need to have a google account so if you do not have that then you will have to first create a google account once you have that account you can just sign into that account.

- Create project, post it is created, go to Library on the left pane, search for "YouTube data API" and click enable. This will enable us to use the youtube api in this particular project. 

- After enabling the API, the last step is to create the api key. To do this, go to the credentials section of the left pane and select "create" from the list of available options. The api key will just be created as we proceed. Your API Key is copyable.

**YouTube API Documentation**

- Google has provided a [documentation,](https://developers.google.com/youtube/v3) this should open the youtube data api documentation.

- The cost of the quota for api requests is what we need to concentrate on because every time you use the api, you have a quota and a daily limit on how many requests you can make. The costs associated with the various methods you call will also vary.
## Tech Stack

- **Language:** Python

- **API:** YouTube

- **Tools:** Jupyter Notebook
## Pre-Requisites

To run this project, you will need to first create a virtual environment.

If running on simple python, command for creating a virtual environment is 
```python
pip install virtualenv
python3.11 -m venv <virtual-environment-name>
```

If running on anaconda, command for creating a virtual environment is

```python
conda create --name <virtual-environment-name>
```

Update the following configurations in .config/config.json file.

`apiKey`
`channelIDList`

```json
{
    "apiKey" : "Your API KEY",
    "channelIDList" : ["Your channel ID List"]
}
```

You must adjust the below variables in accordance with your apiKey and channelIDList if you plan to continue using the Jupyter Notebook.

`apiKey`
`channelIDList`

```python
apiKey = 'Your API KEY'
channelIDList = ["Your channel ID List"]
```
## Python Packages

We just need one particular library to be installed that is google api python client

```python
  pip install --upgrade google-api-python-client
```
    
## Run Locally

Clone the project

```bash
  $ git clone https://github.com/methedjangoguy/YouTube-Data-Analysis.git
```

Go to the project directory

```bash
  $ cd /YouTube Data Analysis
```

Install required packages

```bash
  $ pip install -r requirements.txt
```

Run the Application

```bash
  python main.py
```

For Running the Jupyter Notebook

```bash
Enter the startup folder by typing $ cd /YouTube Data Analysis
Type jupyter notebook to launch the Jupyter Notebook App 
The notebook interface will appear in a new browser window or tab.
```
## Author

- [@methedjangoguy](https://github.com/methedjangoguy)

