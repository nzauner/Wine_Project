#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 20:13:52 2020

@author: z
"""

#  Import statements
import pandas as pd
import numpy as np
import missingno

def clean_df(raw_df):
    '''Function that removes duplicate wines, unwanted columns, naans, and wines above $100'''
    nodup_df = raw_df.duplicated(subset='title', keep='first')
    nodup_df = raw_df[nodup_df].drop(['Unnamed: 0', 'designation', 'region_1', 'region_2'], axis=1)
    nodup_df = nodup_df.dropna()
    df = nodup_df[nodup_df['price'] >= 100 ].index
    nodup_df.drop(df, inplace=True)
    return nodup_df


def country_df(country):
    country = wine_df.loc[wine_df['country'] == country]
    country = us_wine.points.mean()
     = us_wine.points.std()
    return 



class Country:
  def __init__(country):
    self.name = name

  def country_stats(self):
    print("The standard deviation of {country} is " + self.name)

c1 = Country("US")
c1.myfunc() 








#
#def open_csv(file):
#    '''This is to import .csv data into a DataFrame'''
#    df = pd.read_csv(file)
#    print(type(df))
#    return df
#
#def remove_duplicates(df, col):
#    '''Remove the duplicate wine entries'''
#    nodup = df.duplicated(subset=col, keep='first')
#    return nodup
#
#def find_missing(df, nodup):
#    '''Uses missingno to visualize the missing value in DataFrame'''
#    return missingno.matrix(df[nodup])
#
#def drop_col(df, nodup, w, x, y, z):
#    '''Remove columns with missing data'''
#    nodup = df[nodup].drop([w, x, y, z], axis=1)
#    nodup = nodup.dropna()
#    return nodup
#
#def clean_df(nodup):
#    '''Remove wine with pricing over $100 per bottle'''
#    clean_wine_df = nodup[nodup['price'] >= 100 ].index
#    nodup.drop(clean_wine_df, inplace=True)
#    return clean_wine_df

# def open_cleaned_csv():
#     '''This function opens the csv and cleans the data'''
#     df = pd.read_csv('Data/winemag-data-130k-v2.csv')
#     nodup = df.duplicated(subset='title', keep='first')
#     nodup = df[nodup].drop(['Unnamed: 0', 'designation', 'region_1', 'region_2'], axis=1)
#     clean_wine_df = nodup[nodup['price'] >= 100 ].index
#     nodup.drop(clean_wine_df, inplace=True)
#     return clean_wine_df


# def clean_df(raw_df):
#     nodup = raw_df.duplicated(subset='title', keep='first')
#     nodup = raw_df[nodup].drop(['Unnamed: 0', 'designation', 'region_1', 'region_2'], axis=1)
#     df = nodup
#     return df

