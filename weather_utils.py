# This function will display all observations
import streamlit as st
import pandas as pd

def display_all():
    """Display all observations"""
    df = pd.read_csv('weather_observations.csv')
    #st.write("Heluuuuuuuuuuuu-----++++++++++++")
    #st.dataframe(df)
    st.write(df)
    return


# This function for adding new observation

def add_observation(date_str, temp, condition, humidity, wind, filename="weather_observations.csv"):
    # 1. Read my csv file that I put in the same path
    df = pd.read_csv(filename)
    
    # 2. Append the new data
    new_row = {'Date': date_str, 'Temperature_Celsius': temp, 'Condition': condition, 'Humidity_Percentage': humidity, 'Wind_Speed_kmh': wind}
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    
    # 3. Save it back
    df.to_csv(filename, index=False)


# This function is for viewing weather stats

def get_weather_stats(filename="weather_observations.csv"):
    """
    Grabs our weather data file and calculates the core metrics 
    required by our project specs (Averages, Extrems, and Modes).
    """
    # 1. Load the database file
    df = pd.read_csv(filename)
    
    # If the file happens to be completely empty, return None to prevent errors
    if df.empty:
        return None
        
    # 2. Calculate the required metrics precisely
    stats = {
        'avg_temp': df['Temperature_Celsius'].mean(),
        'min_temp': df['Temperature_Celsius'].min(),
        'max_temp': df['Temperature_Celsius'].max(),
        # .mode()[0] picks the top most frequent string in the Condition column
        'common_condition': df['Condition'].mode()[0]
    }
    
    return stats

def search_by_date(target_date, filename="weather_observations.csv"):
    """
    Filters our weather database to find rows matching a specific date.
    Returns a DataFrame of matches, or an empty DataFrame if nothing is found.
    """
    # Load the CSV file
    df = pd.read_csv(filename)
    
    # Filter the 'Date' column to match the user's requested date exactly
    matching_rows = df[df['Date'] == target_date]
    
    return matching_rows

#-------------------------------------------------------------------------Menu option 1
#-------------------------------------------------------------------------Menu option 2
#-------------------------------------------------------------------------Menu option 3
#-------------------------------------------------------------------------Menu option 4

