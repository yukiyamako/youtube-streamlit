import streamlit as st
# import numpy as np
# import pandas as pd
import time as time

from PIL import Image

st.title('Streamlit 超入門')

st.write('プレぐレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(50):
    latest_iteration.text(f'Iteration {i + 1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!!!!'


# st.write('DataFrame')

# left_column, right_column = st.beta_columns(2)
# button = left_column.button('右カラム二文字を表示')
# if button:
#     right_column.write('ここは右カラム')

# expander = st.beta_expander('問い合わせ')
# expander.write('問い合わせの回答')

# df = pd.DataFrame({
#     '1列目':[1,2,3,4],
#     '2列目':[10,20,30,40]
# })

# st.write(df)
# st.dataframe(df.style.highlight_max(axis=1), width=300, height=500)
# st.title(df)
# st.table(df)

# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """

# df = pd.DataFrame(
#     np.random.rand(20, 3),
#     columns=['a', 'b', 'c']
# )

# st.title(df)
# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df)

# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )

# st.title(df)
# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df)
# st.map(df)

# st.write('Interactive Widgets')

# text = st.text_input('あなたの趣味を教えてください、')
# 'あなたの趣味', text, 'です'

# st.write('Display Image')


# option = st.selectbox(
#     'あなたが好きな数字を教えてください、',
#     list(range(1,11))
# )

# 'あなたが好きな数字は、', option, 'です'

# condition = st.slider('あなたの今の調子は？',0,100,50)
# 'コンディション', condition

# if st.checkbox('Show Image'):
#     img = Image.open('スクリーンショット 2022-09-02 22.48.47.png')
#     st.image(img, caption='Kohei Imanishi', use_column_width=True)