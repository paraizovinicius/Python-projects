import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score



def load_data():
    # Abre o arquivo unpopspotify.csv
    df = pd.read_csv("C:\\Users\\parai\\Downloads\\unpopular_songs_full.csv")

    # Supprimer la collone
    df = df.drop(['Unnamed: 17', 'track_id', 'track_name', 'track_artist'], axis=1)

    # imput les valeurs manquantes
    df.fillna(df.mean(), inplace=True)
    df['explicit'] = df['explicit'].fillna(df['explicit'].mode()[0])

    # Séparer les features et variable cible
    features = df.drop('popularity', axis=1)
    target = df['popularity']

    return features, target

def train_and_evaluate_model(features, target, n_neighbors=5):
   
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2) #trainning et test sets

    # KNeighborsClassifier model
    knn_classifier = KNeighborsClassifier(n_neighbors=n_neighbors)
    knn_classifier.fit(X_train, y_train) # fit into the data

    y_pred = knn_classifier.predict(X_test) # faire le prédiction
    accuracy = accuracy_score(y_test, y_pred) # calculer la précision
    print("Accuracy:", accuracy)

    scores = cross_val_score(knn_classifier, features, target, cv=5) #
    mean_accuracy = scores.mean()
    std_deviation = scores.std()
    print("Mean accuracy of cross validation:", mean_accuracy, "Standard deviation:", std_deviation)

if __name__ == "__main__":
    features, target = load_data()
    train_and_evaluate_model(features, target)