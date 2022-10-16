import os
from dash import html
import subprocess as sub
from webviz_config import WebvizPluginABC
from .RV.RVConfig import Configuration


class ReservoirViewer(WebvizPluginABC):

    def __init__(self,
                 root: str,
                 benchmark: str,
                 folder2d: str,
                 folderDistMatr: str,
                 chartType: str,
                 layoutCurve: str,
                 clusteringMethod: str,
                 distanceMatrix: str,
                 minClusters: int,
                 maxClusters: int,
                 iterations: int,
                 properties: list,
                 strategies: list,
                 allModels: str,
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
        
        rvConfig = Configuration(args)

    @property
    def layout(self):
        return (html.Div(
            [self.root,
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
             self.allModels,
             self.highlightedModels]
        )
    )
