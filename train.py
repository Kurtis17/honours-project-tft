from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, mean_squared_error, r2_score, make_scorer
from sklearn.impute import SimpleImputer
from category_encoders import BinaryEncoder
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler
import pandas as pd

control = "4"

data = pd.read_csv('train data/training.csv')

imputer = SimpleImputer(strategy='constant', fill_value="none")
imputed_data = imputer.fit_transform(data)

imputed_df = pd.DataFrame(imputed_data, columns=data.columns)

X = imputed_df.iloc[:, :-1].values
Y = imputed_df.iloc[:, -1].astype(int).values

encoder = BinaryEncoder()
X = encoder.fit_transform(X)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

if control == "1":
    rf_class_model = RandomForestClassifier(n_estimators=80, random_state=0)

    rf_class_model.fit(X_train, Y_train)
    Y_pred = rf_class_model.predict(X_test)

    acc = accuracy_score(Y_test, Y_pred)
    precision = precision_score(Y_test, Y_pred, average='weighted')

    cv = cross_val_score(rf_class_model, X, Y, cv=5, scoring='accuracy')

    print("Accuracy:", acc)
    print("Precision:", precision)
    print("Cross-Validation Scores:", cv.mean())

elif control == "2":
    rf_regress_model = RandomForestRegressor(n_estimators=100, random_state=0)

    rf_regress_model.fit(X_train, Y_train)
    Y_pred = rf_regress_model.predict(X_test)
    rmse = mean_squared_error(Y_test, Y_pred, squared=False)
    r_squared = r2_score(Y_test, Y_pred)

    temp_r2 = make_scorer(r2_score)
    cv = cross_val_score(rf_regress_model, X, Y, cv=5, scoring=temp_r2)

    print("RMSE:", rmse)
    print("R2:", r_squared)
    print("Cross-Validation Scores:", cv.mean())

elif control == "3":
    knn_model = KNeighborsRegressor(n_neighbors=22)
    knn_model.fit(X_train, Y_train)

    Y_pred = knn_model.predict(X_test)

    rmse = mean_squared_error(Y_test, Y_pred, squared=False)
    r_squared = r2_score(Y_test, Y_pred)

    temp_r2 = make_scorer(r2_score)
    cv = cross_val_score(knn_model, X, Y, cv=5, scoring=temp_r2)

    print("RMSE:", rmse)
    print("R2:", r_squared)
    print("Cross-Validation Scores:", cv.mean())

elif control == "4":

    fnn_model = MLPClassifier(hidden_layer_sizes=(1276, 316, 79, 158, 158, 63),
                              activation='relu', solver='adam', random_state=0)
    fnn_model.fit(X_train, Y_train)

    Y_pred = fnn_model.predict(X_test)

    acc = accuracy_score(Y_test, Y_pred)
    precision = precision_score(Y_test, Y_pred, average='weighted')

    cv = cross_val_score(fnn_model, X, Y, cv=5, scoring='accuracy')

    print("Accuracy:", acc)
    print("Precision:", precision)
    print("Cross-Validation Scores:", cv.mean())