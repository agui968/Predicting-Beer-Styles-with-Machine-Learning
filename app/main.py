import streamlit as st
import pickle
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import euclidean_distances
from PIL import Image
import streamlit.components.v1 as c
df=pd.read_csv('resources\\clean_limited.csv',index_col=0)
with open('../models/final_model_gbc.pkl', 'rb') as input:
    gb_model = pickle.load(input) 

with open('../models/trained_model_lr1.pkl', 'rb') as input:
    lr_model = pickle.load(input)

with open('../models/trained_model_adaboost_dtc.pkl', 'rb') as input:
    abdt_model = pickle.load(input)

df=pd.read_csv('resources\\clean_limited.csv',index_col=0)
def classify(pred):
        """Function to classify beer styles according to their qualities"""
        if pred==0:
            return 'Wheat'
        elif pred==1:
            return "Pale Lager/Blonde Ale"
        elif pred==2:
            return "Pale Ale"
        elif pred==3:
            return "Strong Ale"
        elif pred==4:
            return "Brown Ale"
        elif pred==5:
            return "Stout/Porter"


st.set_page_config(page_title='Predicting Beer Styles with Machine Learning 💻🍺',page_icon=':beer types:')

select=st.sidebar.selectbox('Select menu',['Home','Try the model yourself','Discover a new beer'])
if select=='Home':
    st.title('Predicting Beer Styles with Machine Learning')
    img=Image.open('resources\\aibeer.jpg')
    st.image(img)
    st.header('Introduction')
    st.markdown('Tired of making *pour* beer choices? Now you will be able to know the style of a beer based on its main qualities: ABV (alcohol by volume), IBU (international bitterness units) and SRM color (standard reference method). \n\n - If you want to discover your new favorite \'hop juice\', head on to the "**Discover a new beer**" section.\n\n - If you prefer to make your own machine learning predictions, open the "**Try the model yourself**" section, where you will also find a quick guide to choose your parameters.')
    
elif select=='Try the model yourself':
    st.title('Make your own predictions 🍺')
    # df=pd.read_csv('resources\\clean_limited.csv',index_col=0)
    img3=Image.open('resources\\bender.webp')
    st.image(img3)
    st.write('In this section you will introduce the parameters of your beer and let machine learning do the magic and predict its style.\nTo make it easier for you, below you can find some guidance on the usual values of each variable:')
    st.markdown("- ***Alcohol by volume***:\n\n\tUsually, pale ale and stout styles have higher alcohol content, but there's no general rule for this parameter. Go nuts!")
    st.markdown("- ***International bitterness units***:\n\n\tMild - up to 20 IBU;\n\n\tSlightly bitter - 20 to 30 IBU;\n\n\tQuite bitter - 30 to 60 IBU;\n\n\tAs bitter as a rainy Monday - higher than 60 IBU.")
    st.markdown("- ***Color (SRM) scale***: \n\n\tBlonde - 1 to 15 SRM;\n\n\tAmber - 12 to 22 SRM;\n\n\tBrown - 23 to 35 SRM;\n\n\tAfter that... sky is the limit (actually, 50 SRM is the limit).\n\n\tFind the color of your favorite beer in the image below:")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(' ')
    with col2:
        # srm=)
        st.write('Color SRM scale:')
        st.image(Image.open('resources\\SRM_colorscale.webp'),width=450)
    with col3:
        st.write(' ')

#classify() used to go here
    def user_input():
        """Function to collect the parameters chosen by the user in order to make predictions with the ML model"""
        abv=st.sidebar.slider('Alcohol by volume',0,50,5)
        ibu=st.sidebar.slider('Bitterness',0,245,25)
        color=st.sidebar.slider('Color (SRM)',0,50,5)
        data={'ABV':abv,
              'IBU':ibu,
              'Color':color}
        features= pd.DataFrame(data,index=[0])
        return features
    df_user= user_input()

    model_options=['Gradient Boosting (Recommended)','Logistic Regression','Adaboost Decision Tree']
    model_selection=st.sidebar.selectbox('Choose a model for your predictions:',model_options)
    st.subheader('Introduce the parameters of the beer:')
    st.write(model_selection)
    if st.button('RUN'):
        if model_selection=='Gradient Boosting (Recommended)':
            st.success(classify(gb_model.predict(df_user)))
        elif model_selection=='Logistic Regression':
            st.success(classify(lr_model.predict(df_user)))
        elif model_selection=='Adaboost Decision Tree':
            st.success(classify(abdt_model.predict(df_user)))
    st.write(df_user)
    
    st.write('CHEERS TO DATA!🍻')

elif select=='Discover a new beer':
    img2=Image.open('resources\\white_perspective.jpg')
    st.image(img2)
    df=pd.read_csv('resources\\clean_limited.csv',index_col=0)
    st.header('Discover your new favorite \'hop juice\'!')
    st.markdown('This one is easy: tell us what you like and we\'ll take care of the rest. Ready to dive into a whole new realm of vibrant and lively craft beers?\n\n In case you don\'t know where to start, you will find a quick guide to choose your preferences on the "**Try the model yourself**" section.')
    with st.expander('Framework'):
        df=pd.read_csv('resources\\clean_limited.csv',index_col=0).head()
    def user_preferences():
        global abv_range,ibu_range,color_range# ,choice,preferences,distance,closest_beers
        abv_range,ibu_range,color_range= 55,20,6
        abv_filter=st.sidebar.radio('Select a level of alcohol',["Low (1º - 4º)","Medium (4º - 6.5º)","High (> 6º)","I want to forget my own name"])
        if abv_filter=="Low (1º - 4º)":
            abv_range=np.random.uniform(1.0,4.0)
        elif abv_filter=="Medium (4º - 6.5º)":
            abv_range=np.random.uniform(4.0,6.5)
        elif abv_filter=="High (> 6º)":
            abv_range=np.random.uniform(6.5,15.0)
        elif abv_filter=="I want to forget my own name":
            abv_range=np.random.uniform(15.0,53.0)
    
        ibu_filter=st.sidebar.radio('How bitter do you like your beer?',['Mild','Slightly bitter','Quite bitter','As bitter as a rainy Monday'])
        if ibu_filter=="Mild":    
            ibu_range=np.random.randint(0,21)
        elif ibu_filter=="Slightly bitter":
            ibu_range=np.random.randint(21,31)
        elif ibu_filter=="Quite bitter":
            ibu_range=np.random.randint(31,61)
        else:
            ibu_range=np.random.randint(61,246)

        color_filter=st.sidebar.radio('Choose the color of your beer',['Very Pale','Blonde','Amber','Brown','Dark'])
        if color_filter=="Very Pale": #wheat 
            color_range=np.random.randint(0,7)
        elif color_filter=="Blonde": #Pale Ale
            color_range=np.random.randint(7,15)
        elif color_filter=="Amber": #strong ale
            color_range=np.random.randint(12,23)
        elif color_filter=="Brown":
            color_range=np.random.randint(23,35)
        else:
            color_range=np.random.randint(35,51)
        choice=[abv_range,ibu_range,color_range]
        # preferences= pd.DataFrame(columns=['ABV','IBU','Color'],data=choice,index=[0])

        distance= np.linalg.norm(df[['ABV', 'IBU', 'Color']].values - choice, axis=1)
        #checks distance to other beer values in relation to the user choices
        closest_beers = distance.argsort(axis=0)[0] #sorts the distances to get the closest ones (5 closest values)
        
        # preferences, closest_beers,choice
    
        if st.button('Discover my new favorite \'hop juice\'!'):
            recommend_code = gb_model.predict([[abv_range, ibu_range, color_range]])
            print('If you like that kind of beer, you\'re into ', classify(recommend_code))
            print(f'So you should definitely try {df["Name"].iloc[closest_beers]}')
    user_preferences()


#     user_taste=[[abv_preference, ibu_preference, color_preference]]
#     # st.write(df_filtered2)
    # st.table(df_filtered3)


#ahora es local, habría q darle a "Deploy" en la página web