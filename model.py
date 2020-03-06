def Predict(X_user) :
    # Libs
    import pandas as pd
    import numpy as np
    from sklearn.preprocessing import OneHotEncoder
    from sklearn.compose import ColumnTransformer
    from catboost import CatBoostClassifier

    X_user = np.array(X_user).reshape(1,-1)
    print(X_user)
    # Reading the dataset
    dataset = pd.read_csv("modified.csv")

    x = dataset.iloc[:,:-1].values
    y = dataset.iloc[:,-1].values

    x = np.concatenate((x, X_user))

    ct = ColumnTransformer(
        [('one_hot_encoder', OneHotEncoder(categories='auto'), [4])],   # The column numbers to be transformed (here is [0] but can be [0, 1, 3])
        remainder='passthrough'                                         # Leave the rest of the columns untouched
        )
    x = ct.fit_transform(x)

    x = x.astype(np.float64)

    X_train = x[:-1,:]
    Y_train = y
    X_test = x[-1:,:]

    # Catboost
    classifier1 = CatBoostClassifier()
    classifier1.fit(X_train, Y_train)

    pred1 = classifier1.predict(X_test)


    return pred1
