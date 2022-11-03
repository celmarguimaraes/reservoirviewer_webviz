import os
from pathlib import Path
from dash import html
import subprocess as sub
from webviz_config import WebvizPluginABC
from .RV.RVConfig import Configuration
from webviz_config.webviz_assets import WEBVIZ_ASSETS


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
        
        image = Path("C:/Users/k/Documents/Unicamp/IC/rv_webviz_celmar/reservoirviewer_webviz/webviz_plugin_boilerplate/plugins/RV/generated/teste0.png")

        self.image_url = WEBVIZ_ASSETS.add(image)
        rvConfig = Configuration(args)
        

    @property
    def layout(self):

        style = {
            "backgroundImage": f"url({self.image_url})",
            "height": f"500px",
            "align-items": "center",
        }

        return html.Div(
            "teste imagem", style=style
        )
