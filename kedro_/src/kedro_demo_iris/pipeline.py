"""
This is a boilerplate pipeline
generated using Kedro 0.18.8
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import text_split_aws_data,text_split_twitter_data,new_and_train_model,emotion_predict


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            # node(
            #     func=text_split_aws_data,
            #     inputs=["example_emotion_text_data", "parameters"],
            #     outputs=["text_X_train", "text_X_test", "text_y_train", "text_y_test"],
            #     name="text_split",
            # ),
            node(
                func=text_split_twitter_data,
                inputs=["twitter_text_data", "parameters"],
                outputs=["text_X_train", "text_X_test", "text_y_train", "text_y_test"],
                name="text_split",
            ),
            node(
                func=new_and_train_model,
                inputs=["text_X_train", "text_y_train"],
                outputs="trained_model",
                name="train",
            ),
            node(
                func=emotion_predict,
                inputs=["trained_model","text_X_test","text_y_test"],
                outputs="mse",
                name="make_pred",
            )
        ]
    )
