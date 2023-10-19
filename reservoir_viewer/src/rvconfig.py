from .pixelization import Pixelization
from .small_multiples import SmallMultiples


class rvconfig:
    def __init__(self, configs):
        self.folder2d = configs[0]
        self.chart_type = configs[1]
        self.layout_curve = configs[2]
        self.max_clusters = int(configs[3])
        self.num_iterations = int(configs[4])
        self.file2d = configs[5]
        self.save_dir = configs[6]
        self.color_map = configs[7]

        settingDrawConfigs(self, self.num_iterations, self.max_clusters)


def settingDrawConfigs(self, iterations, max_clusters):
    file_2d_path = self.folder2d + "/" + self.file2d
    if self.chart_type == "pixelization":
        print("Executing Pixelization")
        pixelization = Pixelization(file_2d_path, self.layout_curve)
        pixelization.generate_image(
            self.save_dir, self.color_map, iterations, max_clusters
        )

    elif self.chart_type == "smallmultiples":
        print("Executing Small Multiples")
        smallMultiples = SmallMultiples(file_2d_path)
        smallMultiples.draw_small_multiples(
            self.save_dir, self.color_map, iterations, max_clusters
        )
    else:
        raise Exception(
            "Visualization type not recognized. Please choose between Pixelization and Smallmultiples"
        )
