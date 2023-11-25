import streamlit as st
import pandas as pd
from PIL import Image
import streamlit.components.v1 as c

st.set_page_config(page_title='Predicting Beer Styles with Machine Learning',page_icon=':beer types:')

select=st.sidebar.selectbox('Select menu',['Home','Discover a new beer','Try the model yourself'])
df=pd.read_csv('data\\clean_limited.csv',index_col=0)
if select=='Home':
    st.title('Predicting Beer Styles with Machine Learning')
    img=Image.open('data\\white_perspective.jpg')
    st.image(img)
    with st.expander('Introduction'):
        st.write('Tired of making \'pour\' beer choices? Now you will be able to know the style of a beer based on its main qualities: ABV (alcohol by volume), IBU (international bitterness units) and SRM color (standard reference method). \n\n If you want to discover your new favorite \'hop juice\', head on to the "Discover a new beer" section.')

elif select=='Discover a new beer':
    # df=pd.read_csv('data\\clean_limited.csv',index_col=0)
    with st.expander('Framework'):
        df=pd.read_csv('data\\clean_limited.csv',index_col=0)
    # st.write('df_filtered')

    filter=st.sidebar.radio('Select a level of alcohol',["Low (1º - 4º)","Medium (4º - 6.5º)","High (> 6º)"])
    if select=="Low (1º - 4º)":
        filter= df[df['ABV']<=4]
    elif select=="Medium (4º - 6.5º)":
        filter= df[(df['ABV']>4) & (df['ABV']<=6.5)]
    else:
        filter= df[df['ABV']>=6.5]
    df_filtered=filter
    # st.write(df_filtered)

    # file=open('data\\heatmap.html','r')
    # c.html(file.read(),height=400)
    filter3=st.sidebar.selectbox('How bitter do you like your beer?',['Mild','Slightly bitter','Quite bitter','As bitter as a rainy Monday'])
    if select=="Mild":    
        filter3= df_filtered[df['IBU']<20]
    elif select=="Slightly bitter":
        filter3= df_filtered[(df['IBU']<=30) & (df['IBU']>20)]
    elif select=="Quite bitter":
        filter3= df_filtered[(df['IBU']>30) & (df['IBU']<60)]
    else:
        filter3= df_filtered[df['IBU']>60]
    df_filtered3=filter3
    # st.write(df_filtered2)
    # df_filtered.rename(columns={'latidtud':'lat','longitud':'lon'},inplace=True) #es mejor transformar el df en ipynb
    # st.write(df)

    filter2=st.sidebar.selectbox('Choose the color of your beer',['Very Pale','Blonde','Amber','Brown','Dark'])
    if select=="Very Pale": #wheat 
        filter2= df_filtered[df['Color']<6]
    elif select=="Blonde": #Pale Ale
        filter2= df_filtered[(df['Color']>5) & (df['Color']<=15)]
    elif select=="Amber": #strong ale
        filter2= df_filtered[(df['Color']<=22) & (df['Color']>12)]
    elif select=="Brown":
        filter2= df_filtered[(df['Color']>12) & (df['ABV']<=6.5)]
    else:
        filter2= df_filtered[df['Color']>=17]
    df_filtered2=filter2
    # st.write(df_filtered2)
    # st.table(df_filtered3)

    
    # st.sidebar.button('Click here')

elif select=='Try the model yourself':
    df=pd.read_csv('data\\clean_limited.csv',index_col=0)
    st.write('CHEERS TO DATA!🍻')


#ahora es local, habría q darle a "Deploy" en la página web