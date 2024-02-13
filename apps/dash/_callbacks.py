import dash_bootstrap_components as dbc
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

current_user = 'current'
#################################################
#####     Callbacks updating layouts
#################################################
def register_callbacks(dash_app):

    # set the content according to the current pathname
    @dash_app.callback(
            [Output("page-content", "children"), 
             Output("page-title", "children"),
             Output("label-coins", "children"),

             
             ],
            Input("url", "pathname"))
    def render_page_content(pathname):
        if pathname == "/dash/search": #or pathname == "/dash":
            # return html.P("This is the home page!")
            # print(current_user.id)
            return html.Div([
                            html.H5("Dash-ChatGPT Example"),
                            dbc.Row(
                                dbc.Col(
                                    dbc.InputGroup(
                                        [
                                            dbc.Input(id='search-input-text', type='text', placeholder='Type your message here', style={'width':500}),
                                            dbc.Button("Search", id="search-submit-button", n_clicks=0, color="success"),
                                        ]
                                    ),width=6
                                )
                            ),
                            dbc.Row(
                                dbc.Col(
                                    dcc.Loading(
                                        children=[
                                            html.Div(id='search-output-text')
                                        ],
                                        type="default",
                                    ), width = 6, 
                                    # style={"position":"absolute", "left":"300px", "top":"20px"}
                                )
                            )
                        ]), html.Span("Search", style={"font-size": "20px", "margin": "10px", "margin-left": "120px", 'font-weight': 'bold'}),\
                          html.Span("Coins: "+ str(current_user), style={ "margin": "10px", "margin-left": "120px"})


        elif pathname == "/dash/chat":
            return html.Div([
                            html.H5("Test Bet"),
                            dbc.Row(
                                dbc.Col([
                                    html.Div(id="coins-bet"),
                                    dbc.Button("Bet", id="chat-submit-button", n_clicks=0, color="success")
                                ], width=6)
                            ),
                        ]), \
                            html.Span("Chat", style={"font-size": "20px", "margin": "10px", "margin-left": "100px", 'font-weight': 'bold'}), \
                          html.Span("Coins: "+ str(current_user), style={"font-size": "16px", "margin": "10px", "margin-left": "120px"})
        
        elif pathname == "/dash/reference":
            return html.P("Here are all your messages"), \
                           html.Span("Reference", style={"font-size": "20px", "margin": "10px", "margin-left": "100px", 'font-weight': 'bold'}), \
                           html.Span("Coins: "+ str(current_user), style={"font-size": "16px", "margin": "10px", "margin-left": "120px", })
        
        # If the user tries to reach a different page, return a 404 message
        return html.Div(
            [
                html.H1("404: Not found", className="text-danger"),
                html.Hr(),
                html.P(f"The pathname {pathname} was not recognised..."),
            ],
            className="p-3 bg-light rounded-3",
        )

    ###########################################################
    #####              Functional Callbacks
    ###########################################################

    # Page 1 Search
    @dash_app.callback(
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


    # # Page 2 Bet
    # @dash_app.callback(
    #     Output('coins-bet', 'children'),
    #     Input('chat-submit-button', 'n_clicks'),
    # )
    # def update_bet(n_clicks):
    #     if n_clicks >0:
    #         params = {
    #             "user_id": current_user.id,
    #             "guess": 5,
    #             "die_1": 2,
    #             "die_2": 3,
    #             "roll": 5,
    #             "wagered": 1,
    #             "payout": 1,
    #             "net": -1,
    #         }

    #         bet = Bet(**params)
    #         bet.save_and_update_user(current_user)
    #         return html.Span("Coins: "+ str(current_user), style={"font-size": "16px", "margin": "10px", "margin-left": "120px", })



