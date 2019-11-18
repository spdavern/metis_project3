# Classification Project - With SQL Challenges

Author: Sean Davern  

Description: This project aims to determine if the effectiveness of Page Ahead's summer Book Up program to prevent declines in reading ability can be quantified using classification models.

## Project Documentation

Documentation for this project is represented by Jupyter Notebook (.ipynb files) comments, the slide presentation in `./reports/slide_deck.pptx (and .pdf)` and in the summary report in `./reports/summary.md (and .pdf)`.  Finally, see brief explanations of what project work each file is associated with below.

## Data

Due to obligations to Page Ahead and their obligation to the Seattle Public Schools, data used in this project is not stored in the GitHub repo.  See the following 2 files for details of our data sharing agreements (DSA).

* ./references/PA SPS DSA.pdf	Page Ahead's DSA

* ./references/PageAhead_Custom_Proxy_DSA_13_19 Sean.pdf	Sean's DSA

Contact the author for more information about the data.


## Project Organization 
------------

(generated with [datasciencemvp](https://github.com/cliffclive/datasciencemvp/))

(modified from [cookiecutter-datascience](https://drivendata.github.io/cookiecutter-data-science/))

```
.
├── BookUpProgram.ipynb		Notebook used to create the Book Up function
├── Database\ Creation.ipynb		Initial work to create a database for this project. 
├── ETL.ipynb		Python work to combine data files obtained from Page Ahead
├── Feature\ Engineering.ipynb		Python work to do feature engineering
├── Investigation		The investigation I gave on 10/25/19
│   ├── Data\ Control-Security.ipynb
│   ├── Data\ Control-Security.pdf
│   └── Data\ Control-Security.pptx
├── LICENSE
├── MVP.ipynb		My project MVP
├── Modeling.ipynb	Python work representing all modeling
├── Project\ Assignment.pdf		Content provided by Metis describing the assignment
├── README.md		This file
├── SQL\ Challenges		Work/solutions for the SQL challenges
│   ├── 09_part_i_sql_w3school.md		SQL Challenge part I - questions AND solution
│   ├── 09_part_ii_sql_baseball.md	SQL Challenge part II - questions only
│   ├── 09_part_iii_sql_soccer.md		SQL Challenge part III - questions only
│   ├── Baseball.ipynb		Solution to SQL Challenge part II
│   ├── Minimalistic.ipynb		Work completed to ask slack questions. See:
│		│					https://fall-sea19-metis.slack.com/archives/CPX56B88N/p1572213116013700
│   ├── Soccer.ipynb		Solution to SQL Challenge part III
│   ├── Test.ipynb		Work completed to try SQLAlchemy guidance from Roberto. See
│		│					https://fall-sea19-metis.slack.com/archives/CPX56B88N/p1572219428017000
│   ├── baseballdata		Baseball db files for Challenge II from lahman-csv_2014-02-14.zip
│   │   ├── AllstarFull.csv
│   │   ├── Appearances.csv
│   │   ├── AwardsManagers.csv
│   │   ├── AwardsPlayers.csv
│   │   ├── AwardsShareManagers.csv
│   │   ├── AwardsSharePlayers.csv
│   │   ├── Batting.csv
│   │   ├── BattingPost.csv
│   │   ├── Fielding.csv
│   │   ├── FieldingOF.csv
│   │   ├── FieldingPost.csv
│   │   ├── HallOfFame.csv
│   │   ├── Managers.csv
│   │   ├── ManagersHalf.csv
│   │   ├── Master.csv
│   │   ├── Pitching.csv
│   │   ├── PitchingPost.csv
│   │   ├── Salaries.csv
│   │   ├── Schools.csv
│   │   ├── SchoolsPlayers.csv
│   │   ├── SeriesPost.csv
│   │   ├── Teams.csv
│   │   ├── TeamsFranchises.csv
│   │   ├── TeamsHalf.csv
│   │   └── readme2013.txt
│   ├── database.sqlite		Soccer db file for Challenge III from soccer.zip
│   ├── lahman-csv_2014-02-14.zip		Source zip file for baseballdata folder	
│   └── soccer.zip		Source zip file for database.sqlite
├── data		All data used for the project (Not uploaded to GitHub)
│   ├── interim		Pickle files used to save intermediate results
│   │   ├── X_df.pkl
│   │   ├── Y_df.pkl
│   │   ├── book_up_dict.pickle
│   │   ├── map_df.csv
│   │   ├── map_df.pkl
│   │   ├── targets.csv
│   │   └── targets.pkl
│   ├── processed		Not used
│   └── raw		Source data files from Susan Dibble at Page Ahead.  Source:
│				│		https://drive.google.com/drive/folders/1150HuPmgyvbKFgp1A8WT1eFHixpZtD1q
│				│		Covered by Data Sharing Agreement: PageAhead_Custom_Proxy_DSA_13_19\ Sean.pdf
│       ├── 2015_ADR-301-MAP-Assessment-Scores.csv	2015 MAP Data Seattle Public Schools
│       ├── 2016_ADR-301-MAP-Assessment-Scores.csv	2016 MAP Data Seattle Public Schools
│       ├── 2017_ADR-301-MAP-Assessment-Scores.csv	2017 MAP Data Seattle Public Schools
│       ├── 2018_ADR-301-MAP-Assessment-Scores.csv	2018 MAP Data Seattle Public Schools
│       ├── 2018_ADR-311-State-Assessment-Scores.csv  -2018 SBAC Data Seattle Public Schools
│       ├── Sample\ Data	Data files Susan shared during project planning.
│       │   ├── Seandata2.xlsx		Example SBAC data
│       │   └── Seansample.xlsx		Example MAP data
│       └── Seattle\ Onboarding\ History.xlsx		Page Ahead 
├── main.py
├── modules_attempt.ipynb		A failed attempt to move to module based python code
├── proposal.md		My project proposal in markdown format
├── proposal.pdf	My project proposal in pdf format
├── references		Data Sharing Agreements and literature references
│   ├── 2010\ Allington\ Study\ WWC\ Quick\ Review.pdf		1 pg study summary behind Book Up 
│   ├── 2015-MAP-Normative-Data-AUG15.pdf		MAP scores explanation
│   ├── Allington\ Summer\ Reading\ Setback.pdf		Research supporting Book Up program
│   ├── PA\ SPS\ DSA.pdf	Data sharing agreement (DSA) between Page Ahead and SPS
│   └── PageAhead_Custom_Proxy_DSA_13_19\ Sean.pdf	DSA between Sean and Page Ahead
├── reports
│   ├── figures		Figures generated by python
│   │   ├── Classification\ Report.html
│   │   ├── Coefficients1.svg
│   │   ├── ConfusionMatrix.svg
│   │   ├── EthnicGroupCoeffients.svg
│   │   ├── LogREthnicGroupCoeffients.svg
│   │   ├── LogRcvEthnicGroupCoeffients.svg
│   │   ├── SchoolCoeffients.svg
│   │   ├── SchoolCoeffientsCompare.svg
│   │   ├── Scores0-1-2.svg
│   │   ├── Scores1-2.svg
│   │   ├── ScoresMetStandard.svg
│   │   ├── literacy-wordle.jpg
│   │   ├── logRCoefficients1.svg
│   │   └── logRcvCoefficients1.svg
│   ├── slide_deck.pdf		My presentation in pdf format
│   ├── slide_deck.pptx		My presentation in PowerPoint format
│   ├── summary.md		My summary report in md format
│   ├── summary.pdf		My summary report in pdf format
│   └── templates		Slide template I used:  I used the widescreen version.
│       ├── Alphabet-letters-on-wooden-scrabble-pieces-PowerPoint-Templates-Standard.pptx
│       └── Alphabet-letters-on-wooden-scrabble-pieces-PowerPoint-Templates-Widescreen.pptx
└── src		Python module source files  (most came with the cookiecutter template.)
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-37.pyc
    │   └── obtain.cpython-37.pyc
    ├── explore.py
    ├── interpret.py
    ├── model.py
    ├── obtain.py		Modified for use with modules_attempt.ipynb
    ├── scrub.py
    └── utils
        ├── __init__.py
        ├── load_or_make.py
        └── make_dataset.py
```

