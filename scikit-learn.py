from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

x,y = load_breast_cancer(return_x_y = True)
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state = 42)

