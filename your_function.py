def addProduct(products, id_barang_new, nama_barang, harga_barang):
    # this function doesn't need return value
    # modify this pass with your own implementation
    products[id_barang_new] ={
        "id_barang": id_barang_new,
        "nama_barang": nama_barang,
        "harga_barang": harga_barang,
    }


def calculateTotalPriceAfterDiscount(totalPrice):
    # this function need return value
    # modify this return with your own implementation (consider if else threshold for the discount)
    if totalPrice >= 150000:
        totalPrice= totalPrice * 90/100
    elif totalPrice >= 500000:
        totalPrice= totalPrice * 75/100
    return totalPrice
