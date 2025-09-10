{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "13dc7e52",
   "metadata": {},
   "source": [
    "# EXPERIMENT 3 PYTHON DATA ANALYSIS (PANDAS)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1c7aa4d1",
   "metadata": {},
   "source": [
    "### Problem 2"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "47c80be1",
   "metadata": {},
   "source": [
    "##### a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7…) of cars."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "301cc293",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Here are the first five models with their cyl, hp, wt, vs, and gear\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Model</th>\n",
       "      <th>cyl</th>\n",
       "      <th>hp</th>\n",
       "      <th>wt</th>\n",
       "      <th>vs</th>\n",
       "      <th>gear</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Mazda RX4</td>\n",
       "      <td>6</td>\n",
       "      <td>110</td>\n",
       "      <td>2.620</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Mazda RX4 Wag</td>\n",
       "      <td>6</td>\n",
       "      <td>110</td>\n",
       "      <td>2.875</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Datsun 710</td>\n",
       "      <td>4</td>\n",
       "      <td>93</td>\n",
       "      <td>2.320</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Hornet 4 Drive</td>\n",
       "      <td>6</td>\n",
       "      <td>110</td>\n",
       "      <td>3.215</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Hornet Sportabout</td>\n",
       "      <td>8</td>\n",
       "      <td>175</td>\n",
       "      <td>3.440</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               Model  cyl   hp     wt  vs  gear\n",
       "0          Mazda RX4    6  110  2.620   0     4\n",
       "1      Mazda RX4 Wag    6  110  2.875   0     4\n",
       "2         Datsun 710    4   93  2.320   1     4\n",
       "3     Hornet 4 Drive    6  110  3.215   1     3\n",
       "4  Hornet Sportabout    8  175  3.440   0     3"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd # Import the library pandas as pd to use its functions\n",
    "cars = pd.read_csv(\"cars.csv\") # read the excel file saved in the same folder with the code and store it in \"cars\"\n",
    "First_Odd = cars.loc[[0,1,2,3,4],['Model', 'cyl','hp', 'wt', 'vs', 'gear']] #use the loc function to locate the index 0,1,2,3,4 and locate also the columes of cyl,hp,wt,vs, and gear. All these stores in First_Odd\n",
    "print(\"Here are the first five models with their cyl, hp, wt, vs, and gear\") # Print \"Here are the first five models with their cyl, hp, wt, vs, and gear\"\n",
    "First_Odd # print the index and colums selected that was stores in First_Odd"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b8959114",
   "metadata": {},
   "source": [
    "##### b. Display the row that contains the ‘Model’ of ‘Mazda RX4’."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "4be8ba52",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Here are the information regarding Mazda RX4:\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Model</th>\n",
       "      <th>mpg</th>\n",
       "      <th>cyl</th>\n",
       "      <th>disp</th>\n",
       "      <th>hp</th>\n",
       "      <th>drat</th>\n",
       "      <th>wt</th>\n",
       "      <th>qsec</th>\n",
       "      <th>vs</th>\n",
       "      <th>am</th>\n",
       "      <th>gear</th>\n",
       "      <th>carb</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Mazda RX4</td>\n",
       "      <td>21.0</td>\n",
       "      <td>6</td>\n",
       "      <td>160.0</td>\n",
       "      <td>110</td>\n",
       "      <td>3.9</td>\n",
       "      <td>2.62</td>\n",
       "      <td>16.46</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       Model   mpg  cyl   disp   hp  drat    wt   qsec  vs  am  gear  carb\n",
       "0  Mazda RX4  21.0    6  160.0  110   3.9  2.62  16.46   0   1     4     4"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd  # Import the library pandas as pd to use its functions\n",
    "df = pd.read_csv(\"cars.csv\") # read the excel file saved in the same folder with the code and store it in \"df\"\n",
    "Mazda_RX4 = df.loc[df['Model']=='Mazda RX4'] # use loc function to locate in column \"model\" the word \"Mazda RX4\" and print all the colums for it. All these stores in \"Mazda_RX4\"\n",
    "print(\"Here are the information regarding Mazda RX4:\") # Print \"Here are the information regarding Mazda RX4:\"\n",
    "Mazda_RX4 # print the model named Mazda RX$ and all the columns in that index that was stored in Mazda_RX4"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "99618ab3-6a42-43ed-9e0a-dee153458f36",
   "metadata": {},
   "source": [
    "##### c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "7aae8dd2-366f-4b8b-98df-b1f9a8ffd93f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "This is the number of cylinders Camaro Z28 have:\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Model</th>\n",
       "      <th>cyl</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>23</th>\n",
       "      <td>Camaro Z28</td>\n",
       "      <td>8</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Model  cyl\n",
       "23  Camaro Z28    8"
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd # Import the library pandas as pd to use its functions\n",
    "c = pd.read_csv(\"cars.csv\") # read the excel file saved in the same folder with the code and store it in \"c\"\n",
    "C = c.loc[c['Model']=='Camaro Z28',['Model','cyl']] # use locate function for the model named \"Camaro Z28\" and locate also the value in the same index whiole in the column cyl. All these stored in C\n",
    "print(\"This is the number of cylinders Camaro Z28 have:\") # print \"This is the number of cylinders Camaro Z28 have:\"\n",
    "C # print the model named Camaro Z28 and the cyl value"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ef04881c-ad49-43b3-9b13-86b1fb16a260",
   "metadata": {},
   "source": [
    "##### d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "73948f30-a390-40c0-a259-820228c0e65d",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Here are the informations of Mazda RX4 Wag, Ford Pantera L, and Honda Civic\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Model</th>\n",
       "      <th>cyl</th>\n",
       "      <th>gear</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Mazda RX4 Wag</td>\n",
       "      <td>6</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>Honda Civic</td>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>28</th>\n",
       "      <td>Ford Pantera L</td>\n",
       "      <td>8</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             Model  cyl  gear\n",
       "1    Mazda RX4 Wag    6     4\n",
       "18     Honda Civic    4     4\n",
       "28  Ford Pantera L    8     5"
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd # Import the library pandas as pd to use its functions\n",
    "d = pd.read_csv(\"cars.csv\") # read the excel file saved in the same folder with the code and store it in \"d\"\n",
    "D = d.loc[ # Use the loc function\n",
    "        (d['Model']=='Mazda RX4 Wag') | #locate the model named \"Mazda RX4 Wag\", inside column \"Model\" and use a condition or using \"|\" for the next car\n",
    "        (d['Model']=='Ford Pantera L') | #locate the model named \"Ford Pantera L\", inside column \"Model\" and use a conditio or using \"|\" for the next car\n",
    "        (d['Model']=='Honda Civic'), ['Model','cyl','gear']] #locate the model named \"Ford Pantera L\", inside column \"Model\". With all the cars, print also the value stored in the same index of the model and in the columes of cyl and gear all these stored in D\n",
    "print(\"Here are the informations of Mazda RX4 Wag, Ford Pantera L, and Honda Civic\") #print \"Here are the informations of Mazda RX4 Wag, Ford Pantera L, and Honda Civic\"\n",
    "D # Print the car models: Mazara RX4 Wag, Honda Civic, and Ford Pantera L, with their corresponding cyl and gear which was stored in D"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
