import dash
from dash import dcc, html

from django_plotly_dash import DjangoDash

app = DjangoDash('SimpleExample')   # replaces dash.Dash

# app.scripts.config.serve_locally = True
# app.css.config.serve_locally = True

app.layout = html.Div([
    dcc.RadioItems(
        id='dropdown-color',
        options=[{'label': c, 'value': c.lower()} for c in ['Red', 'Green', 'Blue']],
        value='red'
    ),
    html.Div(id='output-color'),
    dcc.RadioItems(
        id='dropdown-size',
        options=[{'label': i,
                  'value': j} for i, j in [('L','large'), ('M','medium'), ('S','small')]],
        value='medium'
    ),
    html.Div(id='output-size')

])

@app.callback(
    dash.dependencies.Output('output-color', 'children'),
    [dash.dependencies.Input('dropdown-color', 'value')])
def callback_color(dropdown_value):
    return "The selected color is %s." % dropdown_value

@app.callback(
    dash.dependencies.Output('output-size', 'children'),
    [dash.dependencies.Input('dropdown-color', 'value'),
     dash.dependencies.Input('dropdown-size', 'value')])
def callback_size(dropdown_color, dropdown_size):
    return "The chosen T-shirt is a %s %s one." %(dropdown_size,
                                                  dropdown_color)











import dash
import dash_bootstrap_components as dbc
from .layout import layout
# from .callbacks import register_callbacks
from django_plotly_dash import DjangoDash


# # external_stylesheets = ['https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css']
# external_stylesheets = ['https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css']

# dash_app = dash.Dash(server=flask_app, url_base_pathname='/dash/', 
#                     #  external_stylesheets = external_stylesheets, 
#                         external_stylesheets=[dbc.themes.BOOTSTRAP],
#                         assets_folder='"/static/assets/')



external_stylesheets = [dbc.themes.BOOTSTRAP, 'http://localhost:8000/static/css/dashapp.css', 'https://use.fontawesome.com/releases/v6.3.0/css/all.css']

# app = DjangoDash('SimpleExample', external_stylesheets=external_stylesheets)   # replaces dash.Dash

app = DjangoDash('SimpleExample')   # replaces dash.Dash

app.title = 'HS Explorer'
# app.index_string = """<!DOCTYPE html>
# <html>
#     <head>
#         <!-- Global site tag (gtag.js) - Google Analytics -->
#         <script async src="https://www.googletagmanager.com/gtag/js?id=UA-62289743-10"></script>
#         <script>
#         window.dataLayer = window.dataLayer || [];
#         function gtag(){dataLayer.push(arguments);}
#         gtag('js', new Date());
#         gtag('config', 'UA-62289743-10');
#         </script>

#         {%metas%}
#         <title>{%title%}</title>
#         {%favicon%}
#         {%css%}
#         <link href="http://localhost:8000/static/css/dashapp.css" rel="stylesheet">
        
#         <link rel="stylesheet" href="https://use.fontawesome.com/releases/v6.3.0/css/all.css">
#     </head>
#     <body>
#         {%app_entry%}
#         <footer>
#             {%config%}
#             {%scripts%}
#             {%renderer%}
#         </footer>
#     </body>
# </html>"""

app.layout = layout
# register_callbacks(app)