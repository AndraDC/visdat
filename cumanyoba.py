#!/usr/bin/env python
# coding: utf-8

# # <center>Interactive Data Visualization in Python With Bokeh</center>

# ## Adding Interaction

# In[1]:

import streamlit as st
import pandas as pd
from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.models import HoverTool, ColumnDataSource
from bokeh.models import CategoricalColorMapper
from bokeh.palettes import Spectral6
from bokeh.layouts import widgetbox, row, gridplot
from bokeh.models import Slider, Select


# In[2]:


data = pd.read_csv("gapminder_tidy.csv")
data.set_index('Year', inplace=True)


# In[3]:


# Make a list of the unique values from the region column: regions_list
regions_list = data.region.unique().tolist()

# Make a color mapper: color_mapper
color_mapper = CategoricalColorMapper(factors=regions_list, palette=Spectral6)


# In[4]:


# Make the ColumnDataSource: source
source = ColumnDataSource(data={
    'x'       : data.loc[1970].fertility,
    'y'       : data.loc[1970].life,
    'country' : data.loc[1970].Country,
    'pop'     : (data.loc[1970].population / 20000000) + 2,
    'region'  : data.loc[1970].region,
})


# In[ ]:


# Create the figure: plot
plot = figure(title='1970', x_axis_label='Fertility (children per woman)', y_axis_label='Life Expectancy (years)',
           plot_height=400, plot_width=700, tools=[HoverTool(tooltips='@country')])

# Add a circle glyph to the figure p
plot.circle(x='x', y='y', source=source, fill_alpha=0.8,
           color=dict(field='region', transform=color_mapper), legend='region')

# Set the legend and axis attributes
plot.legend.location = 'bottom_left'
st.bokeh_chart(plot, use_container_width=True)

slider = st.slider('year', 1970, 2010, 1970)

