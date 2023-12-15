import requests
from bs4 import BeautifulSoup


def main(url_param):
    csv_list = []
    response = requests.get(url_param)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        listing = soup.find_all('li', class_='flex flex-col xl:flex-row xl:items-center gap-4 rounded-lg bg-white p-6 shadow')
        print(len(listing))
        for list in listing:
            asset_classes = ""
            company_name = list.find('p', class_="label-01 leading-normal text-black").text
            description = list.find('div', class_="xl:hidden body-04 leading-normal text-brand-gray-600 wrap").text
            asset_class = list.find_all('span', class_="inline-flex items-center max-w-fit whitespace-nowrap px-2 py-0.5 text-xs font-medium rounded bg-body-100 text-body-800")
            for asset in asset_class:
                asset_classes.append(asset.text)

            #asset_region = list.find('span', class_="flex flex-col flex-none xl:ml-4 hidden xl:flex").text
            website = list.find('a', class_="transition-all flex items-center whitespace-nowrap select-none hover:shadow-sm justify-center bg-brand-gray-800 text-white font-light border border-brand-gray-800 hover:bg-brand-gray-700 text-sm py-2 px-6 rounded w-full")
            href = website['href']
            live = list.find('span', class_="uppercase").text
            
            print([company_name, description, href, live])
            asset_classes = []
    pass


if __name__=="__main__":
    url = "https://app.rwa.xyz/directory"
    main(url)