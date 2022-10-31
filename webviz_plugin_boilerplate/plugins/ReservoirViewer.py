import os
from pathlib import Path
from dash import Dash, dcc, html, Input, Output
import subprocess as sub
from webviz_config import WebvizPluginABC
from .RV.RVConfig import Configuration
from webviz_config.webviz_assets import WEBVIZ_ASSETS
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np

import webviz_core_components as wcc

class ReservoirViewer(WebvizPluginABC):

    def __init__(self,
                 app,
                 root: Path,
                 benchmark: str,
                 folder2d: Path,
                 folderDistMatr: Path,
                 chartType: str,
                 layoutCurve: str,
                 clusteringMethod: str,
                 distanceMatrix: Path,
                 minClusters: int,
                 maxClusters: int,
                 iterations: int,
                 properties: list,
                 strategies: list,
                 allModels: Path,
                 highlightedModels: str) -> None:

        super().__init__()

        self.root = root
        self.benchmark = benchmark
        self.folder2d = folder2d
        self.folderDistMatr = folderDistMatr
        self.chartType = chartType
        self.layoutCurve = layoutCurve
        self.clusteringMethod = clusteringMethod
        self.distanceMatrix = distanceMatrix
        self.minClusters = minClusters
        self.maxClusters = maxClusters
        self.iterations = iterations
        self.properties = properties
        self.strategies = strategies
        self.allModels = allModels
        self.highlightedModels = highlightedModels

        args = [
            self.root,
            self.benchmark,
            self.folder2d,
            self.folderDistMatr,
            self.chartType,
            self.layoutCurve,
            self.clusteringMethod,
            self.distanceMatrix,
            self.minClusters,
            self.maxClusters,
            self.iterations,
            str(self.properties),
            str(self.strategies),
            self.allModels,
            self.highlightedModels]

        image = Path(
            "C:/Users/k/Documents/Unicamp/IC/rv_webviz_celmar/reservoirviewer_webviz/webviz_plugin_boilerplate/plugins/RV/generated/teste.png")

        self.image_url = WEBVIZ_ASSETS.add(image)
        rvConfig = Configuration(args)
        self.finalGrid = rvConfig.final
        self.set_callbacks(app)

    @property
    def layout(self):

        style = {
            "backgroundImage": f"url({self.image_url})",
            "height": f"1000px",
            "align-items": "center",
        }
        
        fig = px.imshow(self.finalGrid[1])

        teste = html.Div([dcc.Dropdown(
            id="my_dropdown",
            options=[{'label':'aaaaaaa','value':0}], style={"width":"50%"}),
            dcc.Graph(id="graph")]
        )

        teste2 = wcc.FlexBox(teste)
        return teste2
    
    def set_callbacks(self, app):
        @app.callback(
            Output("graph", "figure"), 
            [Input("my_dropdown","value")])
        
        def filter_heatmap(my_dropdown):
            df = self.finalGrid[0]
            print(df,"5")
            
            heatmap = px.imshow(df, label=my_dropdown)
            
            # heatmap.show()
            
            return heatmap
    
    # def plugin_callbacks():
    #     @callback(
    #         Output("graph", "figure"), 
    #         Input("value"))
        
    #     def filter_heatmap():
    #         df = px.data.medals_wide(self.finalGrid[0]) # replace with your own data source
    #         fig = px.imshow(df)
    #         return fig