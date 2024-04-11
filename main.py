import streamlit as st
import pickle,json, base64
from datetime import datetime, timedelta


st.sidebar.title("Flight ✈️ Price Prediction!!!")


#Airline___________________________________________________________________________________________________
Airline=st.sidebar.selectbox("Airline",(None,"SpiceJet","Vistara","Indigo","AirAsia","GO_FIRST","Air_India"))
Airline_dict={'AirAsia':0,'Indigo':1,'GO_FIRST':2,'SpiceJet':3,'Air_India':4 ,'Vistara':5}
#Source_City___________________________________________________________________________________________________
Source=st.sidebar.selectbox("Source",(None,"Bangalore","Chennai","Delhi","Kolkata","Mumbai","Hyderabad"))
Source_dict={'Delhi':0,'Hyderabad':1,'Bangalore':2,'Mumbai':3,'Kolkata':4,'Chennai':5}
#Depature_Time___________________________________________________________________________________________________
Depature_Time=st.sidebar.selectbox("Depature Time",(None,"Early_Morning","Morning", 'Afternoon',"Evening","Night","Late_Night"))
Depature_Time_dict={'Early_Morning':0,'Morning':1,'Afternoon':2,'Evening':3,'Night':4,'Late_Night':5}
#Stop___________________________________________________________________________________________________
Stop=st.sidebar.selectbox("Stop",(None,"zero","one","two","two_or_more"))
Stop_dict={'zero':0,'one':1,'two':2,'two_or_more':3} 
#Arrival_Time___________________________________________________________________________________________________
Arrival_Time=st.sidebar.selectbox("Arrival Time",(None,"Early_Morning","Morning", 'Afternoon',"Evening","Night","Late_Night"))
Arrival_Time_dict={'Early_Morning':0,'Morning':1,'Afternoon':2,'Evening':3,'Night':4,'Late_Night':5}
#Destination___________________________________________________________________________________________________
Destination=st.sidebar.selectbox("Destination",(None,"Bangalore","Chennai","Delhi","Kolkata","Mumbai","Hyderabad"))
Destination_dict={'Delhi':0,'Hyderabad':1,'Bangalore':2,'Mumbai':3,'Chennai':4,'Kolkata':5}
#Class___________________________________________________________________________________________________
Class=st.sidebar.selectbox("Class",(None,"Economy","Business"))  
Class_dict={'Economy':0,'Business':1}
#Days_After____________________________________________________________________________________________________
Date=st.sidebar.date_input("Departure Date",min_value=datetime.today(),max_value=datetime.today()+timedelta(days=50))
daY_diff=datetime.strptime(str(Date),"%Y-%m-%d")-datetime.today()
daY_diff=int(daY_diff.days+1)
#Load the saved model___________________________________________________________________________________________________
button=st.sidebar.button("Get Flight Price")
def load_lottiefile(filepath:str):
        with open(filepath,"r") as f:
            return json.load(f)

f=[Airline,Source,Depature_Time,Stop,Arrival_Time,Destination,Class,daY_diff]
if None not in f and button:
    Features=[Airline_dict[Airline],Source_dict[Source],Depature_Time_dict[Depature_Time],Stop_dict[Stop],Arrival_Time_dict[Arrival_Time],Destination_dict[Destination],Class_dict[Class],daY_diff]
    Model=pickle.load(open('LinearModel.pkl','rb'))
    prediction=Model.predict([Features])[0]
    
    st.markdown(f"<h2 style='text-align: center; color: #6A3BFF;'>Happy Traveling!</h1>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='text-align: center; color: #6A3BFF;'>Your Approximate ✈️ Flight Price is Rs.{round(prediction)}/-</h1>", unsafe_allow_html=True)
    st.image("plane.gif",width=200,caption="Happy Traveling!",use_column_width=True)

else:
    st.markdown(f"<h2 style='text-align: center; color: white;'>Enter all the values to get your ✈️ flight price</h1>", unsafe_allow_html=True)
    def get_img_as_base64(file):
        with open(file,"rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    img = get_img_as_base64("flight.jpg")
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image :url("data:image/png;base64,{img}");
    background-size : cover;
    }}
    [data-testid="stHeader"]{{
    background:rgba(0,0,0,0);
    }}
    </style>

    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

    