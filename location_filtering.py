# location_filtering.py
import googlemaps
import plotly.express as px
import pandas as pd

# Initialize Google Maps API client
gmaps = googlemaps.Client(key='AIzaSyBNL8-iWGtMaiwMAY5I11bkHjkpZoXb6lU')

# Function to get coordinates (latitude, longitude) for a location
def get_coordinates(location):
    geocode_result = gmaps.geocode(location)
    if geocode_result:
        return geocode_result[0]['geometry']['location']
    return {'lat': None, 'lng': None}

# Add coordinates to the job listings
def add_coordinates(jobs_df):
    jobs_df['Coordinates'] = jobs_df['Location'].apply(get_coordinates)
    return jobs_df

# Create a map using Plotly Express
def visualize_job_locations(jobs_df):
    df_with_coords = jobs_df.dropna(subset=['Coordinates'])
    df_with_coords['Latitude'] = df_with_coords['Coordinates'].apply(lambda x: x['lat'])
    df_with_coords['Longitude'] = df_with_coords['Coordinates'].apply(lambda x: x['lng'])

    fig = px.scatter_mapbox(df_with_coords, lat='Latitude', lon='Longitude', hover_name='Job Title', hover_data=['Company', 'Location'],
                            color='Match Score', size='Match Score', zoom=10, mapbox_style='open-street-map')
    fig.show()
