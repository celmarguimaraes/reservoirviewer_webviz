# Reservoir Viewer for Web

## How to Run

### Pre-Requistes

-   Python Version 3.11 or above;
-   pip;

### Install the Libraries

The libraries are listed in the `requirements.txt` file. You can install them using the following command (assuming you are at the root folder `reservoirviewer_webviz`).

```
pip install -r .\requirement.txt
```

### Update for your modifications

When you change the code you can run the following command so the changes are applied.

```
pip install -e .
```

### Run Webviz

Assuming you have [Webviz](https://github.com/equinor/webviz-config) installed, you can run the following command (without the brackets) to start a local server with Reservoir Viewer for Web.

```
webviz build {path/to/config_file.yaml}
e.g. webviz build .\webviz_config_files\reservoir_viewer_example.yaml
```

## Current Limitations

### Issues with Cluster Separation

Currently the cluster separation on Small Multiples is not working as expected. It is possible to see that, on the image, the clusters is not well separated. It is visible that one or two models are part of the wrong cluster. Further debugging will be necessary to identify why that is happening but it may has something to do with the use of the space-filling curves.

### Issues with Space-Filling Curves

Currently, only the Snake Curve and Zhang curve is working on Pixelization and, on Small Multiples, only the Snake Curve works. The issue is that, at some point, a Out Of Bound Exception is being thrown. The code related to the space-filling curve tries to access a out of bound index.

### Deploy on the Cloud

The software generates an image and displays it on the screen. The way it does is by generating the image, saving it locally on the user's computer and then accessing it and displaying on the screen. Despite working as expected locally, it brings some issues when it comes to using it on the cloud.

First, it is necessary to consider several people using the software at the same time. Second, the images can only be accessed by the user who generated it. Third, the user may not inform a correct path to save and display the image.

## Future Works

-   Improve documentation;
-   Add support to new reservoir file formats;
-   Add interactivity on the image plot;
-   Add cluster separation within Small Multiples approach;
-   Represent sets of wells on Pixelization approach;
-   Include more space-filling curves to support Small Multiples and Pixelization techniques;
-   Provide other clustering algorithms to both visualization techniques;
-   Conduct a user-based evaluation of the current UI;
