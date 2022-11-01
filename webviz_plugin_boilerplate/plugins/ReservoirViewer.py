import os
from pathlib import Path
from dash import Dash, dcc, html, Input, Output, ctx
from webviz_config import WebvizPluginABC
from .RV.RVConfig import Configuration
from webviz_config.webviz_assets import WEBVIZ_ASSETS
from dash import callback
import webviz_core_components as wcc


class ReservoirViewer(WebvizPluginABC):

    def __init__(self, app) -> None:

        super().__init__()

        ## IDs of the inputs
        self.input_root = "input-root"
        self.input_benchmark = "input-benchmark"
        self.input_folder2d = "input-folder2d"
        self.input_folderDistMatr = "input-folderDistMatr"
        self.input_chartType = "input-chartType"
        self.input_layoutCurve = "input-layoutCurve"
        self.input_clusteringMethod = "input-clusteringMethod"
        self.input_distanceMatrix = "input-distanceMatrix"
        self.input_minClusters = "input-minClusters"
        self.input_maxClusters = "input-maxClusters"
        self.input_iterations = "input-iterations"
        self.input_property_name = "input-property-name"
        self.input_property_file = "input-property-file"
        self.input_property_file_2d = "input-property-file-2d"
        self.input_property_dist_matrix = "input-property-dist-matrix"
        self.input_property_sorting_alg = "input-property-sorting-alg"
        self.input_property_file_feat_vect = "property-file-feat-vect"
        self.input_strategy_name= "input-strategy-name"
        self.input_strategy_folder= "input-strategy-folder"
        self.input_allModels = "input-allModels"
        self.input_highlightedModels = "input-highlightedModels"
        self.button_id = "submit-button"
        self.div_id = "output-state}"

        self.input_list = {
                        self.input_root: "root path",
                        self.input_benchmark: "benchmark",
                        self.input_folder2d: "export 2d folder name",
                        self.input_folderDistMatr: "distance matrix folder name",
                        self.input_chartType: "chart type",
                        self.input_layoutCurve: "layout curve",
                        self.input_clusteringMethod: "clustering method",
                        self.input_distanceMatrix: "distance matrix path",
                        self.input_minClusters: "minimum number of clusters",
                        self.input_maxClusters: "maximum number of clusters",
                        self.input_iterations: "number of iterations",
                        self.input_property_name: "property name",
                        self.input_property_file: "property file",
                        self.input_property_file_2d: "property file-2d",
                        self.input_property_dist_matrix: "property distance matrix file",
                        self.input_property_sorting_alg: "property sorting algorithm" ,
                        self.input_property_file_feat_vect: "property feature vectors file",
                        self.input_strategy_name: "strategy name",
                        self.input_strategy_folder: "strategy folder",
                        self.input_allModels: "all models txt file",
                        self.input_highlightedModels: "highlighted models file"}

        self.set_callbacks()

    @property
    def layout(self):
        style = {
            "height": f"2.5em",
            "align-items": "center",
            "margin": "1em"
        }

        return html.Div([
            wcc.FlexBox([
                html.Div([
                    dcc.Input(
                         id=i,
                         type="text",
                         placeholder="Insert {} here".format(
                             self.input_list[i]),
                         debounce=False,
                         autoComplete="on",
                         required=True,
                         size="60",
                         style=style,
                         ),
                ]) for i in self.input_list #iterate through the list of IDs to create all the text boxes
            ]),

            html.Br(),
            html.Button(id=self.button_id, n_clicks=0, children="Submit"),
            html.Div(id=self.div_id),

        ])

    def set_callbacks(self):
        @callback(
            Output(self.div_id, "children"),
            [
                Input(self.input_root, "value"), Input(self.input_benchmark, "value"),
                Input(self.input_folder2d, "value"), Input(self.input_folderDistMatr, "value"),
                Input(self.input_chartType, "value"), Input(self.input_layoutCurve, "value"),
                Input(self.input_clusteringMethod, "value"), Input(self.input_distanceMatrix, "value"), 
                Input(self.input_minClusters, "value"), Input(self.input_maxClusters, "value"),
                Input(self.input_iterations, "value"), Input(self.input_property_name, "value"),
                Input(self.input_property_dist_matrix, "value"), Input(self.input_property_file, "value"),
                Input(self.input_property_file_2d, "value"), Input(self.input_property_sorting_alg, "value"),
                 Input(self.input_property_file_feat_vect, "value"), Input(self.input_strategy_name, "value"), 
                Input(self.input_strategy_folder, "value"), Input(self.input_allModels, "value"),
                Input( self.input_highlightedModels, "value"), Input((self.button_id), "n_clicks")
             ]
        )
        def update_text(root: Path,
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
                        property_name: str, 
                        property_function: str, 
                        property_file: str, 
                        property_file_dist_matrix: str,
                        property_sorting_alg: str,
                        property_file_feat_vect: str,
                        strategy_name: str,
                        strategy_folder: str,
                        allModels: Path,
                        highlightedModels: str,
                        button: int):
            if (self.button_id == ctx.triggered_id): # if the submit button is clicked

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
                self.property_name = property_name
                self.property_function =property_function
                self.property_file = property_file
                self.property_file_dist_matrix = property_file_dist_matrix
                self.property_sorting_alg = property_sorting_alg,
                self.property_file_feat_vect = property_file_feat_vect,
                self.strategy_name = strategy_name
                self.strategy_folder = strategy_folder
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
                    self.property_name,
                    self.property_function,
                    self.property_file,
                    self.property_file_dist_matrix,
                    self.property_sorting_alg,
                    self.property_file_feat_vect,
                    self.strategy_name,
                    self.strategy_folder,
                    self.allModels,
                    self.highlightedModels]


                rvConfig = Configuration(args)
                
                if(self.chartType == "smallmultiples"):
                    image = Path("C:/Users/k/Documents/Unicamp/IC/rv_webviz_celmar/reservoirviewer_webviz/webviz_plugin_boilerplate/plugins/RV/generated/sm0.png")
                    self.image_url = WEBVIZ_ASSETS.add(image)
                
                return html.Img(src=self.image_url)