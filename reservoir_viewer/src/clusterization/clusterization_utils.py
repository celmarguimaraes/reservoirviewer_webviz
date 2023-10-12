import numpy as np

class CLusterizationUtils:
    def __init__(self, models_vector):
        self.models_vector = models_vector

    def create_feature_vector(self, models_vector):
        feature_vector = []
        for model in models_vector:
            model_feature_vector = self.get_model_summarization(model)
            feature_vector.append(model_feature_vector)

        return feature_vector

    def normalize_column(self, data_frame, property):
        column_values = data_frame[property]
        data_frame[property] = (column_values - column_values.min())/(column_values.max() - column_values.min())

        return data_frame[property]

    def get_value_classification(self, value, high, intermediary, low) -> None:
        if(value >= 0 and value < 0.33):
            low = low + 1
        elif(value >= 0.33 and value <= 0.66):
            intermediary = intermediary + 1
        else:
            high = high + 1

    def get_model_summarization(self, model):
        high_values = []
        intermediary_values = []
        low_values = []

        self.get_values_from_models(model, high_values, intermediary_values, low_values)

        inverted_model = np.transpose(model)
        self.get_values_from_models(inverted_model, high_values, intermediary_values, low_values)

        return high_values + intermediary_values + low_values

    def get_values_from_models(self, model, high_values, intermediary_values, low_values):
        for i in model:
            high = 0
            intermediary = 0
            low = 0
            for j in i:
                self.get_value_classification(j, high, intermediary, low)

            high_values.append(high)
            intermediary_values.append(intermediary)
            low_values.append(low)