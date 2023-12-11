
import pandas as pd
import plotly.graph_objects as go
import dash_mantine_components as dmc
from dash_express import DashExpress, Page
#данные
get_df = lambda: pd.read_csv('data.txt')
#страница
app = DashExpress(logo='Dashbord for project')
page = Page(
    app=app, #DashExpress app
    url_path='/', # Путь страницы
    name='A dashboard about demographic data.',
    get_df=get_df, # Функция дашборда
    )
#график
def bar_func(df):
    pv = pd.pivot_table(df, index='continent', values='lifeExp').reset_index()
    fig = go.Figure([go.Bar(x=pv['continent'], y=pv['lifeExp'])])
    return fig
#макет
page.layout = dmc.SimpleGrid(
    page.add_graph(h='calc(100vh - 140px)',render_func=bar_func)
    )
#фильт
page.add_autofilter('continent', multi=True)
page.add_autofilter('country', multi=True)
#page.add_autofilter('lifeExp', multi=True)


app.run()
   




