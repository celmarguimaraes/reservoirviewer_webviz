import numpy as np


class ClusterizationUtils:
    def __init__(self, models_vector):
        self.models_vector = models_vector

    def create_feature_vector(self, min, max):
        feature_vector = []
        for model in self.models_vector:
            model_feature_vector = self.get_model_summarization(model, min, max)
            feature_vector.append(model_feature_vector)

        return feature_vector

    def get_model_summarization(self, model, min, max):
        high_values = []
        intermediary_values = []
        low_values = []

        self.get_values_from_models(model, high_values, intermediary_values, low_values, min, max)

        inverted_model = np.transpose(model)
        self.get_values_from_models(
            inverted_model, high_values, intermediary_values, low_values, min, max
        )

        return high_values + intermediary_values + low_values

    def get_values_from_models(
        self, model, high_values, intermediary_values, low_values, min, max
    ):
        for i in model:
            high = 0
            intermediary = 0
            low = 0
            for j in i:
                if (j >= min and j < max/3):
                    low = low + 1
                elif j >= max/3 and j <= (2*max)/3:
                    intermediary = intermediary + 1
                elif j > (2*max)/3:
                    high = high + 1

            high_values.append(high)
            intermediary_values.append(intermediary)
            low_values.append(low)
