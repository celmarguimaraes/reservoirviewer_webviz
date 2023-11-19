from .pixelization import Pixelization
from .small_multiples import SmallMultiples


class rvconfig:
    def __init__(self, configs):
        self.folder2d = configs[0]
        self.chart_type = configs[1]
        self.layout_curve = configs[2]
        self.max_clusters = int(configs[3])
        self.save_dir = configs[4]
        self.color_map = configs[5]
        self.property = configs[6]

        settingDrawConfigs(self, self.max_clusters)


def settingDrawConfigs(self, max_clusters):
    if self.chart_type == "pixelization":
        print("Executing Pixelization")
        pixelization = Pixelization(self.folder2d, self.layout_curve, self.property)
        pixelization.generate_image(self.save_dir, self.color_map, max_clusters)

    elif self.chart_type == "smallmultiples":
        print("Executing Small Multiples")
        smallMultiples = SmallMultiples(self.folder2d, self.layout_curve, self.property)
        smallMultiples.draw_small_multiples(self.save_dir, self.color_map, max_clusters)
    else:
        raise Exception(
            "Visualization type not recognized. Please choose between Pixelization and Smallmultiples"
        )
