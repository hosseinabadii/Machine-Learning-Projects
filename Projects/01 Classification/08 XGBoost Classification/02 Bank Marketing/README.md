# Bank Marketing Classification Project

The data is related with direct marketing campaigns of a Portuguese banking institution. The marketing campaigns were based on phone calls. Often, more than one contact to the same client was required, in order to access if the product (bank term deposit) would be ('yes') or not ('no') subscribed.

## Input variables:

### bank client data:

- `age` (numeric)
- `job` (categorical) - type of job:
    - "admin"
    - "unknown"
    - "unemployed"
    - "management"
    - "housemaid"
    - "entrepreneur"
    - "student"
    - "blue-collar"
    - "self-employed"
    - "retired"
    - "technician"
    - "services"
- `marital` (categorical) - marital status:
    - "married"
    - "divorced" (means divorced or widowed)
    - "single"
- `education` (categorical):
    - "unknown"
    - "secondary"
    - "primary"
    - "tertiary"
- `default` (binary: "yes","no") - has credit in default?
- `balance` (numeric) - average yearly balance, in euros
- `housing` (binary: "yes","no") - has housing loan?
- `loan` (binary: "yes","no") - has personal loan?

### related with the last contact of the current campaign:

- `contact` (categorical): contact communication type:
    - "telephone"
    - "cellular"
- `day_of_week` (numeric): last contact day of the week
- `month` (categorical): last contact month of year:
    - "mar"
    - "apr"
    - ...
    - "nov"
    - "dec"
- `duration` (numeric): last contact duration, in seconds

### other attributes:

- `campaign` (numeric) - number of contacts performed during this campaign and for this client (includes last contact)
- `pdays` (numeric) - number of days that passed by after the client was last contacted from a previous campaign (-1 means client was not previously contacted)
- `previous` (numeric) - number of contacts performed before this campaign and for this client
- `poutcome` (categorical) - outcome of the previous marketing campaign:
    - "nonexistent"
    - "failure"
    - "success"

## Output variable (desired target):

- `y` (binary: "yes","no") - has the client subscribed a term deposit?

## Source links

- [Notebook](https://github.com/liannewriting/YouTube-videos-public/blob/main/xgboost-python-tutorial-example/xgboost_python.ipynb)
- [Dataset](https://archive.ics.uci.edu/dataset/222/bank+marketing)