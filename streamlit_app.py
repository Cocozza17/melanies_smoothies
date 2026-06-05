{\rtf1\ansi\ansicpg1252\cocoartf2821
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # Import python packages\
import streamlit as st\
import os\
from snowflake.snowpark.context import get_active_session\
from snowflake.snowpark.functions import col\
\
# Write directly to the app\
st.title(":cup_with_straw: Customize Your Smoothie! :cup_with_straw:")\
st.write(\
  """Choose the fruits you want in your custom Smoothie!\
  """\
)\
#option = st.selectbox(\
#    'What is your favorite fruit?',\
#     ('Banana','Strawberries','Peaches'))\
#\
#st.write('Your favorite fruit is: ',option)\
\
\
\
session = get_active_session()\
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))\
#st.dataframe(data=my_dataframe, use_container_width=True)\
ingredients_list = st.multiselect(\
'Choose up to 5 Ingredients: '\
,my_dataframe\
,max_selection = 5\
)\
if ingredients_list:\
    #st.write(ingredients_list)\
    #st.text(ingredients_list)\
    \
    ingredients_string = ''\
    for fruit_chosen in ingredients_list: \
        ingredients_string += fruit_chosen + ' '\
\
    #st.write(ingredients_string)\
\
\
\
    #\
\
    name_on_order = st.text_input('Name on Smoothie: ', value="Name")\
\
    time_to_insert= st.button('Submit Order')\
\
    my_insert_stmt = """ insert into smoothies.public.orders(ingredients, name_on_order)\
                    values ('""" + ingredients_string + """','"""+name_on_order+"""')"""\
\
    #st.write(my_insert_stmt)\
    if time_to_insert:\
        if ingredients_string:\
            if name_on_order:\
                session.sql(my_insert_stmt).collect()\
                st.success(f'Your Smoothie is ordered, \{name_on_order\}!', icon="\uc0\u9989 ")\
}