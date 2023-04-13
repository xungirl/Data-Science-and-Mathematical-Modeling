import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import shap
import xgboost as xgb
from sklearn.ensemble import GradientBoostingRegressor
from xgboost import plot_importance
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,r2_score
df=pd.read_csv('D:\data(pac2).csv')
features=['Year','Beam','Draft','Sail Area','Comprehensive regional factors','Length']
def mape(actual, pred): 
    actual, pred = np.array(actual), np.array(pred)
    return np.mean(np.abs((actual - pred) / actual))
Y=df['Listing Price']
X=df[features]
tr_x,te_x,tr_y,te_y=train_test_split(X,Y,test_size=0.2,random_state=42)
print("\nXGBOOST:")
xgb_model=xgb.XGBRegressor()
xgb_model.fit(tr_x,tr_y)
y1_pred = xgb_model.predict(tr_x)
y2_pred = xgb_model.predict(te_x)
print("Average absolute percentage error of training set:{:.3f}".format(mape(xgb_model.predict(tr_x),tr_y)))
print("Average absolute percentage error of test set:{:.3f}".format(mape(xgb_model.predict(te_x),te_y)))
print("r2_score",r2_score(tr_y,y1_pred))
print("r2_score",r2_score(te_y,y2_pred))
# plot feature importance
pyplot.show()
explainer = shap.TreeExplainer(xgb_model)
shap_values = explainer.shap_values(X) 
plt.rcParams["axes.unicode_minus"]=False 
shap.summary_plot(shap_values, X)
shap.summary_plot(shap_values, X, plot_type="bar")
shap_interaction_values = explainer.shap_interaction_values(X)
shap.summary_plot(shap_interaction_values, X)
