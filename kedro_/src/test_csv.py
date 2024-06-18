import pandas as pd
import joblib

df = pd.read_csv("C:/Users/caigang/vscode whoks/kedro-test/kedro-demo-iris/data/01_raw/1429_1.csv",dtype={"reviews.text": str})
df.dropna(subset=['reviews.text'], inplace=True)
df.dropna(subset=['reviews.rating'], inplace=True)

def test_accuracy(sk_model:str,df:pd.DataFrame):

    loaded_pipeline = joblib.load(sk_model)
    y_pred = loaded_pipeline.predict(df['reviews.text'])
    y_test = df['reviews.rating']
    accuracy = (y_pred == y_test).sum() / len(y_test)
    print(f'{sk_model} accuracy:', accuracy)


test_accuracy('LR_model.pkl',df)
# test_accuracy('NB_model.pkl',df)
# test_accuracy('svm_model.pkl',df)


