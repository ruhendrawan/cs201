import streamlit as st
import streamlit.components.v1 as components
from jinja2 import Template
import pandas as pd
import numpy as np
import pickle  # to load a saved model
import base64  # to open .gif files in streamlit app

from features.home.controller import home_view


def main():
    app_title = "My App"
    app_mode = st.sidebar.selectbox(
        "Select Page", ["Home", "Table", "Map", "Html", "Prediction"]
    )  # two pages

    if app_mode == "Home":
        st.title("Recent Loan Prediction")
        st.markdown("Applicant Income VS Loan Amount ")
    elif app_mode == "Table":
        df = pd.DataFrame(
            np.random.randn(10, 5), columns=("col %d" % i for i in range(5))
        )
        st.table(df)
    elif app_mode == "Map":
        df = pd.DataFrame(
            np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
            columns=["lat", "lon"],
        )
        st.map(df)
    elif app_mode == "Html":
        items = ["Item 1", "Item 2", "Item 3"]

        with open("template/items.html", "r") as template_file:
            template_content = template_file.read()
            jinja_template = Template(template_content)
        rendered_html = jinja_template.render(title=app_title, items=items)
        components.html(rendered_html, height=200, scrolling=True)
    elif app_mode == "Prediction":
        st.image("slider-short-3.jpg")
        st.subheader(
            "Sir/Mme , YOU need to fill all necessary informations in order    to get a reply to your loan request !"
        )
        st.sidebar.header("Informations about the client :")

        gender_dict = {"Male": 1, "Female": 2}
        feature_dict = {"No": 1, "Yes": 2}
        edu = {"Graduate": 1, "Not Graduate": 2}
        prop = {"Rural": 1, "Urban": 2, "Semiurban": 3}
        ApplicantIncome = st.sidebar.slider(
            "ApplicantIncome",
            0,
            10000,
            0,
        )
        CoapplicantIncome = st.sidebar.slider(
            "CoapplicantIncome",
            0,
            10000,
            0,
        )
        LoanAmount = st.sidebar.slider("LoanAmount in K$", 9.0, 700.0, 200.0)
        Loan_Amount_Term = st.sidebar.selectbox(
            "Loan_Amount_Term",
            (12.0, 36.0, 60.0, 84.0, 120.0, 180.0, 240.0, 300.0, 360.0),
        )
        Credit_History = st.sidebar.radio("Credit_History", (0.0, 1.0))
        Gender = st.sidebar.radio("Gender", tuple(gender_dict.keys()))
        Married = st.sidebar.radio("Married", tuple(feature_dict.keys()))
        Self_Employed = st.sidebar.radio("Self Employed", tuple(feature_dict.keys()))
        Dependents = st.sidebar.radio("Dependents", options=["0", "1", "2", "3+"])
        Education = st.sidebar.radio("Education", tuple(edu.keys()))
        Property_Area = st.sidebar.radio("Property_Area", tuple(prop.keys()))

        class_0, class_3, class_1, class_2 = 0, 0, 0, 0

        if Dependents == "0":
            class_0 = 1
        elif Dependents == "1":
            class_1 = 1
        elif Dependents == "2":
            class_2 = 1
        else:
            class_3 = 1

        Rural, Urban, Semiurban = 0, 0, 0
        if Property_Area == "Urban":
            Urban = 1
        elif Property_Area == "Semiurban":
            Semiurban = 1
        else:
            Rural = 1

        data1 = {
            "Gender": Gender,
            "Married": Married,
            "Dependents": [class_0, class_1, class_2, class_3],
            "Education": Education,
            "ApplicantIncome": ApplicantIncome,
            "CoapplicantIncome": CoapplicantIncome,
            "Self Employed": Self_Employed,
            "LoanAmount": LoanAmount,
            "Loan_Amount_Term": Loan_Amount_Term,
            "Credit_History": Credit_History,
            "Property_Area": [Rural, Urban, Semiurban],
        }
        feature_list = [
            ApplicantIncome,
            CoapplicantIncome,
            LoanAmount,
            Loan_Amount_Term,
            Credit_History,
            get_value(Gender, gender_dict),
            get_fvalue(Married),
            data1["Dependents"][0],
            data1["Dependents"][1],
            data1["Dependents"][2],
            data1["Dependents"][3],
            get_value(Education, edu),
            get_fvalue(Self_Employed),
            data1["Property_Area"][0],
            data1["Property_Area"][1],
            data1["Property_Area"][2],
        ]
        single_sample = np.array(feature_list).reshape(1, -1)

        if st.button("Predict"):
            file_ = open("6m-rain.gif", "rb")
            contents = file_.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            file_.close()
            file = open("green-cola-no.gif", "rb")
            contents = file.read()
            data_url_no = base64.b64encode(contents).decode("utf-8")
            file.close()
            loaded_model = pickle.load(open("Random_Forest.sav", "rb"))
            prediction = loaded_model.predict(single_sample)
            if prediction[0] == 0:
                st.error(
                    "According to our Calculations, you will not get the loan from Bank"
                )
                st.markdown(
                    f'<img src="data:image/gif;base64,{data_url_no}" alt="cat gif">',
                    unsafe_allow_html=True,
                )
            elif prediction[0] == 1:
                st.success("Congratulations!! you will get the loan from Bank")
                st.markdown(
                    f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
                    unsafe_allow_html=True,
                )


if __name__ == "__main__":
    main()
