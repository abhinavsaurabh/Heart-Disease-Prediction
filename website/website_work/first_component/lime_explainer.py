import lime
import lime.lime_tabular
import os
from first_component import data_provider
import pickle
import joblib

dir = os.path.dirname(__file__)


METHODS = {
    'files': {
        'trainFile': 'ml_models/X_train.pkl',
        'trainLabels': 'ml_models/y_train.pkl',
        'featureNames' : 'ml_models/feature_names.pkl',
     },
    
   'mlp': {
        'class': "MLPExplainer",
        'name': "MLP",
        'lowercase': False,
    },
    'svm': {
        'class': "SVMExplainer",
        'name': "SVM",
        'lowercase': False,
    },
    'dt': {
        'class': "DTExplainer",
        'name': "Decision Tree",
        'lowercase': False,
    },
    'knn': {
        'class': "KNNExplainer",
        'name': "KNN",
        'lowercase': True,
    },
    'rf': {
        'class': "RFExplainer",
        'name': "RF",
        'lowercase': True,
    },

    'bayes': {
        'class': "BayesExplainer",
        'name': "Bayes",
        'lowercase': True,
    },

    'lr': {
        'class': "LRExplainer",
        'name': "LR",
        'lowercase': True,
    },

    'xgb': {
        'class': "XGBExplainer",
        'name': "XGB",
        'lowercase': True,
    },

    'voting': {
        'class': "VotingExplainer",
        'name': "Voting",
        'lowercase': True,
    },
}


def GetJobLibFile(filepath):
    if os.path.isfile(os.path.join(dir, filepath)):
        return joblib.load(os.path.join(dir, filepath))
    else:
        print("file does not exit")

def GetPickleFile(filepath):
    if os.path.isfile(os.path.join(dir, filepath)):
        return pickle.load( open(os.path.join(dir, filepath), "rb" ) )
    return None


def getX_train():
    return GetJobLibFile(METHODS['files']['trainFile'])


def gety_train():
    return GetJobLibFile(METHODS['files']['trainLabels'])


def getFeaturesNames():
    return GetJobLibFile(METHODS['files']['featureNames'])


X_train = getX_train()
y_train = gety_train()
featuresNames = getFeaturesNames()

SVCClassifier,DecisionTreeClassifier,KNN,RF,MLP,Bayes,LR,XGB,Voting = data_provider.GetAllClassifiers()



class MLPExplainer:
    """Class to explain classification results of a scikit-learn MLP
       Classifier.
    """
    
  
    def explain(self, testSample):
        explainer = lime.lime_tabular.LimeTabularExplainer(X_train, mode='classification',feature_names=featuresNames,training_labels=y_train, verbose='True')
        exp_lime = explainer.explain_instance(testSample, MLP.predict_proba, num_features=5)
        return exp_lime



class SVMExplainer:
    """Class to explain classification results of a scikit-learn SVM
       Classifier.
    """

    def explain(self, testSample):
        explainer = lime.lime_tabular.LimeTabularExplainer(X_train, mode='classification',feature_names=featuresNames,training_labels=y_train, verbose='True')
        exp_lime = explainer.explain_instance(testSample, SVCClassifier.predict_proba, num_features=5)
  
        return exp_lime


class DecisionTreeExplainer:
    """Class to explain classification results of a scikit-learn DT
       Classifier.
    """

    
    def explain(self, testSample):
        explainer = lime.lime_tabular.LimeTabularExplainer(X_train, mode='classification',feature_names=featuresNames,training_labels=y_train, verbose='True')
        exp_lime = explainer.explain_instance(testSample, DecisionTreeClassifier.predict_proba, num_features=5)
  
        return exp_lime


class KNNExplainer:
    """Class to explain classification results of a scikit-learn KNN
       Classifier.
    """


  
    def explain(self, testSample):
        explainer = lime.lime_tabular.LimeTabularExplainer(X_train, mode='classification',feature_names=featuresNames,training_labels=y_train, verbose='True')
        exp_lime = explainer.explain_instance(testSample, KNN.predict_proba, num_features=5)
  
        return exp_lime


class RFExplainer:
    """Class to explain classification results of a scikit-learn RF
       Classifier.
    """

  
    def explain(self, testSample):
        explainer = lime.lime_tabular.LimeTabularExplainer(X_train, mode='classification',feature_names=featuresNames,training_labels=y_train, verbose='True')
        exp_lime = explainer.explain_instance(testSample, RF.predict_proba, num_features=5)
  
        return exp_lime


class BayesExplainer:
    """Class to explain classification results of a scikit-learn Bayes
       Classifier.
    """

  
    def explain(self, testSample):
        explainer = lime.lime_tabular.LimeTabularExplainer(X_train, mode='classification',feature_names=featuresNames,training_labels=y_train, verbose='True')
        exp_lime = explainer.explain_instance(testSample, Bayes.predict_proba, num_features=5)
  
        return exp_lime

class LRExplainer:
    """Class to explain classification results of a scikit-learn logistic regression
       Classifier.
    """

  
    def explain(self, testSample):
        explainer = lime.lime_tabular.LimeTabularExplainer(X_train, mode='classification',feature_names=featuresNames,training_labels=y_train, verbose='True')
        exp_lime = explainer.explain_instance(testSample, LR.predict_proba, num_features=5)
  
        return exp_lime

class XGBExplainer:
    """Class to explain classification results of a  XGB
       Classifier.
    """

  
    def explain(self, testSample):
        explainer = lime.lime_tabular.LimeTabularExplainer(X_train, mode='classification',feature_names=featuresNames,training_labels=y_train, verbose='True')
        exp_lime = explainer.explain_instance(testSample, XGB.predict_proba, num_features=5)
  
        return exp_lime


