class Exploration:
    
    def __init__(self, train_df=train_df, test_df=test_df):

        self.train_ = train_df.copy()
        self.test_ = test_df.copy()

    def find_local_max(self, local_dct):

        count = 0

        value_ = tuple(local_dct.items())[0][0]
        count = tuple(local_dct.items())[0][1]

        return value_, count

    def find_max_values(self):

        lst_ = list(self.train_.columns.values)
        zero_count_dict = dict()

        for value in lst_:

            local_dct = dict(self.train_[str(value)].value_counts())
            zero_count_dict[value] = self.find_local_max(local_dct)

        return zero_count_dict
