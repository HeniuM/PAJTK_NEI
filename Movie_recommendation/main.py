import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


# Ładowanie danych
def load_data():
    """
    Wczytuje dane z plików CSV i zwraca DataFrame'y dla użytkowników, filmów oraz ocen.

    Returns:
        users_df (DataFrame): DataFrame zawierający ID użytkownika oraz jego nazwisko.
        movies_df (DataFrame): DataFrame zawierający ID filmu, tytuł oraz ID użytkownika, który dodał film.
        ratings_df (DataFrame): DataFrame zawierający ID użytkownika, ID filmu oraz przypisaną ocenę.
    """
    users_df = pd.read_csv('users.csv')
    movies_df = pd.read_csv('movies.csv')
    ratings_df = pd.read_csv('ratings.csv')
    return users_df, movies_df, ratings_df


# Tworzenie macierzy user-item
def create_user_item_matrix(ratings_df):
    """
    Tworzy macierz user-item na podstawie danych o ocenach, gdzie wiersze reprezentują użytkowników,
    kolumny filmy, a wartości to oceny przypisane przez użytkowników.

    Args:
        ratings_df (DataFrame): DataFrame zawierający oceny użytkowników dla filmów.

    Returns:
        user_movie_matrix (DataFrame): Macierz user-item z ocenami.
    """
    user_movie_matrix = ratings_df.pivot(index='user_id', columns='movie_id', values='rating').fillna(0)
    return user_movie_matrix


# Obliczanie podobieństwa między użytkownikami
def calculate_user_similarity(user_movie_matrix):
    """
    Oblicza macierz podobieństwa między użytkownikami przy użyciu cosinusowej miary podobieństwa.

    Args:
        user_movie_matrix (DataFrame): Macierz user-item z ocenami.

    Returns:
        user_similarity (ndarray): Macierz podobieństwa między użytkownikami.
    """
    user_similarity = cosine_similarity(user_movie_matrix)
    return user_similarity


# Rekomendowanie filmów dla użytkownika
def get_recommendations(user_id, user_similarity, user_movie_matrix, movies_df, n=5):
    """
    Generuje rekomendacje filmowe dla danego użytkownika na podstawie podobnych użytkowników,
    z wykluczeniem filmów dodanych przez samego użytkownika.

    Args:
        user_id (int): ID użytkownika docelowego.
        user_similarity (ndarray): Macierz podobieństwa między użytkownikami.
        user_movie_matrix (DataFrame): Macierz user-item z ocenami.
        movies_df (DataFrame): DataFrame zawierający informacje o filmach, w tym ID użytkownika, który dodał film.
        n (int): Liczba rekomendacji do wygenerowania.

    Returns:
        recommendations (list): Lista rekomendowanych ID filmów.
    """
    similar_users = np.argsort(-user_similarity[user_id-1])[1:n+1]  # Znajdź najbardziej podobnych użytkowników
    movie_scores = {}

    for sim_user in similar_users:
        sim_user_ratings = user_movie_matrix.iloc[sim_user]
        for movie_id, rating in sim_user_ratings.items():  # Zmiana iteritems() na items()
            # Sprawdzenie, czy użytkownik ocenił film i czy użytkownik docelowy nie dodał filmu
            if user_movie_matrix.loc[user_id, movie_id] == 0 and movies_df[movies_df['movie_id'] == movie_id]['added_by'].values[0] != user_id:
                if movie_id not in movie_scores:
                    movie_scores[movie_id] = 0
                movie_scores[movie_id] += rating  # Sumowanie ocen

    # Sortowanie filmów po ocenach i wybór top N
    recommendations = sorted(movie_scores, key=movie_scores.get, reverse=True)[:n]
    return recommendations


# Antyrekomendacje dla użytkownika
def get_anti_recommendations(user_id, user_similarity, user_movie_matrix, movies_df, n=5):
    """
    Generuje antyrekomendacje (filmy do unikania) dla danego użytkownika na podstawie ocen podobnych użytkowników,
    z wykluczeniem filmów dodanych przez samego użytkownika.

    Args:
        user_id (int): ID użytkownika docelowego.
        user_similarity (ndarray): Macierz podobieństwa między użytkownikami.
        user_movie_matrix (DataFrame): Macierz user-item z ocenami.
        movies_df (DataFrame): DataFrame zawierający informacje o filmach, w tym ID użytkownika, który dodał film.
        n (int): Liczba antyrekomendacji do wygenerowania.

    Returns:
        anti_recommendations (list): Lista ID filmów, które użytkownik powinien unikać.
    """
    similar_users = np.argsort(-user_similarity[user_id-1])[1:n+1]
    movie_scores = {}

    for sim_user in similar_users:
        sim_user_ratings = user_movie_matrix.iloc[sim_user]
        for movie_id, rating in sim_user_ratings.items():  # Zmiana iteritems() na items()
            # Sprawdzenie, czy użytkownik ocenił film i czy użytkownik docelowy nie dodał filmu
            if user_movie_matrix.loc[user_id, movie_id] == 0 and movies_df[movies_df['movie_id'] == movie_id]['added_by'].values[0] != user_id:
                if movie_id not in movie_scores:
                    movie_scores[movie_id] = 0
                movie_scores[movie_id] += rating  # Sumowanie ocen

    # Sortowanie filmów po ocenach i wybór najniżej ocenianych N
    anti_recommendations = sorted(movie_scores, key=movie_scores.get)[:n]
    return anti_recommendations


# Główna funkcja do uruchomienia systemu rekomendacji
def main():
    """
    Główna funkcja uruchamiająca system rekomendacji filmów.
    Ładuje dane, tworzy macierz user-item, oblicza podobieństwo między użytkownikami,
    a następnie generuje rekomendacje i antyrekomendacje dla przykładowego użytkownika.
    """
    # Ładowanie danych
    users_df, movies_df, ratings_df = load_data()

    # Tworzenie macierzy user-item
    user_movie_matrix = create_user_item_matrix(ratings_df)

    # Obliczanie podobieństwa użytkowników
    user_similarity = calculate_user_similarity(user_movie_matrix)

    # Generowanie rekomendacji i antyrekomendacji dla użytkownika o ID 1
    user_id = 2
    recommendations = get_recommendations(user_id, user_similarity, user_movie_matrix, movies_df)
    anti_recommendations = get_anti_recommendations(user_id, user_similarity, user_movie_matrix, movies_df)

    # Wyświetlenie wyników
    print("Rekomendacje dla użytkownika {}:".format(user_id))
    print([movies_df[movies_df['movie_id'] == movie_id]['title'].values[0] for movie_id in recommendations])

    print("\nAntyrekomendacje dla użytkownika {}:".format(user_id))
    print([movies_df[movies_df['movie_id'] == movie_id]['title'].values[0] for movie_id in anti_recommendations])


# Uruchomienie głównej funkcji
if __name__ == "__main__":
    main()
