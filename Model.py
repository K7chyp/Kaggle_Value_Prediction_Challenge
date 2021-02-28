from sklearn import preprocessing
from sklearn import utils
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score


class Model(): 

	def __init__(self, train, test): 
		self.train = train
		self.test = test

	def post_processinig(self): 

		lab_enc = preprocessing.LabelEncoder()
		y  = lab_enc.fit_transform(self.train.target)

		return y

	def split(self): 

		y = self.post_processinig()
		X_train, X_test, y_train, y_test = train_test_split(self.train, 
													y, random_state=42)
		return X_train, X_test, y_train, y_test 

	def classifier(self)

		X_train, X_test, y_train, y_test = self.split()

		log_clf = LogisticRegression(random_state=42)
		rnd_clf = RandomForestClassifier(random_state=42)
		svm_clf = SVC(random_state=42)

		voting_clf = VotingClassifier(
		    estimators=[('lr', log_clf), 
		                ('rf', rnd_clf),
		                ('svc', svm_clf)],
		                voting='hard')
		return voting_clf.fit(X_train, y_train)
