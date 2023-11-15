import numpy as np


class ClusterizationUtils:
    def __init__(self, models_vector):
        self.models_vector = models_vector

    def create_feature_vector(self):
        feature_vector = []
        for model in self.models_vector:
            model_feature_vector = self.get_model_summarization(model)
            feature_vector.append(model_feature_vector)

        return feature_vector

    def get_value_classification(self, value, high, intermediary, low) -> None:
        if (value >= 0 and value < 266) or value == np.nan:
            low = low + 1
        elif value >= 266 and value <= 533:
            intermediary = intermediary + 1
        else:
            high = high + 1

    def get_model_summarization(self, model):
        high_values = []
        intermediary_values = []
        low_values = []

        self.get_values_from_models(model, high_values, intermediary_values, low_values)

        inverted_model = np.transpose(model)
        self.get_values_from_models(
            inverted_model, high_values, intermediary_values, low_values
        )

        return high_values + intermediary_values + low_values

    def get_values_from_models(
        self, model, high_values, intermediary_values, low_values
    ):
        for i in model:
            high = 0
            intermediary = 0
            low = 0
            for j in i:
                if (j >= 0 and j < 266):
                    low = low + 1
                elif j >= 266 and j <= 533:
                    intermediary = intermediary + 1
                elif j > 533:
                    high = high + 1

            high_values.append(high)
            intermediary_values.append(intermediary)
            low_values.append(low)
