import openai


def set_openai_key(key, org='org-AnPp4ukSu2cNBIlkLonuFUXK'):
    """Sets OpenAI key."""
    openai.organization = org
    openai.api_key = key


class Code:
    def __init__(self):
        print("Model Intilization--->")
        # set_openai_key(API_KEY)

    def query(self, prompt, myKwargs={}):
        """
        wrapper for the API to save the prompt and the result
        """

        # arguments to send the API
        kwargs = {
            # "engine": 'usistextdavinci002',  # Corresponds to the custom name you chose for your model deployment in Azure
            "model": "text-davinci-003",
            "temperature": 0.6,  # increased creativity and randomness
            "max_tokens": 800, # testing 300
            "top_p": 1
        }

        for kwarg in myKwargs:
            kwargs[kwarg] = myKwargs[kwarg]

        r = openai.Completion.create(prompt=prompt, **kwargs)["choices"][0]["text"].strip()
        return r

    #def model_prediction(self, input, api_key):
    def model_prediction(self, prompt, input, api_key, myKwargs={}):
        """
        wrapper for the API to save the prompt and the result
        """
        # Setting the OpenAI API key
        set_openai_key(api_key)
        #output = self.query(defaultPrompt.format(input))
        output = self.query(prompt.format(input), myKwargs)
        return output

