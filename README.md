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
                    -[Other Related data]... <br />
    - PhysiochemicalProperties <br />
                    -Physiochem_analysis.py <br />
                    -Transform_and_Analyze.py <br />
                    -[Other Related data]... <br />
2. graph_resilience
3. variety_by_reviews
4. vivino_scrape


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


