from dash import dcc, html

from reservoir_viewer.src.components.components_style import (
    get_input_style,
    get_section_title_style,
    get_input_div_style,
)


def get_inputs(div_id: str, placeholder: str, label: str):
    return html.Div(
        html.Div(
            style=get_input_div_style(),
            children=[
                html.P(label),
                dcc.Input(
                    id=div_id,
                    type="text",
                    placeholder=placeholder,
                    debounce=False,
                    autoComplete="on",
                    required=False,
                    size="70",
                    style=get_input_style(),
                ),
            ],
        ),
    )


def get_section_title(label: str):
    return html.H6(style=get_section_title_style(), children=label)
