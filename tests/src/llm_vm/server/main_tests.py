import requests
import os
import llm_vm.client as l

if __name__ == '__main__':
    data = l.complete(
        prompt = 'what is the snuff?',
        context = 'repeat the prompt 5 times: ',
        openai_key = os.getenv("OPENAI_API_KEY"),
        stoptoken = 'snuff')
    print(data)
