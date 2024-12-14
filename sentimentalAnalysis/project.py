import os
import csv
import requests
from bs4 import BeautifulSoup
from googlesearch import search
import openai
import tiktoken
import sys




def main():
    validate(input("Input the symbolic repersentation of any Fortune 500 Company you are considering to invest in: ").upper().strip())



def validate(symbol):
    with open('stocks.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        #Checks that there is a symbolic repersentation within stocks.csv
        for row in reader:
            if symbol == row['Symbol']:
                stock = row['Security']
                print(scan(stock))
                return
            else:
                pass
        raise sys.exit("Try inputting the symbol for the company")



def scan(stock):
    query = f"Is it worth investing in {stock} stock?"
    #Sends a search with the stock and returns the top 10 google web results
    search_results = search(query, num_results=10)
    with open('URLs.txt', 'w') as file:
        for url in search_results:
            file.write(url.strip() + '\n')
    return scrape(search_results, stock)

def scrape(results, stock):
    contents = []
    for url in results:

        #agent to get around some premissions
        agent = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=agent)

        #using soup as a html parser to get rid of as many ads as possible so they don't take up the token limit
        soup = BeautifulSoup(response.text, 'html.parser')

        main_content = None

        #consider anything within these tags of HTML to be main content that shoudl be parsed seperately to reduce size
        for tag in ['article', 'main', 'section']:
            main_content = soup.find(tag)
            if main_content:
                break

        if not main_content:
            main_content = soup

        content = main_content.get_text(separator='\n', strip=True)
        contents.append(content)

    full_content = "\n\n".join(contents)

    #Trim and count the tokens to ensure there is no errors going over the cap and taking the maxiumum amount of information possible
    max_tokens = 15500
    full_content = trim_tokens(full_content, max_tokens)


    return sentiment(full_content, stock)

def count_tokens(context):
    encoding = tiktoken.encoding_for_model("gpt-3.5-turbo-16k")
    tokens = encoding.encode(context)
    return len(tokens)

def trim_tokens(context, max_tokens):
    tokens = count_tokens(context)
    if tokens > max_tokens:
        encoding = tiktoken.encoding_for_model("gpt-3.5-turbo-16k")
        token_list = encoding.encode(context)
        trim_token_list = token_list[:max_tokens]
        trim_context = encoding.decode(trim_token_list)
        return trim_context
    else:
        return context


def sentiment(context, stock):
    openai.api_key = os.getenv("OPENAI_API_KEY")    
    
    if openai.api_key == None:
        raise ValueError("API key is not set in enviorment variables")
    
    #this is a specific message sent to ChatGPT that informs its role as a financial advisor and gives it three possible options. then it outline what a possible response should look like
    messages = [
        {"role": "system", "content": f"You are a financial advisor who only gives decisive Buy, Sell, Or Hold chioces in {stock} stock."},
        {
            "role": "user",
            "content": (
                f"You are a financial advisor and are provided with multiple articles to determine if {stock} is worth investing in. "
                "Your response should be either a yes or no. It should also have multiple reasons as to why or why not invest as given by the context below. "
                "This is an example for a fake financial analysis of Phone Corp:\n\n"
                "Phone Corp is a poor choice of investment because\n\n"
                "1. The Corp Phone remains their primary driver of revenue and there are concerns about weak sales, particularly in India.\n"
                "2. Phone Corps's stock is currently trading at a higher valuation compared to its historical average and the broader market so it could be relatively risky.\n"
                "3. Phone Corp's lack of focus on artificial intelligence has customers concerned about innovation at the company and has led to lower sales.\n\n"
                "For the reasons listed above, Phone Corp would be a poor investment right now.\n"
                f"Just like the prompt did above, give a concrete analysis based on the context below of {stock} and decide if it is worth an investment" + context
            )
        }
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=messages,
        temperature=0.1,
        max_tokens=400,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    #prints out the message here
    sentiment_analysis = response["choices"][0]["message"]["content"]
    return "Sentiment Analysis: " + sentiment_analysis


if __name__ == "__main__":
    main()

