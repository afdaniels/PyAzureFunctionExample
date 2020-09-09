import re


def find_name(soup):
    try:
        name = soup.find(id='something').text
        return name
    except:
        return ''


def find_address(soup):
    try:
        soup.findNext
        el = soup.find(text=re.compile("Dirección"))
        result = el.findNext().get_text(separator=u' ')
        return result
    except:
        return ''
