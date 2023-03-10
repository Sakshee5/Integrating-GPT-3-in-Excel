# Integrating-GPT-3-in-Excel
Created an editable user-defined Excel function ask_GPT() capable of interacting directly with the OpenAI API for output.

https://user-images.githubusercontent.com/69002060/213871946-13cc1ed8-dbbc-4e07-8fad-a8c795aff87a.mp4

P.S. I do know how to screen record on a PC but that was just not possible here. Apologies for the bad video quality :)

Almost everyone is talking about ChatGPT and it's multitude of real-life use-cases. The possibilities of OpenAI's GPT are endless and this repository is all about bringing that power to excel. In the past few weeks, there has been a lot of buzz around the GPT Google Sheet Add-in but what if you want to work on sensitive data on a local file? 

I have the solution right here, a User-defined Function coded in Python capable of interacting with Excel's VBA backend as well the OpenAI API. This is accomplished using the open-source python module xlwings.

# Setup and Usage

1. get the xlwings add-in to Excel. Refer [link](https://docs.xlwings.org/en/latest/installation.html) for installation.
2. Open the .xlsm file and the corresponding same name .py file generated as a result of the above installation.
3. Start coding. Refer to ask_gpt.py file for the sample User-defined Function.
4. Lastly, don't forget to add-in your personal OpenAI API key and organisation API key in keys.py and model_training_service_param_openai.py

Note: Answers filled in by GPT may be questionable or incorrect. 

