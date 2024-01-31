# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 10:18:41 2023

@author: bayst
"""

# File: a23_voter_data.py
# your name: Ding Xin
# your email: dmx@bu.edu
# U63555835
# CS108 A1


import pandas as pd
import matplotlib.pyplot as plt

def filter_df(df, bool_series):
    '''returns a new df that contains the records that matches the given bool_series parameter'''
    
    # df_bool = pd.DataFrame(index=df.index)
    boolio = bool_series
    # accumulator set up for the printout
    count = len(df[boolio])
  
    # for cond in df_bool:
        
        # print(cond)
        # matches = df_bool
        
        # new df created
        # df_bool = bool_series 
    
    print(f'{count} records matched the criteria.')
    
    return df[boolio]


def show_party_affiliation(df, floor=100):
    '''procs a df and returns the relative frequencies of the different party affiliations and the raw counts'''
    '''floor refers to the minimum amount that each party must have in order to be displayed in the output'''
    # for cond in df['Party Affiliation']:
    
    print(f'Of the {len(df)} records, the party affiliation is:')
    relative_frequencies = (df['Party Affiliation'].value_counts() / len(df)) * 100
    
    n_counts = df['Party Affiliation'].value_counts()
    # print(n_counts)
    
    condition = filter_df(n_counts, n_counts > floor)
    
    parties = df['Party Affiliation'].unique()
    
    # for criteria printout
    criteria_count = 0
    
    # for the pie chart
    # pie_counts = []
    
    for party in parties:
        # print(party)
        
        if n_counts.loc[party] >= floor:
                
            print(f'    party {party} : {relative_frequencies.loc[party]:2.2f}% (n={n_counts.loc[party]})')
            
            # df_pie += n_counts.loc[party]
            
            
            
            
            # return n_counts.loc[party].plot.pie()
        # if n_counts >= floor:
            criteria_count += 1
            
            # pie_counts += [n_counts.loc[party], party]
            
            
            # print(f'party {party} : {relative_frequencies}% (n={n_counts})')
    print(f'{criteria_count} records matched the criteria.')
    
    # return df_pie.plot.pie()

    
    # if n_counts.loc[party] >= floor:
        
        
    
    # return pie_counts.plot.pie()
    condition.plot.pie(title = 'Party Affiliation')
    
    # plt.close()

def show_dob_distribution(df):
    '''procs a df and returns a string output of the # of voters within certain DOB ranges'''
    
    print(f'Here is the DOB distribution ({len(df)} records):')
    
    # DOB[0] == 1979 evalutaes to True
    # for year in range(1920, 2015, 5):
        # print(year)
        
        # for dob in df['Date of Birth']:
            # maybe reverse for conditions?
            
            # if year < dob < (year + 5):
        
    # date_of_births = df['Date of Birth']            
    
    # for bday in date_of_births:
    
    #     for year in range(1920, 2015, 5):
            
            # condition = (df['Date of Birth'] > f'{year}') & (df['Date of Birth'] < f'{year + 5}')
            
            # if year < date_of_births.loc[bday] < (year + 5):
                
                # print(f'    DOB < {year + 5}    ')
                
    for year in range(1920, 2010, 5):
        
        condition = (df['Date of Birth'] > f'{year}') & (df['Date of Birth'] < f'{year + 5}')
        
        condition_counts = len(df[condition])
        
        # print(condition_counts)
        # true_conditions = condition_counts[1]
        
        upper_year = year + 5
        
        relative_percentage = (condition_counts / len(df)) * 100
        # print(relative_percentage)
        print(f'    DOB < {upper_year}    {condition_counts: ^4}  ({relative_percentage:.2f}%)')
        
        
    df['Date of Birth'].hist(bins = 25)
    plt.title('Date of Birth Distribution')
    plt.show()
    
    # plt.close()

def show_precinct_stats(df):
    '''procs a df and prints out the distribution of voter records grouped by precincts'''
    
    print(f'Here is a distribution of the {len(df)} records by precinct:')
    print()

    # create a new df, this one will be accumulated into
    df_new = pd.DataFrame(index = df['Precinct Number'].unique())
    
    gb = df.groupby('Precinct Number')
    
    # number of voters per precinct
    df_new['Voters'] = df['Precinct Number'].value_counts()
    
    
    # precinct numbers
    df_new['Precinct Names'] = df['Precinct Number'].unique()
    
    
    # median DOB
    df_new['Median DOB'] = gb['Date of Birth'].median()
    
    
    # mean voter score
    df_new['Mean Voter Score'] = gb['voter_score'].mean()
    
    
    # for loop to find # of members in each party by precinct
    # for party in df['Party Affiliation'].unique():
    # df_new['party'] = gb['Party Affiliation'].sum()
    
    # for party in df_new['party']:
        
    #     if party == 'D ':
            
    #         df_new['party-D'] += 1
    # democrats = df['Party Affiliation'] == 'D '
    # for cond in pa:
        
        # matches = gb['Party Affiliation'] == cond
        # df_new['party-D'] = 
    
    # number of democrat numbers
    # df_new['party-D'] = 
    
    # condition_D = gb['Party Affiliation'] == 'D '
    
    # a list that contains the relevant parties
    # pa is short for parties
    pa = ['D ', 'U ', 'R ']
    
    # party_counts = gb['Party Affiliation'].value_counts()
    
    # a loop to iterate over every party
    for party in pa:

        # this is a condition variable that checks if a DUR party is found in the party affiliation column
        DUR_check = df['Party Affiliation'] == party
        
        
        DUR_per_precinct = df[DUR_check].groupby('Precinct Number')
        
        df_new[f'party-{party}'] = DUR_per_precinct['Precinct Number'].count()
        
    
    print(df_new)
    print()
    print('Voter turnout by precinct (percentages):')
    
    
    # new df for voter turnout
    to = pd.DataFrame(index = df['Precinct Number'].unique())
    
    
    # voter turnout for v20 state
    to['turnout-v20state'] = gb['v20state'].sum() / gb['Precinct Number'].count()    
    
    
    # voter turnout for v21 town
    to['turnout-v21town'] = gb['v21town'].sum() / gb['Precinct Number'].count()    
    
    
    # voter turnout for v21 primary
    to['turnout-v21primary'] = gb['v21primary'].sum() / gb['Precinct Number'].count()    
    
    
    # voter turnout for v22 general
    to['turnout-v22general'] = gb['v22general'].sum() / gb['Precinct Number'].count()    


    # voter turnout for v23 town
    to['turnout-v23town'] = gb['v23town'].sum() / gb['Precinct Number'].count()    
    
    
    print(to)

    
def build_google_maps_file(df, filename):
    '''returns a new spreadsheet based on a df parameter'''
    
    # new empty dataframe
    # gm stands for google maps
    df_gm = pd.DataFrame(index = df.index)
    
    # new voter score
    df_gm['voter_score'] = df['voter_score']
    # print(df_gm)
    
    # new names
    df_gm['Name'] = df['First Name'] + ' ' + df['Last Name']
    
    
    # new addresses
    df_gm['Addresses'] = df['Residential Address - Street Number'].astype(str) + ' ' + df['Residential Address - Street Name'] + ', Newton MA, ' + df['Residential Address - Zip Code'].astype(str)
    
    print(f'Building Google Maps file with {len(df)} records.')
    print(f'Wrote {filename}: {len(df)} records.')
    
    return df_gm.to_excel(filename)
    
    



if __name__ == '__main__':
    
    filename = 'newton_voters.xlsx'
    
    # read data and set index
    df = pd.read_excel(filename)
    df.index = df['Voter ID Number']
    
    # some pie charts
    # df['Precinct Number'].value_counts().plot.pie()
    # df['Party Affiliation'].value_counts().plot.pie()
    # df['voter_score'].value_counts().plot.pie()
    
    # filter_df(df, df['First Name'] == 'PAUL')
    # show_party_affiliation(df)
    # show_party_affiliation(df, floor = 200)
    # show_dob_distribution(df)
    show_precinct_stats(df)
    
    # df_results = filter_df(df, df['v22general'])
    # df_results = filter_df(df_results, df_results['Party Affiliation'] == 'L ')
    # build_google_maps_file(df_results, "v2022-voters-L.xlsx")
    
    ### CODE BELOW IS WORK DONE FOR TASK 2 QUESTION 3 ###
    
    # Question A
    
    # a condition variable is assigned to a column, because we only want the True voters, no == operator is needed
    # voted = df['v23town']
    
    # we can create a new df, passing our condition variable into the original df and assigning it to the new df
    # df_v23 = df[voted]
    
    # use the functions as needed, one at a time as to not fuck with the graphs
    # show_party_affiliation(df_v23)
    
    # show_dob_distribution(df_v23)
    
    # Question B
    
    # a condition variable is assigned to a column, because we only want the True voters, no == operator is needed
    voted = df['v23town']
    
    # we can create a new df, passing our condition variable into the original df and assigning it to the new df
    df_v23 = df[voted]
    
    # can create a new condition variable that compares DOBs in v23town voters to the year 1990
    post_1990 = df_v23['Date of Birth'] > '1990'
    
    # ANOTHER df is created with both of these conditions in mind
    # the second condition variable is passed into the new df as the condition was based on the new df
    df_v23_post1990 = df_v23[post_1990]
    
    # home stretch
    # show_party_affiliation(df_v23_post1990)
    # show_party_affiliation(df_v23_post1990, floor = 10)
    
    # show_dob_distribution(df_v23_post1990)
    
    # build_google_maps_file(df_v23_post1990, 'v2023-voters-post1990-DOB.xlsx')

    
    