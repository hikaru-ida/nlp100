import knock020

country_text = knock020.get_text('イギリス')

def main(my_country):
        item = my_country.strip().split('\n')
        file_list = [line.strip() for line in item if line.startswith('[[ファイル:')]
        print('\n'.join(file_list))

main(country_text)
