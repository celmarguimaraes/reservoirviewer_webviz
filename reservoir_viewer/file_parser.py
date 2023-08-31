from dash import callback
from dash import dcc, html, Input, Output, ctx
from webviz_config import WebvizPluginABC
from webviz_config.webviz_assets import WEBVIZ_ASSETS
from reservoir_viewer.src.parser.parse_prop_files import ParseProperties
from pathlib import Path

from reservoir_viewer.src.components.html_components import (
    get_inputs,
    get_section_title,
)


class FileParser(WebvizPluginABC):
    def __init__(self) -> None:
        super().__init__()
        self.input_file = "input-file-parser"
        self.file_property = "file-property-parser"
        self.directory_save = "directory-save-parser"
        self.div_id = "output-state-parser"
        self.button_id = "generate-file-parser"

        self.set_callbacks()

    @property
    def layout(self):
        return html.Div(
            [
                html.Div(
                    [
                        html.H6("File Parser"),
                        html.P(
                            "This plugin will parse the properties file and return the specified property below."
                        ),
                    ]
                ),
                html.Div(
                    [
                        get_inputs(
                            "input-file-parser",
                            "directory and file you wish to extract data from",
                            "Directory for File",
                        )
                    ]
                ),
                html.Div(
                    [
                        get_inputs(
                            "file-property-parser",
                            "desired property",
                            "Desired Property",
                        )
                    ]
                ),
                html.Div(
                    [
                        get_inputs(
                            "directory-save-parser",
                            "directory to save parsed file",
                            "Directory to Save File",
                        )
                    ]
                ),
                html.Div(
                    [
                        html.Button(
                            id="generate-file-parser", n_clicks=0, children="Generate"
                        ),
                        html.Div(
                            id=self.div_id,
                            children="File will be saved on your machine",
                        ),
                    ]
                ),
            ]
        )

    def set_callbacks(self):
        @callback(
            Output(self.div_id, "children"),
            [
                Input(self.input_file, "value"),
                Input(self.file_property, "value"),
                Input(self.directory_save, "value"),
                Input(self.button_id, "n_clicks"),
            ],
        )
        def generate(file: str, property_parser: str, save_dir: str, button: int):
            if self.button_id == ctx.triggered_id:
                self.input_file = Path(file)
                self.file_property = property_parser
                self.directory_save = Path(save_dir)

                parser = ParseProperties()
                parser.parse_file(self.directory_save, self.input_file, self.file_property)
