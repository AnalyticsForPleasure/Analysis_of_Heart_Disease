import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from collections import Counter
from pprint import pprint

######### info about the data ############################################################################################################################################################
# HeartDisease - target trait.
# BMI - a value that allows you to assess the degree of correspondence between a person's mass and his height, and thereby indirectly judge whether the mass is insufficient, normal or excessive. It is important in determining the indications for the need for treatment.
# Smoking is a major risk factor for cardiovascular disease. When smoke from a cigarette is inhaled, the reaction of the cardiovascular system immediately follows: within one minute, the heart rate begins to rise, increasing by 30% within ten minutes of smoking. The bad habit also increases blood pressure, fibrinogen and platelet levels, making blood clots more likely.
# AlcoholDrinking - alcohol causes not only temporary disturbances in the functioning of the heart, but also permanent ones. Heart pain after alcohol is not the only health problem associated with alcohol consumption.
# Stroke - Ischemic stroke occurs 4 times more often than hemorrhagic. One of the leading causes of this suffering is heart disease, which impairs its functioning, as a result of which the blood flow in the arteries is disturbed and the blood supply to the brain is reduced. Another cause of stroke in heart disease is thromboembolism, when clots form in the cavities of the heart (most often with heart failure) - blood clots.
# PhysicalHealth - how many days in a month did you feel poor physical health.
# MentalHealth - how many days in a month did you feel poor mental health.
# DiffWalking - difficulty climbing stairs.
# Sex - gender of a person.
# AgeCategory - age category of the subjects. *Race-obviously
# Diabetic - obviously
# PhysicalActivity - adults who reported doing physical activity or exercise during the past 30 days other than their regular job
# GenHealth - well-being.
# SleepTime - number of hours of sleep.
# Asthma- obviously
# KidneyDisease - obviously
# Skin Cancer - obviously

    # Factor to be checked is a factor related to the presence or absence of a disease.
    # The factors are as follows. : Stroke, KidneyDisease, Diabetic, Asthma, SkinCancer

if __name__ == '__main__':
    pd.set_option('display.max_rows', 5000)
    df = pd.read_csv('/home/shay_diy/PycharmProjects/Analysis_of_Heart_Disease/Data/heart_2020_cleaned.csv')
    column_headers = list(df.columns.values)
    print('*')

    # Filtering by 2 criteria : HeartDisease , DiffWalking
    data_about_heart_disease = df.loc[(df['HeartDisease'] == 'Yes') & (df['DiffWalking'] == 'Yes')]

    # Create a pivot table to count males and females for each AgeCategory
    result = data_about_heart_disease.pivot_table(index='AgeCategory', columns='Sex', aggfunc='size', fill_value=0)

    # Reset index to make AgeCategory a column
    result.reset_index(inplace=True)

    result['Percentage Difference'] = ((result['Male'] - result['Female']) / result[['Male', 'Female']].sum(axis=1)) * 100

    print(result)

