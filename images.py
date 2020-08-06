from bs4 import BeautifulSoup
import requests
import os


def from_xml(path: str) -> list:
    """
    Get a list of URLS from a remote XML files.
    Takes the path to your xml file as input. Returns a python list
    or an error.
    :param path: str: path to an xml file
    :return: urls: list: list of urls
    """
    sitemap_index = ''
    page = ''

    if not path:
        list_of_urls = ''
        print("There doesn't appear to be an xml file here.")
        return []

    try:
        page = requests.get(path)
        sitemap_index = BeautifulSoup(page.content, 'html.parser')
        urls = [element.text for element in
                     sitemap_index.findAll('image:loc')]
    except NameError:
        print('Loaded page with: %s' % page)
        return []

    finally:
        print(f'Created {type(sitemap_index)} object with '
              f'{len(urls)} urls')

        return urls


if __name__ == '__main__':
    path_to_xml = 'https://smutek.net/image-sitemap-1.xml'
    img_urls = from_xml(path_to_xml)
    base_url = 'https://smutek.net'
    base_dir = 'content/img'
    for img_url in img_urls:
        download_url = base_url + img_url
        r = requests.get(download_url, allow_redirects=True)
        save_url = img_url.replace("/app/uploads/", "/")
        file_name = download_url.rsplit('/', 1)[1]
        directory = base_dir + save_url.rsplit('/', 1)[0]
        if not os.path.exists(directory):
            os.makedirs(directory)
        open(directory + file_name, 'wb').write(r.content)
        print(directory + file_name)




