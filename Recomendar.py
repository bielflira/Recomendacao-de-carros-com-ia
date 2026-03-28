import numpy as np

class CarRecommender:
    def __init__(self, df):
        self.df = df.copy()

    def normalize(self):
        for col in ["economia", "conforto", "espaco"]:
            self.df[col] = (self.df[col] - self.df[col].min()) / (
                self.df[col].max() - self.df[col].min()
            )

    def score(self, budget, preferences):
        df = self.df[self.df["preco"] <= budget].copy()

        if df.empty:
            return None

        # pesos dinâmicos (IA baseada em preferências)
        weights = {
            "economia": preferences.get("economia", 1),
            "conforto": preferences.get("conforto", 1),
            "espaco": preferences.get("espaco", 1),
        }

        total_weight = sum(weights.values())

        df["score"] = (
            df["economia"] * weights["economia"] +
            df["conforto"] * weights["conforto"] +
            df["espaco"] * weights["espaco"]
        ) / total_weight

        return df.sort_values(by="score", ascending=False)

    def recommend(self, budget, preferences, top_n=3):
        self.normalize()
        ranked = self.score(budget, preferences)

        if ranked is None:
            return "Nenhum carro encontrado"

        return ranked.head(top_n)
