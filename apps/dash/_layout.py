"""
This app creates an animated sidebar using the dbc.Nav component and some local
CSS. Each menu item has an icon, when the sidebar is collapsed the labels
disappear and only the icons remain. Visit www.fontawesome.com to find
alternative icons to suit your needs!

dcc.Location is used to track the current location, a callback uses the current
location to render the appropriate page content. The active prop of each
NavLink is set automatically according to the current pathname. To use this
feature you must install dash-bootstrap-components >= 0.11.0.

For more details on building multi-page Dash applications, check out the Dash
documentation: https://dash.plot.ly/urls
"""

import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html
# from flask_login import current_user

PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"
PLOTLY_LOGO = "static/images/logo-dash.png"

PLOTLY_LOGO = "http://127.0.0.1:8000/static/images/logo-dash.png"


# def create_user_component():
#     # Check if the user is authenticated
#     # if current_user.is_authenticated:
#     #     user_id = current_user.id
#     # else:
#     #     user_id = "Guest"  # or whatever you want to display for non-authenticated users
#     user_id = current_user.id
#     return html.Div(
#         [
#             html.A(f"Back to home (User ID: {user_id})", href="/", style={"margin": "10px"}),
#             html.A("Logout", href="/logout", style={"margin": "10px"}),
#         ],
#         style={"text-align": "left"}
#     )













sidebar = html.Div(
    [
        html.Div(
            [
                # width: 3rem ensures the logo is the exact width of the
                # collapsed sidebar (accounting for padding)
                html.Img(src=PLOTLY_LOGO, style={"width": "3rem"}),
                html.H4("HSExplorer"), 
            ],
            className="sidebar-header",
        ),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink(
                    [
                        html.I(className="fa fa-compass me-2"), 
                        html.Span("Search")
                    ],
                    href="/dash/search",
                    active="exact",
                ),
                dbc.NavLink(
                    [
                        html.I(className="fa fa-comments me-2"),
                        html.Span("Chat"),
                    ],
                    href="/dash/chat",
                    active="exact",
                ),
                dbc.NavLink(
                    [
                        html.I(className="fa fa-book me-2"),
                        html.Span("Reference"),
                    ],
                    href="/dash/reference",
                    active="exact",
                ),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    className="sidebar",
)

# Define the top bar
topbar = dbc.Row(
    [
        dbc.Col(
                # html.Span("Your Text Label", 
                # style={"font-size": "20px", "margin": "10px"}), 
                html.Div(id="page-title", 
                        #  className="content"
                         ),
                width=8
            ),
        dbc.Col(


            dbc.Row(
                [
                    dbc.Col(html.Div(id="label-coins"), width='auto'),
                    dbc.Col(html.A("Back to home", href="/", style={"margin": "10px"}), width='auto'),
                    dbc.Col(html.A("Logout", href="/logout", style={"margin": "10px"}), width='auto')
                ],
                align="center",  # Vertical alignment
                # no_gutters=True,  # Remove space between columns
            )





            # html.Div(
            #     [
            #         html.Div(id="label-coins"),

            #         # dbc.Col(create_user_component()),
            #         html.A("Back to home", href="/", style={"margin": "10px"}),
            #         html.A("Logout", href="/logout", style={"margin": "10px"}),
            #     ],
            #     style={"text-align": "left"}
            # ),
            # width=4
        )
    ],
    # no_gutters=True,
    align="center",
    style={"background-color": "#f8f9fa", "padding": "10px", "borderBottom": "1px solid #e8e9ea"}
)

content = html.Div(id="page-content", className="content")

layout = html.Div(
    [
        dcc.Location(id="url"),
        sidebar,
        html.Div(
            [
                topbar,
                content
            ],
            style={"width": "calc(100% - 5em)", "float": "right"}
        )
    ]
)



