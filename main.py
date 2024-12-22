# import required libraries
from random import choice
from faker.proxy import Faker
from numpy.ma.core import arange
from csv import writer


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
        csv_writer.writerow(['ID', 'Name', 'Location', 'College', 'Year', 'Program', 'Source'])  # Header
        csv_writer.writerows(zip(ids, names_list, location_list, college_list, years_list, programs_list,
                                 sources_list))  # Writing the data into the csv file


def main() -> None:
    size = 10000

    # Generate fake data
    generate_data(size)


if __name__ == '__main__':
    main()
