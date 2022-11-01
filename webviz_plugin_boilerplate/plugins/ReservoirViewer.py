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
        self.input_folder_Dist_Matr = "input-folder_Dist_Matr"
        self.input_chart_type = "input-chart_type"
        self.input_layout_curve = "input-layout_curve"
        self.input_clustering_method = "input-clustering_method"
        self.input_distance_matrix = "input-distance_matrix"
        self.input_min_clusters = "input-min_clusters"
        self.input_max_clusters = "input-max_clusters"
        self.input_iterations = "input-iterations"
        self.input_property_name = "input-property-name"
        self.input_property_file = "input-property-file"
        self.input_property_file_2d = "input-property-file-2d"
        self.input_property_dist_matrix = "input-property-dist-matrix"
        self.input_property_sorting_alg = "input-property-sorting-alg"
        self.input_property_file_feat_vect = "property-file-feat-vect"
        self.input_strategy_name= "input-strategy-name"
        self.input_strategy_folder= "input-strategy-folder"
        self.input_all_models = "input-all_models"
        self.input_highlighted_models = "input-highlighted_models"
        self.button_id = "submit-button"
        self.div_id = "output-state}"

        self.input_list = {
                        self.input_root: "root path",
                        self.input_benchmark: "benchmark",
                        self.input_folder2d: "export 2d folder name",
                        self.input_folder_Dist_Matr: "distance matrix folder name",
                        self.input_chart_type: "chart type",
                        self.input_layout_curve: "layout curve",
                        self.input_clustering_method: "clustering method",
                        self.input_distance_matrix: "distance matrix path",
                        self.input_min_clusters: "minimum number of clusters",
                        self.input_max_clusters: "maximum number of clusters",
                        self.input_iterations: "number of iterations",
                        self.input_property_name: "property name",
                        self.input_property_file: "property file",
                        self.input_property_file_2d: "property file-2d",
                        self.input_property_dist_matrix: "property distance matrix file",
                        self.input_property_sorting_alg: "property sorting algorithm" ,
                        self.input_property_file_feat_vect: "property feature vectors file",
                        self.input_strategy_name: "strategy name",
                        self.input_strategy_folder: "strategy folder",
                        self.input_all_models: "all models txt file",
                        self.input_highlighted_models: "highlighted models file"}

        self.set_callbacks()

    @property
    def layout(self):
        style = {
            "height": f"2.5em",
            "align-items": "center",
            "margin": "1em"
        }
        
        div_style = {
            "width": "60vw",
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
                ]) for i in self.input_list # Iterate through the list of IDs to create all the text boxes
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
                Input(self.input_folder2d, "value"), Input(self.input_folder_Dist_Matr, "value"),
                Input(self.input_chart_type, "value"), Input(self.input_layout_curve, "value"),
                Input(self.input_clustering_method, "value"), Input(self.input_distance_matrix, "value"), 
                Input(self.input_min_clusters, "value"), Input(self.input_max_clusters, "value"),
                Input(self.input_iterations, "value"), Input(self.input_property_name, "value"),
                Input(self.input_property_dist_matrix, "value"), Input(self.input_property_file, "value"),
                Input(self.input_property_file_2d, "value"), Input(self.input_property_sorting_alg, "value"),
                 Input(self.input_property_file_feat_vect, "value"), Input(self.input_strategy_name, "value"), 
                Input(self.input_strategy_folder, "value"), Input(self.input_all_models, "value"),
                Input( self.input_highlighted_models, "value"), Input((self.button_id), "n_clicks")
             ]
        )
        def update_text(root: Path,
                        benchmark: str,
                        folder2d: Path,
                        folder_Dist_Matr: Path,
                        chart_type: str,
                        layout_curve: str,
                        clustering_method: str,
                        distance_matrix: Path,
                        min_clusters: int,
                        max_clusters: int,
                        iterations: int,
                        property_name: str, 
                        property_function: str, 
                        property_file: str, 
                        property_file_dist_matrix: str,
                        property_sorting_alg: str,
                        property_file_feat_vect: str,
                        strategy_name: str,
                        strategy_folder: str,
                        all_models: Path,
                        highlighted_models: str,
                        button: int):
            if (self.button_id == ctx.triggered_id): # if the submit button is clicked

                self.root = root
                self.benchmark = benchmark
                self.folder2d = folder2d
                self.folder_Dist_Matr = folder_Dist_Matr
                self.chart_type = chart_type
                self.layout_curve = layout_curve
                self.clustering_method = clustering_method
                self.distance_matrix = distance_matrix
                self.min_clusters = min_clusters
                self.max_clusters = max_clusters
                self.iterations = iterations
                self.property_name = property_name
                self.property_function =property_function
                self.property_file = property_file
                self.property_file_dist_matrix = property_file_dist_matrix
                self.property_sorting_alg = property_sorting_alg,
                self.property_file_feat_vect = property_file_feat_vect,
                self.strategy_name = strategy_name
                self.strategy_folder = strategy_folder
                self.all_models = all_models
                self.highlighted_models = highlighted_models

                args = [
                    self.root,
                    self.benchmark,
                    self.folder2d,
                    self.folder_Dist_Matr,
                    self.chart_type,
                    self.layout_curve,
                    self.clustering_method,
                    self.distance_matrix,
                    self.min_clusters,
                    self.max_clusters,
                    self.iterations,
                    self.property_name,
                    self.property_function,
                    self.property_file,
                    self.property_file_dist_matrix,
                    self.property_sorting_alg,
                    self.property_file_feat_vect,
                    self.strategy_name,
                    self.strategy_folder,
                    self.all_models,
                    self.highlighted_models]


                rvConfig = Configuration(args)
                
                if(self.chart_type == "smallmultiples"):
                    image = Path("C:/Users/k/Documents/Unicamp/IC/rv_webviz_celmar/reservoirviewer_webviz/webviz_plugin_boilerplate/plugins/RV/generated/sm0.png")
                    self.image_url = WEBVIZ_ASSETS.add(image)
                           
                div_style = {
                    "width": "80vw",
                    "align-items": "center",
                    "margin": "0.5em"
                }
                
                return html.Img(src=self.image_url, style=div_style)