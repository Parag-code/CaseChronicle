import pandas as pd
import plotly.express as px

def plot_timeline(events):
    df = pd.DataFrame(events)
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df = df.dropna()
    df.sort_values(by='date', inplace=True)
    fig = px.scatter(df, x='date', y='event', title="Legal Case Timeline", hover_data=['date', 'event'])
    fig.update_yaxes(autorange="reversed")
    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Event",
        hovermode="closest"
    )
    return fig