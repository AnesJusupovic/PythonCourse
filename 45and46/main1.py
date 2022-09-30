from bs4 import BeautifulSoup

if __name__ == "__main__":
    with open("website.html") as file:
        contents = file.read()
        soup = BeautifulSoup(contents, "html.parser")
        print(soup.title)
        print(soup.prettify())

        all_anchor_tags = soup.find_all(name="a")
        print(all_anchor_tags)
