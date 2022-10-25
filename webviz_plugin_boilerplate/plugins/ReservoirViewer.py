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


class ReservoirViewer(WebvizPluginABC):

    def __init__(self,
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
            "C:/Users/k/Documents/Unicamp/IC/rv_webviz_celmar/reservoirviewer_webviz/webviz_plugin_boilerplate/plugins/RV/generated/teste0.png")

        self.image_url = WEBVIZ_ASSETS.add(image)
        rvConfig = Configuration(args)
        self.finalGrid = rvConfig.final

    @property
    def layout(self):

        # fig = make_subplots()

        # for s in range(9):
        #     grid = np.array(self.finalGrid[s])
        #     fig.add_trace(
        #         go.Figure(data=go.Heatmap(
        #             grid))
        #     )
            

        style = {
            "backgroundImage": f"url({self.image_url})",
            "height": f"500px",
            "align-items": "center",
        }
        
        fig = px.imshow(self.finalGrid[1])

        return html.Div(
            [
                html.H4('Olympic medals won by countries'),
                dcc.Graph(figure = fig),
            ]
        )

    # def plugin_callbacks():
    #     @callback(
    #         Output("graph", "figure"), 
    #         Input("value"))
        
    #     def filter_heatmap():
    #         df = px.data.medals_wide(self.finalGrid[0]) # replace with your own data source
    #         fig = px.imshow(df)
    #         return fig