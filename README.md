# RepoGrader
---
This is a simple script that was made for our final seminar in Advanced Software Engineering.

* **DatasetGenerator.py** creates our dataset using Github API, and inserts it into a CSV file.

* **DatasetCombiner.py** is used to combine between two CSV files. This was used to collect our dataset in different parts, because running our program for too long with the Github API resulted in crashes.

* **Grader.py** is the main script. It gives a grade for each repository and test the correlation between the grade and the number of forks that the repo recieved.

To use this script for yourself, you should first generate a personal ghp token to access the Github API. The one that is provided in the code is out of date.
