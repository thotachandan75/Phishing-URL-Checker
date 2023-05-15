import streamlit as st
import main_app
import pandas as pa
import plotly.express as px


def main():
    page_markdown = open("general_style.css", "r").read()
    st.markdown(f"<style>{page_markdown}</style>", unsafe_allow_html=True)
    
    st.title("URL Model analysis")

    st.write(f"We have used the dataset from the website which contains about 84 features which can be used to "
             f"determine whether the website is used for phishing or not The dataset consists of 11430 urls which are "
             f"categorized as legitimate or phishing links.")
    kaggle_link = '<a href="https://www.kaggle.com/datasets/shashwatwork/web-page-phishing-detection-dataset"' \
                  ' target="_blank" class="kaggle_link" >Kaggle Link</a>'
    st.markdown(kaggle_link, unsafe_allow_html=True)

    st.write("")
   
    columns = st.columns(2)
    with columns[0]:
         st.subheader("Before Preprocessing Dataset")
        before_preprocess = pa.read_csv("url_model_analysis/WebsiteDatasets/phishing_before_preprocess.csv")
        st.dataframe(data=before_preprocess)
    with columns[1]:
        st.subheader("After Preprocessing Dataset")
        after_preprocess = pa.read_csv("url_model_analysis/WebsiteDatasets/phishing_after_preprocess.csv")
        st.dataframe(data=after_preprocess.set_index("id"))
        


    st.write("")
    st.write("Preprocessing the dataset would insure better results and less training time for building the models. "
             "We have performed many preprocessing steps such as balancing the dataset using SMOTE Analysis, "
             "Dimensionality reduction using PCA, Data Transformation and Normalization, Feature Selection, "
             "etc.. Now the preprocessed dataset consists of 28 High correlated features which can be used for model "
             "building")
    st.write("")

        st.image(f"data:image/png;"
                 f"base64,{main_app.image_to_bytes('url_model_analysis/WebsiteImages/after_preprocess.png')}",
                 caption=None,
                 channels="RGB")

    st.write("We have used a Machine Learning, Ensemble Learning and Deep Learning and build and trained a total of "
             "20 models. this models are evaluated and results are presented below")

    columns = st.columns(2)

    with columns[0]:
        st.subheader("Machine Learning Models")

        ml = pa.read_csv("url_model_analysis/WebsiteDatasets/Machine Learning model results.csv")
        st.table(data=ml.set_index('Model'))

        ml_colors = ['#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

        ml_long = pa.melt(ml, id_vars=['Model'], var_name='Metric', value_name='Value')
        fig = px.bar(ml_long, x='Metric', y='Value', color='Model', barmode='group',
                     category_orders={'Metric': ['Accuracy', 'Precision', 'Recall', 'F1 Score']},
                     labels={'Metric': 'Metrics', 'Value': 'Value', 'Model': 'Models'},
                     color_discrete_sequence=ml_colors)
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

    with columns[1]:
        st.subheader("Deep Learning Models")

        dl = pa.read_csv("url_model_analysis/WebsiteDatasets/Deep Learning model results.csv")
        st.table(data=dl.set_index('Model'))

        dl_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

        dl_long = pa.melt(dl, id_vars=['Model'], var_name='Metric', value_name='Value')
        fig = px.bar(dl_long, x='Metric', y='Value', color='Model', barmode='group',
                     category_orders={'Metric': ['Accuracy', 'Precision', 'Recall', 'F1 Score']},
                     labels={'Metric': 'Metrics', 'Value': 'Value', 'Model': 'Models'},
                     color_discrete_sequence=dl_colors)
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("Ensemble Learning Models")
    columns = st.columns(2)

    with columns[0]:
        el = pa.read_csv("url_model_analysis/WebsiteDatasets/Ensemble Learning model results.csv")
        st.table(data=el.set_index('Model'))

    with columns[1]:
        el_colors = ['#393b79', '#6b6ecf', '#9c9ede', '#637939', '#8ca252', '#b5cf6b', '#cedb9c', '#8c6d31', '#bd9e39',
                     '#e7ba52']

        el_long = pa.melt(el, id_vars=['Model'], var_name='Metric', value_name='Value')
        fig = px.bar(el_long, x='Metric', y='Value', color='Model', barmode='group',
                     category_orders={'Metric': ['Accuracy', 'Precision', 'Recall', 'F1 Score']},
                     labels={'Metric': 'Metrics', 'Value': 'Value', 'Model': 'Models'},
                     color_discrete_sequence=el_colors)
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

    st.write("We are going to take models which have highest Accuracy out of machine, ensemble and deep learning and "
             "make accurate predictions")
