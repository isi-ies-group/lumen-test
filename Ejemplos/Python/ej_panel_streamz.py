
### el plugin de Intake "intake-streamz" no está maduro y no se puede usar mediante .yaml
### sí se puede usar directamente Streamz en un panel: ejecutar "panel serve ej_panel_streamz.py" con panel v=0.X (el v=1.X no funciona)

# The following packages will be DOWNGRADED:

  # bokeh                                  3.1.1-pyhd8ed1ab_0 --> 2.4.3-pyhd8ed1ab_3
  # panel                                  1.0.3-pyhd8ed1ab_0 --> 0.14.4-pyhd8ed1ab_0
  
import numpy as np
import pandas as pd
import panel as pn
from streamz.dataframe import Random, PeriodicDataFrame
import hvplot.streamz

def random_datapoint3(now=None, **kwargs):
    """Example of querying a single current value"""
    if now is None:
        now = pd.Timestamp.now()
    return pd.DataFrame(
        {'c': np.random.random(1)}, index=[now])

df = PeriodicDataFrame(random_datapoint3, interval='1s')

plot = df.hvplot.line(title="Memory Usage (used)", backlog=200)
pn.panel(plot).servable()