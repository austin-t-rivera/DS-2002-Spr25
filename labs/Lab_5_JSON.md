# Lab 5 - JavaScript Object Notation (JSON)

## Part 0. Setup

1. If you have not already, fork this repository: [**https://github.com/austin-t-rivera/DS2002-json-practice/**](https://github.com/austin-t-rivera/DS2002-json-practice/)
2. Open your repository in either Google Cloud Shell or locally.
    - Use `git clone` to clone your repo locally to Google Cloud Shell; or
    - Use `git clone` to clone your repo locally to your laptop.
    - If you are familiar with GitPod or have a preference using something else, you are more than welcome! :)
3. Refer to documentation within that repository as needed, and follow the instructions closely below.
4. You will create two scripts for this lab, one `bash` and one `python`. Create a directory named `lab5` in your fork of `DS2002-json-practice`. Place your two scripts in that directory, add/commit/push them, **then submit the URL to your `lab5` directory within your repository for grading**.

<br>

## Part 1. Parse JSON with `jq` (2 Points)

Review the instructions for how to parse JSON with `jq` on [this page](https://github.com/austin-t-rivera/DS2002-json-practice/tree/main/jq). 

The NOAA manages an open, public API for tracking aviation weather data.  METAR data is a format for weather reporting that includes information on wind, visibility, runway visual range, and more.

The NOAA Aviation Weather API has built-in documentation (look who else uses FastAPI?) here: https://aviationweather.gov/data/api/#/

Retrieve data from this URL, which is for the KMCI (Kansas City) airport, output into JSON format, showing the last 12 hours, bound by a small geographic box:
```
curl -s "https://aviationweather.gov/api/data/metar?ids=KMCI&format=json&taf=false&hours=12&bbox=40%2C-90%2C45%2C-85" > aviation.json
```

Note that you need to wrap this URL in quotes when using `curl` from the command-line.

### Write a `bash` script that does the following:

1. Includes a shebang/hashbang.
2. Fetches the METAR data from the URL above.
3. Parses the data and pulls out the `receiptTime` value.
4. **Outputs** only the first six values to the screen.
   - There are many ways to do this, i.e. manually, using a loop, using a range, etc. Be creative!
6. Parses the data and pulls out each of the temperature.
7. **Outputs** the average temperature across the 12 hours.
8. Parses whether or not the `cloud` value is "CLR" meaning clear or something else.
9. **Outputs** a boolean response for if more than half of the last 12 hours were cloudy (i.e. not CLR).

Your script should output something like this with no more than 6 lines of date/times, the average temperature, and whether or not the last 12 hours were mostly cloudy:

```
"2025-03-03 03:00:14"
"2025-03-03 01:58:19"
"2025-03-03 01:02:06"
"2025-03-03 00:00:07"
"2025-03-02 22:58:21"
"2025-03-02 21:58:35"
"Average Temperature: 9.5"
"Mostly Cloudy: true"
```

<br>

## 2. Parse JSON with Python (3 Points)

0. This is where it may be easier to work in a Python notebook (i.e. `.ipynb`) within `JupyterLab` or `Google Collab`, so you can see your output regularly. IF YOU DO THIS, note that you will submitting a `.py` file, so once your code is working, please make sure to transfer the code over to a Python file for submitting.

1. Review the file [data/schacon.repos.json](https://github.com/austin-t-rivera/DS2002-json-practice/blob/0fc909adffe8b13aea33a59af90c38f978bca61d/data/schacon.repos.json) and notice it lists the first 30 repositories owned by Scott Chacon in GitHub. Each entry has around 100 data points.

2. Recall that reading a file into Python looks something like this (in read-only mode):

    ```
    import json
    
    with open('somefile.json', 'r') as file:
        data = json.load(file)
    ```

3. Write a Python script that does the following:
   
   1. Reads in the file as JSON.
   2. Pulls out the following four fields:
      1. `name`
      2. `html_url`
      3. `updated_at`
      4. `visibility`
   3. Assembles these four fields using ONE of these four methods:
      1. Append each comma-separated line; OR                          (HINT: using a `for loop`, `enumerate()`, and `f""`)
      2. Dictionary entry to then a pandas dataframe entry; OR         (HINT: using a `for loop`, `pd.DataFrame()`, and `to_csv`)
      3. Using json_normalize from the Pandas library                  (HINT: using `pd.json_normalize()` and `to_csv`)
   4. Appends/Exports **the first 5 lines only** to a new text file named `chacon.csv`

Your Python script should output into `chacon.csv` so that it looks exactly like this:

```
3D-Me,https://github.com/schacon/3D-Me,2014-04-10T21:53:58Z,public
aeon,https://github.com/schacon/aeon,2015-07-04T15:31:31Z,public
agitmemnon,https://github.com/schacon/agitmemnon,2019-07-14T17:02:27Z,public
agitmemnon-server,https://github.com/schacon/agitmemnon-server,2024-02-05T21:14:57Z,public
amp,https://github.com/schacon/amp,2017-06-29T22:21:55Z,public
```

**You will not be submitting your output data file, so make sure to delete it once you have confirmed it matches the above. It is bad practice to upload your output data onto GitHub. GitHub is meant for code, not for storing data. Yes, I am a hypocrit for having the data for Part 2 of the lab in the repo you fork. Hopefully one day UVA will have a centralized data repository for things like this.**

<br>

## 3. Submit your work

By this point, you should now have a bash file (.sh), a Python file (.py) living within your `lab5` directory. Make sure to add/commit/push your new script files to your main branch. On Canvas, you will submit the URL to your `lab5` directory within YOUR forked `DS2002-json-practice` repo.
