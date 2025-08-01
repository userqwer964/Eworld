import pandas as pd

def calculate_demographic_data(print_data=True):
    column_names = [
        "age", "workclass", "fnlwgt", "education", "education-num", "marital-status",
        "occupation", "relationship", "race", "sex", "capital-gain", "capital-loss",
        "hours-per-week", "native-country", "salary"
    ]
    df = pd.read_csv("adult.data", header=None, names=column_names, skipinitialspace=True)


    race_count = df['race'].value_counts()


    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)


    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)


    advanced_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education = df[advanced_education]
    lower_education = df[~advanced_education]

    higher_education_rich = round((higher_education['salary'] == '>50K').mean() * 100, 1)
    lower_education_rich = round((lower_education['salary'] == '>50K').mean() * 100, 1)


    min_work_hours = df['hours-per-week'].min()


    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((num_min_workers['salary'] == '>50K').mean() * 100, 1)


    country_salary_df = df.groupby('native-country')['salary'].value_counts(normalize=True).unstack()
    country_salary_df = country_salary_df.fillna(0)
    highest_earning_country = (country_salary_df['>50K'] * 100).idxmax()
    highest_earning_country_percentage = round(country_salary_df['>50K'].max() * 100, 1)


    india_50k = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_50k['occupation'].value_counts().idxmax()

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelors degrees:", percentage_bachelors)
        print("Percentage with higher education that earn >50K:", higher_education_rich)
        print("Percentage without higher education that earn >50K:", lower_education_rich)
        print("Min work time:", min_work_hours)
        print("Percentage of rich among those who work fewest hours:", rich_percentage)
        print("Country with highest percentage of rich:", highest_earning_country)
        print("Highest percentage of rich people in country:", highest_earning_country_percentage)
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
