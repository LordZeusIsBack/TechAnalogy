# import required libraries
from random import choice
from faker.proxy import Faker
from numpy.ma.core import arange
from csv import writer
import pandas as pd
from pandas import DataFrame
from matplotlib import pyplot as plt
import seaborn as sns

def generate_data(num: int) -> None:
    """This function creates a randomly generated data to be written in the CSV file."""
    fake = Faker('en_IN')  # create faker object for creating fake data

    ids, names_list, college_list, programs_list, sources_list, years_list, location_list = [], [], [], [], [], [], []  # Initialize all lists
    programs = [
        'Data Science', 'Robotics', 'AI', 'Electric Vehicle',
        'Cybersecurity', 'Mechanical Engineering', 'Civil Engineering',
        'Software Development', 'Medicine', 'Digital Marketing'
    ]
    sources = [
        'Instagram', 'LinkedIn', 'College Collaboration',
        'Google-Form', 'Mass Mailing', 'WhatsApp', 'Facebook', 'X'
    ]
    years = ['1st', '2nd', '3rd', '4th']

    # append data into the initialized lists
    for i in arange(1, num + 1):
        ids.append(f'ID{str(i).zfill(5)}')
        names_list.append(fake.name())
        college_list.append(fake.company() + ' Company')
        programs_list.append(choice(programs))
        sources_list.append(choice(sources))
        years_list.append(choice(years))
        location_list.append(fake.city())

    with open('random_data.csv', 'w', newline='', encoding='UTF-8') as fp:
        csv_writer = writer(fp)  # Create Writer Object
        csv_writer.writerow(['ID', 'Name', 'City', 'College', 'Year', 'Program', 'Source'])  # Header
        csv_writer.writerows(zip(ids, names_list, location_list, college_list, years_list, programs_list,
                                 sources_list))  # Writing the data into the csv file

def demographic_analysis(df: DataFrame) -> None:
    print('Demographic Analysis:')

    # Trend analysis based on year of study
    year_counts = df['Year'].value_counts()

    # Visualization for Year distribution
    plt.figure(figsize=(8, 5))
    sns.set(style="whitegrid")
    sns.barplot(x=year_counts.index, y=year_counts.values, palette="viridis")
    plt.title("Distribution of Students by Year")
    plt.xlabel("Year")
    plt.ylabel("Number of Students")
    plt.show()

    # Trend analysis based on program
    program_counts = df['Program'].value_counts()

    # Visualization for Program distribution
    plt.figure(figsize=(8, 5))
    sns.barplot(y=program_counts.index, x=program_counts.values, palette="cubehelix")
    plt.title("Distribution of Students by Program")
    plt.xlabel("Number of Students")
    plt.ylabel("Program")
    plt.show()

    # Trend analysis based on source
    source_counts = df['Source'].value_counts()

    # Visualization for Source distribution
    plt.figure(figsize=(8, 5))
    sns.barplot(y=source_counts.index, x=source_counts.values, palette="magma")
    plt.title("Distribution of Students by Source")
    plt.xlabel("Number of Students")
    plt.ylabel("Source")
    plt.show()

def program_analysis(df: DataFrame) -> None:
    print('Program Analysis:')

    # Trend analysis based on program
    program_trend = df['Program'].value_counts().head(5)  # Top 5 programs
    print('\nInterest levels for various e-learning platforms:')
    print(program_trend)

    # Visualization
    plt.figure(figsize=(12, 6))
    sns.barplot(x=program_trend.index, y=program_trend.values)
    plt.title('Interest Level for various E-Learning Platforms')
    plt.show()

def data_preprocessing(df: DataFrame) -> None:
    print('Data Preprocessing Steps:')

    # Checking for missing values
    missing_values = df.isnull().sum()
    print('\nMissing values in the dataset:')
    print(missing_values)

    # Example: Fill missing values (if any)
    df.fillna(method='ffill', inplace=True)

    # Checking for duplicates
    duplicates = df.duplicated().sum()
    print('\nNumber of duplicate rows:')
    print(duplicates)

    # Example: Remove duplicates (if any)
    df.drop_duplicates(inplace=True)

    # Summary of cleaned data
    print('\nSummary of cleaned data:')
    print(df.describe())

def main() -> None:
    size = 10000

    # Generate fake data
    generate_data(size)

    # Load the generated dataset
    data = pd.read_csv('random_data.csv')

    # Execute the tasks
    demographic_analysis(data)
    program_analysis(data)
    data_preprocessing(data)

if __name__ == '__main__':
    main()
