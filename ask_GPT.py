import xlwings as xw
from keys import OPENAI_API_KEY
from model_training_service_param_openai import Code

pred = Code()
api_key_openai = OPENAI_API_KEY


def main():
    wb = xw.Book.caller()
    ws = wb.sheets[0]


def process_prompt(prompt, input, myKwargs={}):
    return pred.model_prediction(prompt=prompt, input=input, api_key=api_key_openai, myKwargs=myKwargs)


@xw.func
@xw.func
@xw.arg('country', doc='The country you want to know more about')
@xw.arg('country_info', doc='A parameter that you can ask about a country. The function currently supports Captial, GDP, Population')
def ask_GPT(country, country_info):
    """
    Sample function which to show how GPT can be integrated with Excel.
    """
    prompt = """What is the {country_info} of {country}. Only return the country's {country_info}."""

    dynamic_input = {
        "country": country,
        "country_info": country_info
    }
    question = prompt.format(**dynamic_input)

    answer = process_prompt(prompt=question, input="")

    return answer


if __name__ == "__main__":
    xw.Book("excel_xlwings.xlsm").set_mock_caller()
    main()

