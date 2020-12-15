import requests

cveSearchDatabase = "https://cve.circl.lu/api/"

# Gets list of all vendors.
def cvesGetAllVendors():
    try:
        r = requests.get(cveSearchDatabase + "/browse")
        return r
    except Exception as e:
        print(e)

# Gets list of all products from a specific vendor.
def cvesGetAllProducts(vendor):
    try:
        r = requests.get(cveSearchDatabase + "/browse/" + vendor)
        return r
    except Exception as e:
        print(e)

# Gets all vulnerabilities per vendor and specific product.
def cvesGetSpecificProduct(vendor, product):
    try:
        r = requests.get(cveSearchDatabase + "/search/" + vendor + "/" + product)
        return r
    except Exception as e:
        print(e)

# Gets a JSON of a specific CVE ID.
def cvesGetId(ID):
    try:
        r = requests.get(cveSearchDatabase + "/cve/" + ID)
        return r
    except Exception as e:
        print(e)

# Gets last 30 CVEs.
def cvesGetLastCves():
    try:
        r = requests.get(cveSearchDatabase + "/last")
        return r
    except Exception as e:
        print(e)