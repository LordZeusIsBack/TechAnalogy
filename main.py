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

    # Trend analysis based on location
    location_trend = df['City'].value_counts().head(5)  # Top 5 locations
    print('\nLead sourcing based on location:')
    print(location_trend)

    # Trend analysis based on college
    college_trend = df['College'].value_counts().head(5)  # Top 5 colleges
    print('\nLead sourcing based on college:')
    print(college_trend)

    # Trend analysis based on year of study
    year_trend = df['Year'].value_counts()
    print('\nLead sourcing based on year of study:')
    print(year_trend)

    # Visualization
    fig, axes = plt.subplots(3, 1, figsize=(12, 18))
    sns.barplot(x=location_trend.index, y=location_trend.values, ax=axes[0])
    axes[0].set_title('Lead Sourcing by Location')
    axes[0].set_xticklabels(axes[0].get_xticklabels(), rotation=0)

    sns.barplot(x=college_trend.index, y=college_trend.values, ax=axes[1])
    axes[1].set_title('Lead Sourcing by College')
    axes[1].set_xticklabels(axes[1].get_xticklabels(), rotation=0)

    sns.barplot(x=year_trend.index, y=year_trend.values, ax=axes[2])
    axes[2].set_title('Lead Sourcing by Year of Study')

    plt.tight_layout()
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

    # Recommendations
    recommendations = df.groupby('Program')['City'].value_counts().unstack().fillna(0)
    print("\nRecommendations for target demographics:")
    print(recommendations)


def main() -> None:
    size = 10000

    # Generate fake data
    generate_data(size)

    # Load the generated dataset
    data = pd.read_csv('random_data.csv')

    # Execute the tasks
    demographic_analysis(data)
    program_analysis(data)


if __name__ == '__main__':
    main()
