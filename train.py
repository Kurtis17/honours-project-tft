from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, accuracy_score, precision_score, r2_score
import category_encoders as ce
import joblib

binary_encoder = ce.BinaryEncoder

rf_class_model = RandomForestClassifier(n_estimators=100, random_state=17)
rf_regres_model = RandomForestRegressor(n_estimators=100, random_state=17)
knn_model = KNeighborsRegressor()
ffnn_model = MLPClassifier(hidden_layer_sizes=(100, 50,))

#joblib.dump(model, 'trained_model.joblib')