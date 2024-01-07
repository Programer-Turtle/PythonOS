from bs4 import BeautifulSoup
import requests

def find_summary(soup):
    index = 0
    while True:
        try:
            text = soup.find_all('p')[index].get_text()
            if text != "" and len(text) > 100:
                return text
            else:
                index += 1
        except:
            return "To broad of a subject."

def GetWikiInfo(Article):
    # get URL
    page = requests.get(f"https://en.wikipedia.org/wiki/{Article}")

    #Scrapes Web
    soup = BeautifulSoup(page.content, 'html.parser')

    # Check if the article is not found
    not_found_message = "Wikipedia does not have an article with this exact name."
    if soup.find('b', string=not_found_message) or soup.find_all('p') == []:
        return "Article Not Found"
    else:
        return find_summary(soup)

def main():
    while True:
        userinput = input('What would you like to learn about?\n')
        if(userinput.lower() == "exit"):
            exit()
        print(f"\n{GetWikiInfo(userinput)}")


if __name__ == "__main__":
    main()