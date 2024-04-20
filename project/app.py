import pandas as pd
import plotly.graph_objects as go
import dash_mantine_components as dmc
from dash_express import DashExpress, Page
from module import bar_func
from module import get_df
from module import draw
#данные
def main():
    #страница
    app = DashExpress(logo='Dashbord for project')
    page = Page(
        app=app, #DashExpress app
        url_path='/', # Путь страницы
        name='A dashboard about demographic data.',
        get_df=get_df, # Функция дашборда
        )
    fig = bar_func(get_df())
    draw(page)
    app.run()
if __name__ == "__main__":
    main()
   
   





