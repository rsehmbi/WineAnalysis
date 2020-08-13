# Wine Analysis

CMPT-353 Summer 2020 Project

## Getting Started

In order to clone the project, copy and paster the link on terminal using the command:<br />
```
git clone https://csil-git1.cs.surrey.sfu.ca/rsehmbi/sfucmpt353.git
```
### Prerequisites

In order to run the various small programs in the project you need to install python 3 including some libraries


### Installing

The list of libraries to install before running the project

1. Install Pandas: https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html <br />
2. Install Numpy: https://www.edureka.co/blog/install-numpy/
3. Install Ski-kit learn: https://scikit-learn.org/stable/install.html


## Project Structure
The project is divided into various small directories and programs

1. data_comparison
    <br />
    - LocationReviews <br />
                    -Extract_Location_analysis.py <br />
                    -Transform_Load_Analysis.py <br />
                    -[Other related files] <br />
    - PhysiochemicalProperties <br />
                    -Physiochem_analysis.py <br />
                    -Transform_and_Analyze.py <br />
                    -[Other related files] <br />
2. graph_resilience
    <br />
    - grape_resilience.py <br />
    - internal_error.py<br />
    - predict_ratings.py<br />
    - wine_stats.py<br />
    - [Other related files]
3. variety_by_reviews
   - data
      - 1442_8172_compressed_winemag-data-130k-v2.csv.zip
   - output
      - barplots_by_variety.png
      - wordcloud_by_variety.png
   - data_classification.py
   - dadta_cleaning.py
   - data_exploration.py
   - main.py
4. vivino_scrape
   - vivino_scrape_sel.py


### How to run the individual programs and the order to run the program

## data_comparison
1. In order to see the results as mentioned on the report: <br />
   From the project home directory go to
   ```
   cd data_comparison/LocationReviews
   ```
2. After you are in LocationReviews folder <br />
   First Command to run:
   ```
   python3 Extract_Location_analysis.py
   ```
   After running this command you can run
   ```
   python3 Transform_Load_Analysis.py
   ```
3. From the project home directory go to
   ```
   cd data_comparison/PhysiochemicalProperties
   ```
   First Command to run:
   ```
   python3 Physiochem_analysis.py
   ```
   Seconf Command to run:
   ```
   python3 Transform_and_Analyze.py
   ```

<br /><br /><br />
##  grape_resilience
To run:
```
python3 wine_stats.py merge.csv winemag-data-130k-v2.csv
```
Various figures will be output in figures, stats data can be found in stats

<br /><br /><br />
## variety_by_reviews
1. Non standard libraries that need to be installed:
   ```
   nltk
   wordcloud
   sklearn
   seaborn
   numpy
   pandas
   ```
2. **Must mainain** the directory structure to read the input data and output files.
3. cd into
   ```
   cd sfucmpt353/variety_by_reviews
   ```
4. Run the command:
   ```
   python3 main.py
   ```
5. The input data will be read from <br />**sfucmpt353/variety_by_reviews/data/1442_8172_compressed_winemag-data-130k-v2.csv.zip**
6. The visualization files will be produced in <br /> **sfucmpt353/variety_by_reviews/output/barplots_by_variety.png**
and **sfucmpt353/variety_by_reviews/output/wordcloud_by_variety.png**
7. The classification validation accuracy score will be output to the console.