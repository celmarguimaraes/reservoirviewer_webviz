from .pixelization import Pixelization
from .small_multiples import SmallMultiples


class rvconfig:
    def __init__(self, configs):
        self.root = configs[0]
        self.folder2d = configs[1]
        self.chart_type = configs[2]
        self.layout_curve = configs[3]
        self.clust_method = configs[4]
        self.min_clusters = int(configs[5])
        self.max_clusters = int(configs[6])
        self.num_iterations = int(configs[7])
        self.file2d = configs[8]
        self.save_dir = configs[9]
        self.color_map = configs[10]

        settingDrawConfigs(self, self.num_iterations, self.max_clusters)


def settingDrawConfigs(self, iterations, max_clusters):
    file_2d_path = self.root + "/" + self.folder2d + "/" + self.file2d
    if self.chart_type == "pixelization":
        print("Executing Pixelization")
        pixelization = Pixelization(file_2d_path, self.layout_curve)
        pixelization.generate_image(
            self.save_dir, self.color_map, iterations, max_clusters
        )

    elif self.chart_type == "smallmultiples":
        print("Executing Small Multiples")
        smallMultiples = SmallMultiples(file_2d_path, self.layout_curve)
        smallMultiples.draw_small_multiples(
            self.save_dir, self.color_map, iterations, max_clusters
        )
    else:
        raise Exception(
            "Visualization type not recognized. Please choose between Pixelization and Smallmultiples"
        )
