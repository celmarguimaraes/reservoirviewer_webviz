import os
from pathlib import Path

from dash import callback
from dash import dcc, html, Input, Output, ctx
from webviz_config import WebvizPluginABC
from webviz_config.webviz_assets import WEBVIZ_ASSETS

from .RV.rvconfig import rvconfig


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
        self.input_property_function = "input-property-file"
        self.input_property_file_2d = "input-property-file-2d"
        self.input_property_dist_matrix = "input-property-dist-matrix"
        self.input_property_sorting_alg = "input-property-sorting-alg"
        self.input_property_file_feat_vect = "property-file-feat-vect"
        self.input_strategy_name = "input-strategy-name"
        self.input_strategy_folder = "input-strategy-folder"
        self.input_all_models = "input-all_models"
        self.input_highlighted_models = "input-highlighted_models"
        self.button_id = "submit-button"
        self.div_id = "output-state"
        self.input_directory_save = "directory-save"
        self.color_map = "dropdown-colormap"

        self.set_callbacks()

    @property
    def layout(self):
        style = {"height": f"2.5em", "align-items": "center", "margin": "0.8em"}

        def get_text_input(div_id: str, placeholder_text: str):
            return dcc.Input(
                id=div_id,
                type="text",
                placeholder=placeholder_text,
                debounce=False,
                autoComplete="on",
                required=False,
                size="100",
                style=style,
            )

        return html.Div(
            [
                html.Div(get_text_input("input-root", "root path")),
                html.Div(get_text_input("input-benchmark", "benchmark")),
                html.Div(get_text_input("input-folder2d", "name of 2d file folder")),
                html.Div(get_text_input("input-folder_Dist_Matr", "distance matrix folder name")),
                html.Div(get_text_input("input-clustering_method", "clustering method")),
                html.Div(get_text_input("input-distance_matrix", "distance matrix")),
                html.Div(get_text_input("input-min_clusters", "minimum number of clusters")),
                html.Div(get_text_input("input-max_clusters", "maximum number of clusters")),
                html.Div(get_text_input("input-iterations", "number of iterations")),
                html.Div(get_text_input("input-property-name", "property name")),
                html.Div(get_text_input("input-property-file", "coordinate suppression function")),
                html.Div(get_text_input("input-property-file-2d", "name of file-2d")),
                html.Div(get_text_input("input-property-dist-matrix", "name of distance matrix file")),
                html.Div(get_text_input("input-property-sorting-alg", "sorting algorithm")),
                html.Div(get_text_input("property-file-feat-vect", "name of feature vector file")),
                html.Div(get_text_input("input-strategy-name", "strategy name")),
                html.Div(get_text_input("input-strategy-folder", "strategy path to folder")),
                html.Div(get_text_input("input-all_models", "name of txt file with all models")),
                html.Div(get_text_input("input-highlighted_models", "name of highlighted models files")),
                html.Div(get_text_input("directory-save", "directory to save generated image")),
                html.Br(),
                html.Div(
                    [
                        dcc.Dropdown(
                            placeholder="Select the curve",
                            options=[
                                {'label': 'snake curve', 'value': 'snake curve'},
                            ],
                            id="input-layout_curve"
                        ),
                    ]
                ),
                html.Div(
                    [
                        dcc.Dropdown(
                            placeholder="Select the visualization technique",
                            options=[
                                {'label': 'Pixelization', 'value': 'pixelization'},
                                {'label': 'Smallmultiples', 'value': 'smallmultiples'},
                            ],
                            id="input-chart_type"
                        ),
                    ]
                ),
                html.Div(
                    [
                        dcc.Dropdown(
                            placeholder="Select the colormap",
                            options=[
                                {'label': 'jet', 'value': 'jet'},
                                {'label': 'rainbow', 'value': 'rainbow'},
                                {'label': 'turbo', 'value': 'turbo'},
                                {'label': 'gist_rainbow', 'value': 'gist_rainbow'},
                            ],
                            id="dropdown-colormap"
                        ),
                    ]
                ),
                html.Div(
                    [
                        html.Button(id="submit-button", n_clicks=0, children="Submit"),
                        html.Div(id=self.div_id, children="Image will appear below"),
                    ]
                ),
                html.Div(id=self.div_id),
            ]
        )

    def set_callbacks(self):
        @callback(
            Output(self.div_id, "children"),
            [
                Input(self.input_root, "value"),
                Input(self.input_benchmark, "value"),
                Input(self.input_folder2d, "value"),
                Input(self.input_folder_Dist_Matr, "value"),
                Input(self.input_chart_type, "value"),
                Input(self.input_layout_curve, "value"),
                Input(self.input_clustering_method, "value"),
                Input(self.input_distance_matrix, "value"),
                Input(self.input_min_clusters, "value"),
                Input(self.input_max_clusters, "value"),
                Input(self.input_iterations, "value"),
                Input(self.input_property_name, "value"),
                Input(self.input_property_function, "value"),
                Input(self.input_property_file_2d, "value"),
                Input(self.input_property_dist_matrix, "value"),
                Input(self.input_property_sorting_alg, "value"),
                Input(self.input_property_file_feat_vect, "value"),
                Input(self.input_strategy_name, "value"),
                Input(self.input_strategy_folder, "value"),
                Input(self.input_all_models, "value"),
                Input(self.input_highlighted_models, "value"),
                Input(self.button_id, "n_clicks"),
                Input(self.input_directory_save, "value"),
                Input(self.color_map, "value"),
            ],
        )
        def update_text(
                root: Path,
                benchmark: str,
                folder2d: str,
                folder_Dist_Matr: str,
                chart_type: str,
                layout_curve: str,
                clustering_method: str,
                distance_matrix: str,
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
                all_models: str,
                highlighted_models: str,
                button: int,
                directory_save: str,
                color_map: str
        ):
            if self.button_id == ctx.triggered_id:  # if the submit button is clicked

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
                self.property_function = property_function
                self.property_file = property_file
                self.property_file_dist_matrix = property_file_dist_matrix
                self.property_sorting_alg = (property_sorting_alg,)
                self.property_file_feat_vect = (property_file_feat_vect,)
                self.strategy_name = strategy_name
                self.strategy_folder = strategy_folder
                self.all_models = all_models
                self.highlighted_models = highlighted_models
                self.directory_save = directory_save
                self.color_map = color_map

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
                    self.highlighted_models,
                    self.directory_save,
                    self.color_map
                ]

                rvConfig = rvconfig(args)

                full_path = os.path.realpath(__file__)

                if self.chart_type == "smallmultiples":
                    path = (
                            os.path.dirname(full_path) + "//generated//sm" + str(0) + ".png"
                    )
                    image = Path(path)
                    self.image_url = WEBVIZ_ASSETS.add(image)

                if self.chart_type == "pixelization":
                    image = Path(rvConfig.save_dir)
                    self.image_url = WEBVIZ_ASSETS.add(image)

                div_style = {
                    "width": "80vw",
                    "align-items": "center",
                    "margin": "0.5em",
                }

                return html.Img(src=self.image_url, style=div_style)
