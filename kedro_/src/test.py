import joblib
import pandas as pd
import tensorflow as tf
import numpy as np

def sklearn_model_test():
    loaded_pipeline = joblib.load('LR_model.pkl')
    while True:
        text = input('text:')
        if text == 'q':
            break
        print(loaded_pipeline.predict([text]))

def test():
    df = pd.read_csv('./data/01_raw/twitter.csv',encoding='ISO-8859-1')
    print(df[:3])


def tf_model_save_test():
    model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    data = np.random.rand(20,10)
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    y = np.random.rand(20)
    model.fit(data,y)
    model.save('tf_sentiment_model.h5')
    

tf_model_save_test()





