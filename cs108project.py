# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 22:10:24 2023

@author: bayst
"""

# File: cs108project.py
# your name: Ding Xin
# your email: dmx@bu.edu
# U63555835
# CS108 A1

import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm


# haul depth vs larval yield

def depth_vs_yield(df, depth, fish, floor = 100, ceiling = 100000):
    '''sets haul depth as an index and compares it to total larval yield on a line graph'''
    
    # indexed by sorted haul depth values
    df_depth = pd.DataFrame(index = depth.sort_values())   
    
    
    plt.ylabel('Larval Yield by Species (Number)')
    plt.title('Depth vs. Total Larval yield by Species')
    
    
    # iterate thru all fish species
    for species in fish:
        
        if ceiling >= df[species].sum() >= floor:
            
            # create a 
            df_depth[f'{species}'] = df[species]
            
            df_depth[f'{species}'].plot(legend = True)
    
    
    
    # df_depth.plot()

    plt.show()
    
    
# calculate relative fish frequency per yield

def relative_fish_frequency(df, popular_fish):
    '''calculates a new df column with the percentage of the most abundant fish out of the total larval yield for that cruise'''
    
    # rf = relative frequency
    df_rf = pd.DataFrame(index = df['Record Number'])
    
    # placehodler to define column
    for species in popular_fish:
        
        df_rf[f'{species}_rf'] = 0

    # iterate over df length and popular fish list to do arithemetic  
    for record in range(len(df)):
        
        for species in popular_fish:
            
            df_rf[f'{species}_rf'].iloc[record] = df[species].iloc[record] / df['Total Larvae (Number)'].iloc[record]
            
    
    df_rf.plot()
    
    
# larval yield per transect/station

def yield_per_transect(df, transect, latitude, longitude, date, filename, popular_fish):
    '''plots a histogram containing the total larvae found at each cruise station/transect'''
    '''the transect parameter can take the form of any cruise station/transect data series'''
    '''also produces an excel file that can be produced on a google map'''
    
    # set new index and sort the index
    df_transect_unsorted = pd.DataFrame(index = df[transect].unique())
    
    df_transect = df_transect_unsorted.sort_index()
    
    # group the original df by the transect data series
    gb_transect = df.groupby(transect)
    
    df_transect['Larval Yield by Species (Number)'] = gb_transect['Total Larvae (Number)'].sum()

    # df_transect.hist()
    # plt.bar(df.index, df_transect['Larval Yield by Species (Number)'])
    
    plot = df_transect.plot(y = 'Larval Yield by Species (Number)', kind = 'bar', legend = True)
    
    # formatting

    plot.set_title('Larval Yield per Transect')
    plot.set_xlabel('Transect')
    plot.set_ylabel('Total Larval Yield (Number)')
    
    print(df_transect)
    print()
    
    plt.show()
    
    # google maps part starts here
    
    df_map = pd.DataFrame()
    
    # df is grouped by the transect column
    gb_transect = df.groupby(transect)
    
    # averages of coordinates are taken to give an approximate location on google maps
    longitude_mean = gb_transect[longitude].mean()
    
    latitude_mean = gb_transect[latitude].mean()
    
    
    # longtidue mean here is set as a placeholder to define the new column
    df_map['Coordinates'] = longitude_mean
    
    
    # iterate over the length of the new df
    for record in range(len(df_map)):
        
        df_map['Coordinates'].iloc[record] = f'{latitude_mean.iloc[record]}, {longitude_mean.iloc[record]}'
    
    
    # total counts of popular fish
    for fish in popular_fish:
        
        # placeholder again
        df_map[f'{fish}_count'] = longitude_mean
        
        fish_count = gb_transect[fish].sum()
        
        df_map[f'{fish}_count'] = fish_count
         
        # print(df_map[f'{fish}_count'])
        
        plt.title(f'Larval Yield of {fish} by Transect')
        
        df_map[f'{fish}_count'].plot(y = 'Larval Yield by Species (Number)', kind = 'bar', legend = True)
        
        plt.show()
    
    df_map.to_excel(filename)
    
    # relative frequencies (%) of fish per transect
    
    
    for species in popular_fish:
        
        df_map[f'{species}_rf'] = df_map[f'{species}_count'] / df_transect['Larval Yield by Species (Number)']
        
        df_map[f'{species}_rf'].plot(y = 'Relative Frequency of Larval Yield', legend = True)
        
        # print(f'{species}, {df_map[f"{species}_rf"].mean()}')\
            
        print(df_map[f'{species}_rf'])
        print()
        
        # species_list += [species]
        
    # print(df_map[species_list])
        
            
            
    

# helper regression function

def regression(df, independent, dependent):
    '''helper function for comparing all fish species to one another'''
    
    # set x and y variables
    X = df[independent]
    Y = df[dependent]
    
    # this costant method is used to make the linear regression model 
    constant = sm.add_constant(X) 
    
    # perform regression
    model = sm.OLS(Y, constant).fit()
    print(model.summary())
    
    # method to extract R^2
    r_squared = model.rsquared    
    
    plt.xlabel(independent)
    plt.ylabel(dependent)
    plt.scatter(X, Y)
    plt.plot(X, model.predict(constant), color='red')
    plt.show()
    
    
    return r_squared



def fish_matrix(df, test_fish, fish):
    '''takes a test fish as a parameter and returns '''

    # dictionary to hold R^2 values to be accumulated in to
    
    R2_values = {}
    
    for species in fish:
        
        # the R^2 value is assigned to its respective species in comparison to the test fish
        regression_result = regression(df, test_fish, species)
        
        R2_values[species] = f'{regression_result:.5f}'
        
    # the matrix tests the test fish against itself, so it is removed for redundancy purposes
    del R2_values[test_fish]
    
    print(R2_values)
        

    





if __name__ == '__main__':
    
    filename = 'Ichthyoplankton Data - Prerecruit Survey Larval Data Data.csv'
    
    # read data and set index
    df = pd.read_csv(filename)
    
    # comparing depth and larval yield
    depth = df['Haul Depth (M)']
    
    # fish list
    fish = ['Anoplarchus Purpurescens', 'Artedius Sp.', 'Artedius Harringtoni', 'Bathylagus Pacificus', 'Brosmophycis Marginata',
    'Chauliodus Macouni', 'Citharichthys Spp.', 'Cololabis Saira', 'Diaphus Theta', 'Engraulis Mordax',	'Glyptocephalus Zachirus',
    'Hippoglossoides Elassodon', 'Icichthys Lockingtoni', 'Isopsetta Isolepis', 'Leuroglossus Stilbius', 'Liparis Fucensis',
    'Liparis Pulchellus', 'Lipolagus Ochotensis', 'Lyopsetta Exilis', 'Microgadus Proximus', 'Microstomus Pacificus',
    'Nannobrachium Regale', 'Nansenia Candida', 'Osmeridae', 'Parophrys Vetulus', 'Plectobranchus Evides', 'Pleuronichthys Decurrens', 
    'Protomyctophum Crockeri', 'Protomyctophum Thompsoni', 'Psettichthys Melanostictus', 'Pseudobathylagus Milleri', 'Ronquilus Jordani', 
    'Sardinops Sagax', 'Sebastes Spp.', 'Sebastolobus Spp.', 'Stenobrachius Leucopsarus', 'Tarletonbeania Crenularis', 
    'Tetragonurus Cuvieri', 'Trachipterus Altivelis', 'Trachurus Symmetricus', 'Unidentified']
    
    # no ceiling 
    # depth_vs_yield(df, depth, fish, floor = 1000)
    
    # lower yield species
    # depth_vs_yield(df, depth, fish, floor = 250, ceiling = 1000)
    
    # no restrictions
    # depth_vs_yield(df, depth, fish, floor = 0)
   
    # abundant fish relative frequency
    popular_fish = ['Engraulis Mordax', 'Stenobrachius Leucopsarus', 'Sebastes Spp.', 'Lyopsetta Exilis']
    
    # larval yield per transect/station
    transect = 'New Transect'
    latitude = 'Latitude'
    longitude = 'Longitude'
    date = 'Cruise Date'
    filename = 'transect-locational-data.xlsx'
    total_larvae = 'Total Larvae (Number)'
    
    # yield_per_transect(df, transect, latitude, longitude, date, filename, popular_fish)
    
    # relative_fish_frequency(df, popular_fish)
    
    # regression depression !
    # regression(df, 'Stenobrachius Leucopsarus', 'Engraulis Mordax')
    # regression(df, 'Lyopsetta Exilis', 'Engraulis Mordax')
    # regression(df, 'Citharichthys Spp.', 'Engraulis Mordax')
    # regression(df, 'Engraulis Mordax', 'Citharichthys Spp.')
    
    fish_matrix(df, 'Engraulis Mordax', fish)
    # fish_matrix(df, 'Citharichthys Spp.', fish)
    # fish_matrix(df, 'Stenobrachius Leucopsarus', fish)
    # fish_matrix(df, 'Sebastolobus Spp.', fish)
    # fish_matrix(df, 'Tarletonbeania Crenularis', fish)
    # fish_matrix(df, 'Nannobrachium Regale', fish)
    # fish_matrix(df, 'Sebastes Spp.', fish)
    # fish_matrix(df, 'Lyopsetta Exilis', fish)
    
    
    
    
    