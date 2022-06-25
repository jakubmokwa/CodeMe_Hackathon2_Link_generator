class IdError(Exception):
    pass


class URLError(Exception):
    pass


def get_url():
    prefixes = ('https://', 'http://', 'www.')
    suffixes = ('.pl', '.pl/', '.com', '.com/')
    url = input('Write address of website -> ')
    if not url.startswith(prefixes):
        raise URLError("Prefix incorrect")
    if not url.endswith(suffixes):
        raise URLError("Suffix incorrect")
    return url


def get_id():
    id_num = input('Write your partner id number -> ')
    if len(id_num) != 5:
        raise IdError('Id length is not correct')
    return id_num


def print_menu():
    print("Choose what to convert your link to ")
    print('1: Main page')
    print('2: Product page')
    print('3: Promotion page')
    print('4: Add to cart')
    print('5: Category page')
    print('6: Print all generated links')
    print('7: Delete previous links')
    print('0: Quit')


def print_links():
    with open('generated_links.txt', 'r') as f:
        content = f.read()
    print(content)


def get_inputs():
    try:
        link = get_url()
        id_num = get_id()
    except URLError:
        print("Given link is not correct")
    except IdError as err:
        print(err)
    else:
        return link, id_num


def main_page():
    link, id_num = get_inputs()
    curr_link = link + 'view/' + id_num
    with open('generated_links.txt', 'a') as f:
        f.write(curr_link + '\n')


def clear_file():
    open('generated_links.txt', 'w').close()


def get_inputs_simplified():
    link = input('Write address of website -> ')
    id_num = input('Write your partner id number -> ')
    return link, id_num


def get_new_link(link):
    count = 0
    index = 0
    designed_link = ''
    while count != 3:
        if link[index] == '/':
            count += 1
        designed_link += link[index]
        index += 1
    return designed_link


def get_product_code(link):
    index = link.find(',')
    index += 1
    product_code = ''
    while link[index] != '.':
        product_code += link[index]
        index += 1
    return product_code


def product_page_link():
    link, id_num = get_inputs_simplified()
    index = link.find(',')
    index += 1
    product_code = get_product_code(link)
    link = get_new_link(link)
    link = link + 'view/' + id_num + '/' + product_code
    with open('generated_links.txt', 'a') as f:
        f.write(link + '\n')


def promotion_page():
    link, id_num = get_inputs_simplified()
    url_fragment = 'page/' + id_num + '/promocja'
    link = link.replace('kategorie', url_fragment)
    with open('generated_links.txt', 'a') as f:
        f.write(link + '\n')


def category_page():
    link, id_num = get_inputs_simplified()
    url_fragment = 'page/' + id_num + '/kategorie'
    link = link.replace('kategorie', url_fragment)
    with open('generated_links.txt', 'a') as f:
        f.write(link + '\n')


def add_to_cart():
    link, id_num = get_inputs_simplified()
    curr_link = get_new_link(link)
    product_num = get_product_code(link)
    curr_link += 'add/' + id_num + '/' + product_num
    with open('generated_links.txt', 'a') as f:
        f.write(curr_link + '\n')


def main():
    while True:
        print_menu()
        match input():
            case '1':
                main_page()
            case '2':
                product_page_link()
            case '3':
                promotion_page()
            case '4':
                add_to_cart()
            case '5':
                category_page()
            case '6':
                print_links()
            case '7':
                clear_file()
            case '0':
                break


if __name__ == '__main__':
    main()
