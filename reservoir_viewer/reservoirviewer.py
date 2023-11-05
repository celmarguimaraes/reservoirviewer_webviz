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
        self.input_max_clusters = "input-max_clusters"
        self.input_iterations = "input-iterations"
        self.input_property_file_2d = "input-property-file-2d"
        self.button_id = "submit-button"
        self.div_id = "output-state"
        self.input_directory_save = "directory-save"
        self.color_map = "dropdown-colormap"
        self.property_name = "property-name"

        self.set_callbacks()

    @property
    def layout(self):
        return html.Div(
            style={"display": "flex", "flex-direction": "row"},
            children=[
                html.Div(
                    style=get_section_div_style(),
                    children=[
                        get_section_title("Configurations"),
                        html.Div(
                            get_inputs(
                                "input-folder2d",
                                "e.g. C:/Users/youruser/folder",
                                "Path to 2D Files Folder",
                            )
                        ),
                        html.Div(
                            get_inputs(
                                "directory-save",
                                "e.g. C:/Users/youruser/save_images/my_image.png",
                                "Path to Save Folder",
                            )
                        ),
                        html.Div(
                            get_inputs(
                                "input-max_clusters",
                                "e.g. 5",
                                "Number of Maximum Cluster",
                            )
                        ),
                        html.Div(
                            get_inputs(
                                "property-name",
                                "e.g. GeometricMean",
                                "Property",
                            )
                        ),
                        html.Div(
                            [
                                html.P("Filling Curve"),
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
                                html.P("Visualization Technique"),
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
                                html.P("Colormap"),
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
                        html.Button(
                            id="submit-button", n_clicks=0, children="Generate Image"
                        ),
                        html.Div(id=self.div_id, children="Image will appear below"),
                    ],
                ),
            ],
        )

    def set_callbacks(self):
        @callback(
            Output(self.div_id, "children"),
            [
                Input(self.input_folder2d, "value"),
                Input(self.input_chart_type, "value"),
                Input(self.input_layout_curve, "value"),
                Input(self.input_max_clusters, "value"),
                Input(self.button_id, "n_clicks"),
                Input(self.input_directory_save, "value"),
                Input(self.color_map, "value"),
                Input(self.property_name, "value")
            ],
        )
        def update_text(
            folder2d: Path,
            chart_type: str,
            layout_curve: str,
            max_clusters: int,
            button: int,
            directory_save: str,
            color_map: str,
            property_name: str
        ):
            if self.button_id == ctx.triggered_id:  # if the submit button is clicked
                self.folder2d = folder2d
                self.chart_type = chart_type
                self.layout_curve = layout_curve
                self.max_clusters = max_clusters
                self.directory_save = directory_save
                self.color_map = color_map
                self.property_name = property_name

                args = [
                    self.folder2d,
                    self.chart_type,
                    self.layout_curve,
                    self.max_clusters,
                    self.directory_save,
                    self.color_map,
                    self.property_name
                ]

                rv_config = rvconfig(args)

                if self.chart_type == "smallmultiples":
                    image = Path(rv_config.save_dir)
                    self.image_url = WEBVIZ_ASSETS.add(image)

                if self.chart_type == "pixelization":
                    image = Path(rv_config.save_dir)
                    self.image_url = WEBVIZ_ASSETS.add(image)

                div_style = {
                    "width": "80vw",
                    "align-items": "right",
                    "margin": "0.5em",
                }

                return html.Img(src=self.image_url, style=div_style)
