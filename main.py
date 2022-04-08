import streamlit as st
import pandas as pd
st.title('Streamlit is very well to integrate data webapps for ML and DS')
st.write("Hi, This is the sample line chart:")
# st.write(pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
# }))
df=pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
# st.table(df)
st.line_chart(df)
hour_to_filter = st.slider('hour', 0, 23, 17)