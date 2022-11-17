# Title

**Authors**: Jocel Arcelona, Josh Gottlieb, Josh Palgon

## Overview

We were tasked with providing Microsoft with a recommendation on how to get into the movie making business by looking at what films are currently doing well in the box office. Our chosen measure of successs is Return on Investment, which is calculated as Worldwide Profit / Production Budget. Our data sources had information only on box office revenue, not other sources such as streaming or downloads. Our data sources are The Numbers (`tn.movie_budgets.csv`), The Movie Database (`tmdb.movies.csv`), Box Office Mojo (`bom.movie_gross.csv`), and IMDb (`im.db`). To clean out data, we dropped all data that could not be joined by movie title and only looked at data from 2010-2019. We decided to use this method, as our budget data only had title to use to link with our other data, and the business question only cares about recent data. We did not have useable information from 2020 onwards, so we chose 2010-2019 to have a ten year period up to our most current data. Mystery and Sci-Fi are our top choices for best genres to produce, given their high median return on investment and upward trend in the most recent years. Animation is the highest performing genre by median return on investment in our data set but has been on the decline recently, so we would not recommend producing in Animation. Horror and Thriller are genres that are worth keeping tabs on due to their upward trend but it would be best to see if the trend continues. 



A one-paragraph overview of the project, including the business problem, data, methods, results and recommendations.

## Business Problem

Microsoft wants to enter the movie business, but they do not know what type of movie to make. They want to know which movies are currently doing the best at the box office, so that they can understand what kind of movie to produce.

Our business problem is quite vague, as there are no particular variables we are required to focus on. Success is also not defined for us. Therefore, we chose to focus on money overall, specifically the return on investment (ROI) for each movie. ROI is calculated by dividing the worldwide profit by the production costs.

ROI is an important metric because it represents a measurement of profitability of a venture that can be used to compare alteranatives with different investment sizes. For example, if a project costs $100 and makes a profit of $200, and another project costs $10,000 and makes a profit of $20,000, they both have an ROI of 200%. This allows us to normalize profits between cheap and expensive movies.

One pitfall of using return on investment is that it introduces some instability into our calculations because movies which have a very low budget with a medium-high nominal profit will have an inflated ROI. For a company of Microsoft's size, they may prefer to have a lower return on investment per project but make larger sums of money overall. However, we believe that ROI is useful for showing the overall profitability of a movie and is one of the better single factors to consider outside of a more extensive multi-dimensional analysis.



Summary of the business problem you are trying to solve, and the data questions that you plan to answer in order to solve them.

***
Questions to consider:
* What are the business's pain points related to this project?
* How did you pick the data analysis question(s) that you did?
* Why are these questions important from a business perspective?
***

## Data

We incorporated data from The Numbers (`tn.movie_budgets.csv`), The Movie Database (`tmdb.movies.csv`), Box Office Mojo (`bom.movie_gross.csv`), and IMDb (`im.db`). We pulled budget and revenue information from the Box Office Mojo and The Numbers datasets. Genre information was pulled from The Movie Database and IMDB, whie directors and writers were pulled solely from IMDB.

As part of merging our data sets, we focused mainly on merging via titles, with release date acting as a secondary key. Our sample size dropped significantly due to a lack of overlap between data sets.

Once we had our data merged, we determined that we had the most information with regards to genre, director, and writer.



***
Questions to consider:
* Where did the data come from, and how do they relate to the data analysis questions?
* What do the data represent? Who is in the sample and what variables are included?
* What is the target variable?
* What are the properties of the variables you intend to use?
***

## Methods

We prepared the data by going through each dataset, figuring out which datasets can be merged with other ones and cleaning each dataframe created. 
After the preparation, we proceeded with data analysis. We decided which datasets to use and merged into one cohesive dataframe that helped us figure out which variables play a huge role in a movies financial success. 
The last step of the project, after cleaning and analyzing is visualizing all the output of our analysis. We used different types of plots and graphs that explained all our findings. 


Describe the process for analyzing or modeling the data. For Phase 1, this will be descriptive analysis.

***
Questions to consider:
* How did you prepare, analyze or model the data?
* Why is this approach appropriate given the data and the business problem?
***

## Results

Present your key results. For Phase 1, this will be findings from your descriptive analysis.

***
Questions to consider:
* How do you interpret the results?
* How confident are you that your results would generalize beyond the data you have?
***

Here is an example of how to embed images from your sub-folder:

### Visual 1
![graph1](./images/viz1.png)

## Conclusions

Provide your conclusions about the work you've done, including any limitations or next steps.

***
Questions to consider:
* What would you recommend the business do as a result of this work?
* What are some reasons why your analysis might not fully solve the business problem?
* What else could you do in the future to improve this project?
***

## For More Information

Please review our full analysis in [our Jupyter Notebook](./dsc-phase1-project-template.ipynb) or our [presentation](./DS_Project_Presentation.pdf).

For any additional questions, please contact **name & email, name & email**

## Repository Structure

Describe the structure of your repository and its contents, for example:

```
├── README.md                           <- The top-level README for reviewers of this project
├── dsc-phase1-project-template.ipynb   <- Narrative documentation of analysis in Jupyter notebook
├── DS_Project_Presentation.pdf         <- PDF version of project presentation
├── data                                <- Both sourced externally and generated from code
└── images                              <- Both sourced externally and generated from code
```
