# RepoGrader
---
This is a simple script that was made for my final seminar in Advanced Software Engineering.

* **DatasetGenerator.py** creates our dataset using Github API, and inserts it into a CSV file.

* **DatasetCombiner.py** is used to combine between two CSV files. This was used to collect our dataset in different parts, because Github didnt't allow us access to it's API for more than an hour at a time.

* **Grader.py** is the main script. It gives a grade for each repository and tests the correlation between the grade and the number of forks that the repo recieved.

To use this script for yourself, you should first generate a personal ghp token to access the Github API. The one that is provided in the code is out of date.
