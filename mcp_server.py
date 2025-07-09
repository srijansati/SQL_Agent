from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit  
from langchain_community.utilities.sql_database import SQLDatabase  
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()
os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')

db = SQLDatabase.from_uri("sqlite:///Report_Card.db")  
llm =  ChatGroq(model= 'llama3')
toolkit = SQLDatabaseToolkit(db=db, llm=llm)



