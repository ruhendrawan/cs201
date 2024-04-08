import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
from jinja2 import Template

from features.home.controller import home_view


def main():
    app_title = "My App"

    # Automatic routing to pages using Multi-page app pattern
    #   /pages/1_Plotting_Demo.py
    #   /pages/2_Map_Demo.py

    # Single page app pattern
    app_mode = st.sidebar.selectbox("Select Page", ["Home", "Table", "Map", "Html"])

    if app_mode == "Home":
        # App routing to controller actions function
        home_view()
    elif app_mode == "Table":
        # Inline action
        # Not recommended for large codebase
        df = pd.DataFrame(
            np.random.randn(10, 5), columns=("col %d" % i for i in range(5))
        )
        st.table(df)
    elif app_mode == "Map":
        df = pd.DataFrame(
            np.random.randn(100, 2) / [100, -100] + [40.4301135, -79.9528444],
            columns=["lat", "lon"],
        )
        st.map(df)
    elif app_mode == "Html":
        # HTML rendering  using Jinja2
        items = ["Item 1", "Item 2", "Item 3"]

        with open("templates/items.html", "r") as template_file:
            template_content = template_file.read()
            jinja_template = Template(template_content)
        rendered_html = jinja_template.render(title=app_title, items=items)
        components.html(rendered_html, height=200, scrolling=True)


if __name__ == "__main__":
    main()
