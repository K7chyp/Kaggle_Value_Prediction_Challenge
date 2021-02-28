import numpy as np

class Preprocessing:
    def __init__(self, train_df, test_df):
        self.train_ = train_df.copy()
        self.test_ = test_df.copy()

    def remove_constant_columns(self):

        col_rm = []
        for col in self.train_.columns:
            if col != "ID" and col != "target":
                if self.train_[col].std() == 0:
                    col_rm.append(col)

        self.train_.drop(col_rm, axis=1, inplace=True)
        self.test_.drop(col_rm, axis=1, inplace=True)

    def drop_sparse(self):
        flist = [x for x in self.train_.columns if not x in ["ID", "target"]]
        for f in flist:
            if len(np.unique(self.train_[f])) < 2:
                self.train_.drop(f, axis=1, inplace=True)
                self.test_.drop(f, axis=1, inplace=True)

    def prerproce_it(self): 
      self.remove_constant_columns()
      self.drop_sparse()
      return self.train_, self.test_
