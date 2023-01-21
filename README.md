# Integrating-GPT-3-in-Excel
Created an editable user-defined Excel function ask_gpt() capable of interacting directly with the OpenAI API for output.

Almost everyone is talking about ChatGPT and it's multitude of real-life use-cases. The possibilities of OpenAI's GPT is endless and this repository is all about bringing that power to excel. In the past few weeks, there has been a lot of buzz around the GPT Google Sheet Add-in but what if you want to work on sensitive data on a local file? 

I have the solution right here, a User-defined Function coded in Python capable of interacting with Excel's VBA backend as well the OpenAI API. This is accomplished using the open-source python module xlwings.

# Setup and Usage

1. get the xlwings add-in to Excel. Refer [link](https://docs.xlwings.org/en/latest/installation.html) for installation.
2. Open the .xlsm file and the corresponding same name .py file generated as a result of the above installation.
3. Start coding. Refer to ask_gpt.py file for the sample User-defined Function.

