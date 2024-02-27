import streamlit as st
import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

#------------ Defining Templates -------------------------------------------


question_types = {'Calculate':'work out from given facts, figures or information',
'Compare':'identify/comment on similarities and/or differences',
'Consider':'review and respond to given information',
'Contrast':'identify/comment on differences',
'Deduce':'conclude from available information',
'Define':'give precise meaning',
'Demonstrate':'show how or give an example',
'Describe':'state the points of a topic / give characteristics and main features',
'Determine':'establish an answer using the information available',
'Discuss':'write about issue(s) or topic(s) in depth in a structured way',
'Evaluate':'judge or calculate the quality, importance, amount, or value of something',
'Examine':'investigate closely, in detail',
'Explain':'set out purposes or reasons / make the relationships between things evident / provide why and/or how and support with relevant evidence',
'Give':'produce an answer from a given source or recall/memory',
'Identify':'name / select / recognise',
'Justify':'support a case with evidence/argument',
'Predict':'suggest what may happen based on available information',
'Show (that)':'provide structured evidence that leads to a given result',
'Sketch':'make a simple freehand drawing showing the key features, taking care over proportions',
'State':'express in clear terms',
'Suggest':'apply knowledge and understanding to situations where there are a range of valid responses in order to make proposals / put forward considerations',
}

prompt_infos = []

for key,description in zip(question_types.keys(), question_types.values()):
    temp = {}
    temp['name'] = key
    temp['explanation'] = description
    prompt_infos.append(temp)

st.markdown("# O levels chemistry teacher")
st.markdown("## Ask your chemistry questions. Mention question in o levels format.")

llm = ChatOpenAI(temperature=0.9, model='gpt-3.5-turbo')

text_prompt = st.text_input("Ask your questions here: ")

if text_prompt:
  prompt = ChatPromptTemplate.from_messages([
    ("system", "I am a chemistry o levels teacher. I know alot about all kinds of chemistry questions including organic chemistry, inorganic chemistry etc. Ask me any questions regarding chemistry.\
     For a specific question, I find more information about keywords present in the user's question in the this lookup data {lookup_text}."),
    ("user", "Yes I am struggling with this question regarding chemistry: {input}")
])
  chain = prompt | llm 
  response = chain.invoke({"input": text_prompt, "lookup_text" : str(prompt_infos)})
  st.write(response.content)