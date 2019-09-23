customers = {
    0:{
        "id":0,
        "name":"John",
        "city":"San Francisco",
        "email":"johny.bravo@cn.com"
    },
    1:{
        "id":1,
        "name":"Mark",
        "city":"Las Vegas",
        "email":"mark.zuckerberg@fb.com"
    },
    2:{
        "id":2,
        "name":"Thomas",
        "city":"Birmingham",
        "email":"thomas.shelby@peakyblinder.com"
    }
}

def search(data, target, search):
    print(data[target][search])

search(customers,1,"email")
search(customers,2, search = "email")