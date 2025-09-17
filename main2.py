import requests
from bs4 import BeautifulSoup

def get_random_celeste_map_link():
	url = "https://maddie480.ovh/celeste/random-map"
	klic = requests.get(url)
	klic.raise_for_status()
	soup = BeautifulSoup(klic.text, "html.parser")
	# Find the first <a> tag whose href contains 'gamebanana.com/mods/'
	# Try to extract the map link from the meta tag 'og:url'
	meta_tag = soup.find('meta', property='og:url')
	if meta_tag and meta_tag.get('content'):
		print(meta_tag['content'])
	else:
		print("No map link found.")

if __name__ == "__main__":
	get_random_celeste_map_link()