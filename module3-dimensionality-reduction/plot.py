from plotly.graph_objs import *
import plotly.io as pio
import numpy as np
import copy

def DictMerge(a, b):
    return {**a, **b}

def Map(func, iterable):
    return list(map(func, iterable))


def Setup(plot, data=[], layout={}):
    plot = plot.copy()
    to_copy = plot['data'][0]

    new_data = Map(lambda thing: DictMerge(to_copy, thing), data)

    plot['data'] = new_data
    plot['layout'] = DictMerge(plot['layout'], layout)

    return plot


def Plot(plot, fig=None):
    if fig==None:
        fig = Figure(data=plot['data'], layout=plot['layout'])

    return fig


plots = {
  "default" : {
    "data": [{
      "line": {
        "color": "rgb(102,135,231)", 
        "width": 3
      }, 
      "mode": "lines", 
      "type": "scatter3d", 
      "x": [0, 2],
      "y": [0, 3],
      "z": [0, 4],
    }],
    "layout": {
      "scene": {
        "xaxis": {
          "gridcolor": "rgb(255, 255, 255)", 
          "zerolinecolor": "rgb(255, 255, 255)", 
          "showbackground": True, 
          "backgroundcolor": "rgb(235, 235,235)"
        }, 
        "yaxis": {
          "gridcolor": "rgb(255, 255, 255)", 
          "zerolinecolor": "rgb(255, 255, 255)", 
          "showbackground": True, 
          "backgroundcolor": "rgb(235, 235,235)"
        }, 
        "zaxis": {
          "gridcolor": "rgb(255, 255, 255)", 
          "zerolinecolor": "rgb(255, 255, 255)", 
          "showbackground": True, 
          "backgroundcolor": "rgb(235, 235,235)"
        }, 
        "camera": {"eye": {
            "x": 1.25, 
            "y": -1.4, 
            "z": 0.5
          }}, 
        "aspectratio": {
          "x": 1, 
          "y": 1, 
          "z": 0.85
        },
        "annotations" : [{
            # doing text
            "showarrow" : False,
            "x": 0,
            "y": 0,
            "z": 0,
            "text":"",
            "font":{
                "color":"black",
                "size":12
            },
            "xanchor":"left",
            "xshift":10,
            "opacity":0.7
        }]}, 
      "title": "Default Graph", 
      "width": 900, 
      "height": 750, 
      "showlegend": False,
      "autosize": False
      }},
    "default_2d": {
        "data": [{
          "line": {
            "color": "rgb(102,135,231)", 
            "width": 4
          }, 
          "mode": "lines", 
          "type": "scatter", 
          "x": [0, 2],
          "y": [0, 3]
    }], 
    "layout": {

    }
    }}
