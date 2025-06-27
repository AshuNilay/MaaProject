

# * Firmwide Data Analyst # " Author - Nilay_Adhwaryu from tan langchain_ core:messages import BaseMessage ana from langchain.prompts import PromptTemplate from langchain core,output parsers import JsonoutputParser from langgraph.types import Checkpointer from Jnggraph.graph import START, END, StateGraph from Janggraph.greph.state import CompiledStateGraph
from typing import TypedDict, Annotated, Sequence, Union import operator
import pandas as pd import json from IPython.display import Markdown
from templates import BaseAgent from Agents import DataWranglingAgent, DataVisualizationAgent from utils.plotly import plotly_from_dict from utils.regex import remove_consecutive_duplicates, get_gener:
AGENT_NAME wsr_data_analyst"
I
class FWSRDataAnalyst(BaseAgent):
FWSR DataAnalyst is a multi-agent class that combines data wri
'arameters:
model:
The language model to be used for the agents. data_wrangling_agent: DataWranglingAgent The Data Wrangling Agent for transforming raw data. data_visualization_agent: DataVisualizationAgent The Data Visualization Agent for generating plots. checkpointer: Checkpointer optional) The checkpointer to save the state of the multi-agent systel
Methods:
ainvoke_agent(user_instructions, data_raw, ""kwargs) Asynchronously invokes the multi-agent with user instructionfrom tan langchain_ core:messages import BaseMessage ana from langchain.prompts import PromptTemplate from langchain core,output parsers import JsonoutputParser from langgraph.types import Checkpointer from Jnggraph.graph import START, END, StateGraph from Janggraph.greph.state import CompiledStateGraph
from typing import TypedDict, Annotated, Sequence, Union import operator
import pandas as pd import json from IPython.display import Markdown
from templates import BaseAgent from Agents import DataWranglingAgent, DataVisualizationAgent from utils.plotly import plotly_from_dict from utils.regex import remove_consecutive_duplicates, get_gener:
AGENT_NAME wsr_data_analyst"
I
class FWSRDataAnalyst(BaseAgent):
FWSR DataAnalyst is a multi-agent class that combines data wri
'arameters:
model:
The language model to be used for the agents. data_wrangling_agent: DataWranglingAgent The Data Wrangling Agent for transforming raw data. data_visualization_agent: DataVisualizationAgent The Data Visualization Agent for generating plots. checkpointer: Checkpointer optional) The checkpointer to save the state of the multi-agent systel
Methods:
ainvoke_agent(user_instructions, data_raw, ""kwargs) Asynchronously invokes the multi-agent with user instruction