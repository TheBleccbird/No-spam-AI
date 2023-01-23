import steps.data_understanding as du
import steps.data_preparation as dp
import steps.data_modeling as dm

dataset = du.data_understanding()
dp.data_preparation(dataset)
model, X_test_features, y_test, feature_extractor = dm.data_modeling()
