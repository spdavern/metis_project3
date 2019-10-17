# Project Proposal

## Predicting Success of K-2 Literacy Intervention

Sean Davern<br/>Seattle, Fall Cohort, weeks 4-6.5

[Page Ahead Children's Literacy Program](http://www.pageahead.org/) is the leading provider of children's book and literacy services in Washington State, serving more than 850,000 childreen with 3 million new books since 1990.  Based on the reasearch that if a child can read at grade level by 3rd grade, they'll continue to read at grade level throughout through their academic career, Page Ahead's literacy programs especially aid reading and language skills of at-risk children.  Page Ahead's Book Up Summer program provides K-2nd grade students their choice of 12 new books, at no cost to the student, that are theirs to keep and read over each summer vacation.  This program, based on literacy research in Florida[^1] and elsewhere, has been shown to help address a well-established[^2] phenomenon called "summer reading setback" where reading abilities decline in summers.

Data provided to Page Ahead from the state of Washington is proposed to be analyzed to assess the performance of the Book Up program in the WA elementary schools  Page Ahead serves.  Student assessed as "at risk" or not meeting reading standards in kindergarten receive 0 to 3 years of Book Up program intervention services.  At third grade the state begins a mandatory testing program based on the Smarter Balanced Assessment Consortium[^3] (SBAC) testing system. The target predictors is whether these students meet English Language Arts (ELA) literacy standards [level 3 or 4].  The data contains other factors that may or may not correlate with the success for meeting standards which may help families, school, and third party programs like Page Ahead to identify kids at highest risk.

The proposed product of this project is a tool that can predict the impact on the probability of meeting ELA literacty standards of Page Ahead's Book Up program for K-2 students.  The projected impact will be a function of the number of summers a student receives the Book Up intervention as well as their kindergarten reading MAP score.

## MVP

An MVP would successfully identify kindergartener's who evaluated below standards and received 3 years of the Book Up program, which may not occur at the same school, and evaluate the increase in probability for meeting 3rd grade SBAC standards.   This involves evaluating each student for how many years of Page Ahead services they received, Kindergarten and 3rd grade ELA performances.  A model can then be fit to simply predict the probability for MetStandard=Y.  The MVP model will fit MetStandard as a function of kindergarten RIT score and number of treatments received.

## Data

Two example data files have been provided by Page Ahead:

* Seansample.xlsx
* Seandata2.xlsx

I signed an [Affidavit of Nondisclosure](https://github.com/spdavern/metis_project3/blob/master/references/PageAhead_Custom_Proxy_DSA_13_19%20Sean.pdf) with Page Ahead on 10/16/2019.  Subsequently I was provided access to 6 files totalling ~90MB of csv files.  The table below give an idea of the features based on the example data.

| Variable                   |  Type  | Description                                         | Used for Model |
| -------------------------- | :----: | --------------------------------------------------- | :------------: |
| RITScore                   |  Int   | K-2 performance score                               |     Target     |
| Score                      |  Int   | SBAC performance score                              |     Target     |
| LevelCode                  | string | SBAC performance level                              |     Target     |
| MetStandard                | string | Indicates is student met state standards            |     Target     |
| CurrentEnrollment SchoolID |  Int   | School student is entrolled in                      |     track      |
| TestSchoolID               |  Int   | School student took assessment at (indicates move)  |       Y        |
| CurrentGrade               |  int   | Grade in school student is in at time of assessment |       Y        |
| TestSchoolYear             | string | School year at time of assessment                   |       Y        |
| TestSeason                 | string | Part of school year assessment was taken            |       Y        |
| TestName                   | string | Assessment used                                     |       Y        |
| Gender                     | string | gender - use for assessing at risk groups           |       Y        |
| RacialEthnicGroup          | string | Ethnicity - use for assesing at risk groups         |       Y        |
| ELLStatus                  | string | English Language Learner - use for risk groups      |       Y        |
| PrimaryLanguage            | string | Mother tongue - use for risk groups                 |       Y        |
| HomeLanguage               | string | Language spoken in home - risk groups               |       Y        |
| LivingWith                 | string | Household leader - use for risk groups              |       y        |

Known Unknowns:

* Total number of students served by Page Ahead that we can track:  Low income student tend to be pretty mobile. Moving to a different school that isn't served by Page Ahead will reduce the number of students receiving the intervention.  The data above will be combined with data from Page Ahead indicating which schools they serve and when they began serving those schools.
* The performance of Book Up interventions, while almost certainly helpful, may not be enough to overcome other factors.  So, the percentage of kindergartners at risk that ultimately meet standards in 3rd grade may not have been previously assessed.

[^1]: Allington, Richard L and Anne McGill-Franzen,  [**Addressing Summer Reading Setback Among Economically Disadvantaged Elementary Students**](http://pageahead.org/_p/Allington%20Summer%20Reading%20Setback.pdf), Reading Psychology, 31: 411-427, 2010.

[^2]: Alexander, Entwisle, & Olson, 2007; Allington & McGill-Franzen, 2003; Cooper, Nye, Charlton, Lindsay, & Greathouse, 1996; Entwisle, Alexander, & Olson, 1997.  See ref **1**, pg. 412.
[^3]: Smarter Balanced Score Reporting, http://www.smarterbalanced.org/assessments/scores/.