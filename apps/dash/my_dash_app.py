import dash
# import dash_bootstrap_components as dbc
# from .layout import layout
# from .callbacks import register_callbacks
from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc
# from dash import Input, Output, dcc, html
from dash import Input, Output, State, dcc, html
import openai
# from flask_login import current_user
# from snakeeyes.blueprints.bet.models.bet import Bet

#################################################
#####     configurations
#################################################

##### openai-mais2
API_KEY = "d70b34fbd24d4016a5cf88dbc5f91e78"
RESOURCE_ENDPOINT = "https://openai-mais-2.openai.azure.com/"
openai.api_type = "azure"
openai.api_key = API_KEY
openai.api_base = RESOURCE_ENDPOINT
openai.api_version = "2023-07-01-preview"

def get_completion(prompt, model='gpt-35-turbo-16k'):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        engine=model,
        messages=messages,
        temperature=0,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]



# external_stylesheets = [dbc.themes.BOOTSTRAP, 'http://localhost:8000/static/css/dashapp.css', 'https://use.fontawesome.com/releases/v6.3.0/css/all.css']
external_stylesheets = [dbc.themes.BOOTSTRAP]

app = DjangoDash('SimpleExample', external_stylesheets=external_stylesheets)   # replaces dash.Dash
# app = DjangoDash('SimpleExample')   # replaces dash.Dash
# app.title = 'HS Explorer'
# app.layout = layout


app.layout = html.Div([
    # html.H5("Dash-ChatGPT Example"),
    html.Br(),
    dbc.Row(
        dbc.Col(
            dbc.InputGroup(
                [
                    dbc.Input(id='search-input-text', type='text', placeholder='Type your message here', style={'width':500}),
                    dbc.Button("Search", id="search-submit-button", n_clicks=0, color="success"),
                ]
            ), 
            # width=6, 
            # lg=6,  # Sets the width to 4 out of 12 columns on large screens and above
            # sm=12,
            # className="ml-8 ml-lg-3 p-3",
        ), 
    ),
    dbc.Row(
        dbc.Col(
            dcc.Loading(
                children=[
                    html.Div(id='search-output-text')
                ],
                type="default",
            ), 
            # width = 6, 
            # style={"position":"absolute", "left":"300px", "top":"20px"}
        ),
        # style={"left":"300px", "top":"20px"}
    )

])

# Search
@app.callback(
    Output('search-output-text', 'children'),
    Input('search-submit-button', 'n_clicks'),
    State('search-input-text', 'value')
)
def update_output(n_clicks, input_text):
    if n_clicks >0:
        # Extract the generated text from the response
        generated_text =  get_completion(input_text)
        # current_user = current_user -1   # ???????????????????????????????????????
        # Return the generated text as the output
        return generated_text
