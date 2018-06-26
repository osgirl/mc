from openpyxl import load_workbook
#from xlrd import open_workbook


def read_file(filename):
    wb = load_workbook(filename)
    wb1 = wb['Sheet1']
    items=[]
    for row in wb1.rows:
        for cell in row:
            item = cell.value
            items.append(item)

    return(items)
def product_check():

    product_total=read_file('product_total.xlsx')
    product_in_store=read_file('product_in_store.xlsx')
    #product_check_list=list(set(product_total) - set(product_in_store))
    product_check_list=list(set(product_total))
    return product_check_list
