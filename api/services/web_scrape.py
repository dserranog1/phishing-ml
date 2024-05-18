from bs4 import BeautifulSoup
import requests


def extract_features(soup):
    features = {
        "has_title": 1 if soup.title else 0,
        "has_input": 1 if soup.find("input") else 0,
        "has_button": 1 if soup.find("button") else 0,
        "has_image": 1 if soup.find("img") else 0,
        "has_submit": 1 if soup.find("input", type="submit") else 0,
        "has_link": 1 if soup.find("a") else 0,
        "has_password": 1 if soup.find("input", type="password") else 0,
        "has_email_input": 1 if soup.find("input", type="email") else 0,
        "has_hidden_element": 1 if soup.find(attrs={"type": "hidden"}) else 0,
        "has_audio": 1 if soup.find("audio") else 0,
        "has_video": 1 if soup.find("video") else 0,
        "number_of_inputs": len(soup.find_all("input")),
        "number_of_buttons": len(soup.find_all("button")),
        "number_of_images": len(soup.find_all("img")),
        "number_of_option": len(soup.find_all("option")),
        "number_of_list": len(soup.find_all(["ul", "ol"])),
        "number_of_th": len(soup.find_all("th")),
        "number_of_tr": len(soup.find_all("tr")),
        "number_of_href": len(soup.find_all(href=True)),
        "number_of_paragraph": len(soup.find_all("p")),
        "number_of_script": len(soup.find_all("script")),
        "length_of_title": len(soup.title.string) if soup.title else 0,
        "has_h1": 1 if soup.find("h1") else 0,
        "has_h2": 1 if soup.find("h2") else 0,
        "has_h3": 1 if soup.find("h3") else 0,
        "length_of_text": len(soup.get_text()),
        "number_of_clickable_button": len(
            [btn for btn in soup.find_all("button") if btn.has_attr("onclick")]
        ),
        "number_of_a": len(soup.find_all("a")),
        "number_of_img": len(soup.find_all("img")),
        "number_of_div": len(soup.find_all("div")),
        "number_of_figure": len(soup.find_all("figure")),
        "has_footer": 1 if soup.find("footer") else 0,
        "has_form": 1 if soup.find("form") else 0,
        "has_text_area": 1 if soup.find("textarea") else 0,
        "has_iframe": 1 if soup.find("iframe") else 0,
        "has_text_input": 1 if soup.find("input", type="text") else 0,
        "number_of_meta": len(soup.find_all("meta")),
        "has_nav": 1 if soup.find("nav") else 0,
        "has_object": 1 if soup.find("object") else 0,
        "has_picture": 1 if soup.find("picture") else 0,
        "number_of_sources": len(soup.find_all("source")),
        "number_of_span": len(soup.find_all("span")),
        "number_of_table": len(soup.find_all("table")),
    }
    return features


def get_website_features(url):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    return extract_features(soup)
