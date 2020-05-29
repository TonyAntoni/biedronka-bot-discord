import urllib.request
import bs4 as bs

class Biedronka:
	def requested_url(self, request):
		request = request.replace(' ','%20') # Change spaces to '%20'
		url_request = f'https://www.biedronka.pl/pl/searchhub,query,{request}'
		page = urllib.request.urlopen(url_request) # Go to url with user's request
		soup = bs.BeautifulSoup(page, 'lxml')

		for divs in soup.find_all('div', {"class": "productsimple-default"}):
			for a in divs.find_all('a'):
				self.link = a.get('href') # Take first link of the page with requested products
				break
			break

	def get_url(self):
		link = f'https://www.biedronka.pl{self.link}'

		return link

	def get_product(self):
		url = f'https://www.biedronka.pl{self.link}'
		page = urllib.request.urlopen(url) # Going to product page
		soup = bs.BeautifulSoup(page, 'lxml')

		self.product = soup.select_one('#container > div:nth-child(2) > div > div > article > div.prod-cat-descryption > h3') # Taking product online

		for price_box in soup.find_all('span', {'class':'price-wrapper'}):
			for pln in price_box.find_all('span', {'class':'pln'}): # Taking price as PLN (złotówki)
				self.pln = pln

			for gr in price_box.find_all('span', {'class':'gr'}): # Taking price as GR (grosze)
				self.gr = gr

		self.tip_box = soup.find('span', {'class': 'product-promo-tip'})

		if self.tip_box != None: # If page contains 'multi-pack' tag of products
			self.tip = f'{self.tip_box.string}'

			for regular_price in soup.select_one('#container > div:nth-child(2) > div > div > article > div.prod-cat-descryption > span > span:nth-child(1)'):
				self.regular_price = regular_price

		else:
			tip = ''

		return self.product.string

	def get_price(self):
		price = f'{self.pln.string},{self.gr.string}'

		return price

	def get_basis_weight(self):
		url = f'https://www.biedronka.pl{self.link}'
		page = urllib.request.urlopen(url)  # Going to product page
		soup = bs.BeautifulSoup(page, 'lxml')

		basis_weight = soup.select_one('#container > div:nth-child(2) > div > div > article > div.prod-cat-descryption > span > span.product-description.price_per_kg.product173342')

		if basis_weight != None:
			basis_weight = basis_weight.string.replace(' ', '')
		else:
			pass

		return basis_weight

	def get_amount(self):
		url = f'https://www.biedronka.pl{self.link}'
		page = urllib.request.urlopen(url)  # Going to product page
		soup = bs.BeautifulSoup(page, 'lxml')

		for span in soup.find_all('span', {'class':'amount'}):
			amount = span

		return  amount