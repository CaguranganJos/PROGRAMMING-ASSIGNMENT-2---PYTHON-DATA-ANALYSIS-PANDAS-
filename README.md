# PROGRAMMING-ASSIGNMENT-2---PYTHON-DATA-ANALYSIS-PANDAS-
Deadline: September 10, 2025; 11:59 pm

<br>

## I. Table of Contents:
1. Programming Assignment 3.1: PROBLEM 1
2. Programming Assignment 3.2: PROBLEM 2
3. Author

<br>

## Programming Assignment 3.1: PROBLEM 1
> Instructions: <br>
&nbsp;&nbsp;&nbsp;&nbsp;Using knowledge obtained from the experiment and demonstrations: <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;a. Load the corresponding .csv file into a data frame named cars using pandas <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;b. Display the first five and last five rows of the resulting cars. <br>

<br>

#### The entire code.
```python
import pandas as pd

cars = pd.read_csv('cars.csv') 
first_5 = cars.loc[(cars.index<5)|(cars.index>26)]

print("These are the first and last five entries: ")
first_5
```

<br>

#### Step-by-step Thought Process.
1. First, import the library pandas as it will be used throughout the entire code by importing it as pd.
```python
import pandas as pd
```
2. To answer letter (a), first, read and load the Excel file, "cars.csv" using pandas function: pf.read_csv(file name) and store it in the dataframe named cars. After this, to answer (b), I first use the function .loc[] to locate a certain indices. Inside the loc function, I made two conditions in selecting indices, the first condition is that it should be less than 5, and the second condition is that it should be more than 26; with these conditions, it will result to the first and last 5 indices of the data frame. All these are stored in First_5. This technique is called subsetting because it is based on conditions regarding index values.
```python
cars = pd.read_csv('cars.csv') 
first_5 = cars.loc[(cars.index<5)|(cars.index>26)]
```
3. Lastly is to print "These are the first and last five entries: " and to also print the First_5 dataframe, which is the final result.
```python
print("These are the first and last five entries: ")
first_5
```

<br>

## Programming Assignment 3.1: PROBLEM 2
> Instructions: <br>
&nbsp;&nbsp;&nbsp;&nbsp;Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and indexing operations. <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars. <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;b. Display the row that contains the ‘Model’ of ‘Mazda RX4’. <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have? <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have. <br>

<br>

### a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.

<br>

#### The entire code.
```python
import pandas as pd 
cars = pd.read_csv("cars.csv") 
First_Odd = cars.loc[[0,1,2,3,4],['Model', 'cyl','hp', 'wt', 'vs', 'gear']]
print("Here are the first five models with their cyl, hp, wt, vs, and gear")
First_Odd 
```

<br>

#### Step-by-step Thought Process.
1. First, I imported the library pandas as pd, for it is used throughout the code. Next, I read and loaded the file named "cars.csv" and stored it in the dataframe named cars that will be manipulated later on.
```python
import pandas as pd 
cars = pd.read_csv("cars.csv") 
```
2. Next, I used the .loc function to locate certain indices in the dataframe cars. I have selected the indices: 0,1,2,3,4 to select all the rows in that index, and then I selected the odd-numbered columns that will intersect the selected index's rows. This means that all the odd-numbered columns of the first 5 indices will be stored in the dataframe named First_Odd. 
```python
First_Odd = cars.loc[[0,1,2,3,4],['Model', 'cyl','hp', 'wt', 'vs', 'gear']]
```
3. Lastly, I printed the sentence: "Here are the first five models with their cyl, hp, wt, vs, and gear". And later on printed the dataframe First_Odd where the results are stored.
```python
print("Here are the first five models with their cyl, hp, wt, vs, and gear")
First_Odd 
```

<br>

### b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.

<br>

#### The entire code.
```python
import pandas as pd  
df = pd.read_csv("cars.csv") 
Mazda_RX4 = df.loc[df['Model']=='Mazda RX4'] 
print("Here are the information regarding Mazda RX4:") 
Mazda_RX4
```

<br>

#### Step-by-step Thought Process.
1. First, I imported the library pandas as pd, for it is used throughout the code. Next, I read and loaded the file named "cars.csv" and stored it in the dataframe named df.
```python
import pandas as pd  
df = pd.read_csv("cars.csv") 
```
2. Next, I used the function .loc to locate certain columns. I first located the column named "model", and then a condition to compare all the words in the column model and find the exact word: "Mazda RX4", and print all the rows in that index. All these are then stored in Mazda_RX4.
```python
Mazda_RX4 = df.loc[df['Model']=='Mazda RX4'] 
```
3. Lastly, I printed the sentence: "Here are the information regarding Mazda RX4:". And later on printed the dataframe Mazda_RX4 where the results are stores.
```python
print("Here are the information regarding Mazda RX4:") 
Mazda_RX4
```

<br>

### c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have? 

<br>

#### The entire code.
```python
import pandas as pd 
c = pd.read_csv("cars.csv") 
C = c.loc[c['Model']=='Camaro Z28',['Model','cyl']] 
print("This is the number of cylinders Camaro Z28 have:") 
C
```

<br>

#### Step-by-step Thought Process.
1. First, I imported the library pandas as pd, for it is used throughout the code. Next, I read and loaded the file named "cars.csv" and stored it in the dataframe named 'c'.
```python
import pandas as pd 
c = pd.read_csv("cars.csv") 
```
2. Next, I used .loc to locate from the dataframe c the column named 'Model' and then I selected 'Camaro Z28' in that model column. I have also selected the values alligned with the column cyl and model. All these are then stored in C.
```python
C = c.loc[c['Model']=='Camaro Z28',['Model','cyl']] 
```
3. Lastly, I printed the sentence: "This is the number of cylinders Camaro Z28 have:". And later on printed the dataframe C where the results are stored.
```python
print("This is the number of cylinders Camaro Z28 have:") 
C
```

<br>

### d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

<br>

#### The entire code.
```python
import pandas as pd 
d = pd.read_csv("cars.csv") 
D = d.loc[ 
        (d['Model']=='Mazda RX4 Wag') | 
        (d['Model']=='Ford Pantera L') | 
        (d['Model']=='Honda Civic'), ['Model','cyl','gear']] 
print("Here are the informations of Mazda RX4 Wag, Ford Pantera L, and Honda Civic") 
D
```

<br>

#### Step-by-step Thought Process.
1. First, I imported the library pandas as pd, for it is used throughout the code. Next, I read and loaded the file named "cars.csv" and stored it in the dataframe named 'd'.
```python
import pandas as pd 
d = pd.read_csv("cars.csv") 
```
2. Next, I used the .loc function to find a certain index in the column named model. However, since I needed to find several models, I made a condition of (|) to find several indices in the model column. After this, I also printed the column model, cyl, and gear intersecting those indices. All these are then stored in D.
```python
D = d.loc[ 
        (d['Model']=='Mazda RX4 Wag') | 
        (d['Model']=='Ford Pantera L') | 
        (d['Model']=='Honda Civic'), ['Model','cyl','gear']] 
```
3. Lastly, I printed the sentence: "Here are the information of Mazda RX4 Wag, Ford Pantera L, and Honda Civic". And later on printed the dataframe D where the results are stored.
```python
print("Here are the informations of Mazda RX4 Wag, Ford Pantera L, and Honda Civic") 
D
```

## V. Author
Name: Cagurangan, Jos Kendirck L.
<br>
Section: 2ECE-B
