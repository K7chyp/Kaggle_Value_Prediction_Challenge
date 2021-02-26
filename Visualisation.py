import seaborn as sns 
import matplotlib.pyplot as plt

class Visualisation:

    def __init__(self, train_df, test_df):

        self.train_ = train_df.copy()
        self.test_ = test_df.copy()

    def plot_target(self):

        plt.figure(figsize=(8, 10))
        plt.scatter(range(self.train_.shape[0]), 
                    np.sort(self.train_["target"].values))
        plt.xlabel("index", fontsize=12)
        plt.ylabel("Target", fontsize=12)
        plt.title("Target Distribution", fontsize=14)

        return plt.show()

    def plot_target_hist(self):

        plt.figure(figsize=(12, 8))
        sns.distplot(self.train_["target"].values, bins=50)
        plt.xlabel("Target", fontsize=14)
        plt.title("Target Histogram", fontsize=14)

        return plt.show()
