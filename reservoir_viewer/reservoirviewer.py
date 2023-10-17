import os
from pathlib import Path

from dash import callback
from dash import dcc, html, Input, Output, ctx
from webviz_config import WebvizPluginABC
from webviz_config.webviz_assets import WEBVIZ_ASSETS

from reservoir_viewer.src.components.components_style import (
    get_section_div_style,
    get_dropdown_style,
)
from reservoir_viewer.src.components.html_components import (
    get_inputs,
    get_section_title,
)
from reservoir_viewer.src.rvconfig import rvconfig


class ReservoirViewer(WebvizPluginABC):
    def __init__(self) -> None:
        super().__init__()

        # IDs of the inputs
        self.input_root = "input-root"
        self.input_folder2d = "input-folder2d"
        self.input_chart_type = "input-chart_type"
        self.input_layout_curve = "input-layout_curve"
        self.input_clustering_method = "input-clustering_method"
        self.input_min_clusters = "input-min_clusters"
        self.input_max_clusters = "input-max_clusters"
        self.input_iterations = "input-iterations"
        self.input_property_file_2d = "input-property-file-2d"
        self.input_property_sorting_alg = "input-property-sorting-alg"
        self.button_id = "submit-button"
        self.div_id = "output-state"
        self.input_directory_save = "directory-save"
        self.color_map = "dropdown-colormap"

        self.set_callbacks()

    @property
    def layout(self):
        return html.Div(
            [
                html.Div(
                    style=get_section_div_style(),
                    children=[
                        get_section_title("Folders Configuration"),
                        html.Div(get_inputs("input-root", "root path", "Path")),
                        html.Div(
                            get_inputs(
                                "input-folder2d",
                                "name of 2d file folder",
                                "Directory for 2D Files",
                            )
                        ),
                        html.Div(
                            get_inputs(
                                "directory-save",
                                "directory to save generated_images image",
                                "Directory to Save Folder",
                            )
                        ),
                    ],
                ),
                html.Div(
                    style=get_section_div_style(),
                    children=[
                        get_section_title("Files Configuration"),
                        html.Div(
                            get_inputs(
                                "input-property-file-2d",
                                "name of file-2d",
                                "Property 2D File",
                            )
                        ),
                    ],
                ),
                html.Div(
                    style=get_section_div_style(),
                    children=[
                        get_section_title("Clusters Configuration"),
                        html.Div(
                            get_inputs(
                                "input-clustering_method",
                                "clustering method",
                                "Clustering Method",
                            )
                        ),
                        html.Div(
                            get_inputs(
                                "input-min_clusters",
                                "minimum number of clusters",
                                "Number of Minimum Cluster",
                            )
                        ),
                        html.Div(
                            get_inputs(
                                "input-max_clusters",
                                "maximum number of clusters",
                                "Number of Maximum Cluster",
                            )
                        ),
                        html.Div(
                            get_inputs(
                                "input-iterations",
                                "number of iterations",
                                "Number of Iterations",
                            )
                        ),
                    ],
                ),
                html.Div(
                    style=get_section_div_style(),
                    children=[
                        get_section_title("Prop. Configuration"),
                        html.Div(
                            get_inputs(
                                "input-property-sorting-alg",
                                "sorting algorithm",
                                "Sorting Algorithm",
                            )
                        ),
                        html.Div(
                            [
                                dcc.Dropdown(
                                    style=get_dropdown_style(),
                                    placeholder="Select the Filling Curve",
                                    options=[
                                        {
                                            "label": "snake curve",
                                            "value": "snake curve",
                                        },
                                    ],
                                    id="input-layout_curve",
                                ),
                            ]
                        ),
                        html.Div(
                            [
                                dcc.Dropdown(
                                    style=get_dropdown_style(),
                                    placeholder="Select the Visualization Technique",
                                    options=[
                                        {
                                            "label": "Pixelization",
                                            "value": "pixelization",
                                        },
                                        {
                                            "label": "Smallmultiples",
                                            "value": "smallmultiples",
                                        },
                                    ],
                                    id="input-chart_type",
                                ),
                            ]
                        ),
                        html.Div(
                            [
                                dcc.Dropdown(
                                    style=get_dropdown_style(),
                                    placeholder="Select the Colormap",
                                    options=[
                                        {"label": "jet", "value": "jet"},
                                        {"label": "rainbow", "value": "rainbow"},
                                        {"label": "turbo", "value": "turbo"},
                                        {
                                            "label": "gist_rainbow",
                                            "value": "gist_rainbow",
                                        },
                                    ],
                                    id="dropdown-colormap",
                                ),
                            ]
                        ),
                    ],
                ),
                html.Br(),
                html.Div(
                    [
                        html.Button(id="submit-button", n_clicks=0, children="Submit"),
                        html.Div(id=self.div_id, children="Image will appear below"),
                    ]
                ),
            ]
        )

    def set_callbacks(self):
        @callback(
            Output(self.div_id, "children"),
            [
                Input(self.input_root, "value"),
                Input(self.input_folder2d, "value"),
                Input(self.input_chart_type, "value"),
                Input(self.input_layout_curve, "value"),
                Input(self.input_clustering_method, "value"),
                Input(self.input_min_clusters, "value"),
                Input(self.input_max_clusters, "value"),
                Input(self.input_iterations, "value"),
                Input(self.input_property_file_2d, "value"),
                Input(self.input_property_sorting_alg, "value"),
                Input(self.button_id, "n_clicks"),
                Input(self.input_directory_save, "value"),
                Input(self.color_map, "value"),
            ],
        )
        def update_text(
            root: Path,
            folder2d: str,
            chart_type: str,
            layout_curve: str,
            clustering_method: str,
            min_clusters: int,
            max_clusters: int,
            iterations: int,
            property_file: str,
            property_sorting_alg: str,
            button: int,
            directory_save: str,
            color_map: str,
        ):
            if self.button_id == ctx.triggered_id:  # if the submit button is clicked
                self.root = root
                self.folder2d = folder2d
                self.chart_type = chart_type
                self.layout_curve = layout_curve
                self.clustering_method = clustering_method
                self.min_clusters = min_clusters
                self.max_clusters = max_clusters
                self.iterations = iterations
                self.property_file = property_file
                self.property_sorting_alg = (property_sorting_alg,)
                self.directory_save = directory_save
                self.color_map = color_map

                args = [
                    self.root,
                    self.folder2d,
                    self.chart_type,
                    self.layout_curve,
                    self.clustering_method,
                    self.min_clusters,
                    self.max_clusters,
                    self.iterations,
                    self.property_file,
                    self.property_sorting_alg,
                    self.directory_save,
                    self.color_map,
                ]

                rv_config = rvconfig(args)
                full_path = os.path.realpath(__file__)

                if self.chart_type == "smallmultiples":
                    path = (
                        os.path.dirname(full_path)
                        + "//generated_images//sm"
                        + str(0)
                        + ".png"
                    )
                    image = Path(path)
                    self.image_url = WEBVIZ_ASSETS.add(image)

                if self.chart_type == "pixelization":
                    image = Path(rv_config.save_dir)
                    self.image_url = WEBVIZ_ASSETS.add(image)

                div_style = {
                    "width": "80vw",
                    "align-items": "center",
                    "margin": "0.5em",
                }

                return html.Img(src=self.image_url, style=div_style)
