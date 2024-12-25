import pandas as pd

def calculate_demographic_data(print_data=True):
    # Leer los datos desde el archivo CSV
    df = pd.read_csv('adult.data.csv', header=None, names=[
        'age', 'workclass', 'fnlwgt', 'education', 'education-num',
        'marital-status', 'occupation', 'relationship', 'race',
        'sex', 'capital-gain', 'capital-loss', 'hours-per-week',
        'native-country', 'salary'
    ])

    # 1. Número de cada raza representada en el conjunto de datos
    race_count = df['race'].value_counts()

    # 2. Edad promedio de los hombres
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Porcentaje de personas con título de licenciatura (Bachelor's degree)
    percentage_bachelors = round(
        (df['education'].value_counts().get('Bachelors', 0) / len(df)) * 100, 1
    )

    # 4. Porcentaje de personas con educación avanzada que ganan más de 50K
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    higher_education_rich = round(
        (higher_education[higher_education['salary'] == '>50K'].shape[0] / higher_education.shape[0]) * 100, 1
    )
    lower_education_rich = round(
        (lower_education[lower_education['salary'] == '>50K'].shape[0] / lower_education.shape[0]) * 100, 1
    )

    # 5. Número mínimo de horas trabajadas por semana
    min_work_hours = df['hours-per-week'].min()

    # 6. Porcentaje de personas que trabajan las horas mínimas y ganan >50K
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round(
        (num_min_workers[num_min_workers['salary'] == '>50K'].shape[0] / num_min_workers.shape[0]) * 100, 1
    )

    # 7. País con el porcentaje más alto de personas que ganan >50K
    countries = df[df['salary'] == '>50K']['native-country'].value_counts()
    total_people_per_country = df['native-country'].value_counts()
    percentage_per_country = (countries / total_people_per_country * 100).dropna()
    highest_earning_country = percentage_per_country.idxmax()
    highest_earning_country_percentage = round(percentage_per_country.max(), 1)

    # 8. Ocupación más popular para personas que ganan >50K en India
    india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_rich['occupation'].mode()[0]

    # Resultados opcionales para imprimir
    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
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
