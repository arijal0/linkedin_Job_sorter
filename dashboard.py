# dashboard.py
import dash
from dash import dcc, html
import plotly.express as px

def create_dashboard(jobs_df):
    app = dash.Dash(__name__)

    # Create the layout of the dashboard
    app.layout = html.Div(children=[
        html.H1(children='LinkedIn Job Matching Dashboard'),

        # Job match graph
        dcc.Graph(
            id='match-score-graph',
            figure=px.bar(jobs_df.head(10), x='Job Title', y='Match Score', color='Company')
        ),
        
        # Skill gap analysis
        html.Div(children=[
            html.H4('Skill Gap Analysis'),
            html.P(id='skill-gap-output'),
        ]),
        
        # Predicted salary
        html.Div(children=[
            html.H4('Predicted Salary for Selected Job'),
            html.P(id='predicted-salary-output'),
        ]),
        
        # Job location map
        dcc.Graph(
            id='job-location-map',
            figure=px.scatter_mapbox(jobs_df.dropna(subset=['Coordinates']),
                                     lat=jobs_df['Latitude'], lon=jobs_df['Longitude'], hover_name='Job Title')
        ),
    ])

    # Run the app
    app.run_server(debug=True)
