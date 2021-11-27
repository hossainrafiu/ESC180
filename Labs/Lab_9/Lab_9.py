import urllib.request

def choose_variant(varients):
    appearances = []
    for varient in varients:
        search_term = ""
        for i in range(len(varient)):
            if varient[i] == " ":
                search_term += "+"
            else:
                search_term += varient[i]
        f = urllib.request.urlopen(f"https://ca.search.yahoo.com/search;_ylt=Av3YHOEya_QRKgRTD8kMWgst17V_?p={search_term}&amp;toggle=1&amp;cop=mss&amp;ei=UTF-8&amp;fr=yfp-t-715&amp;fp=1")
        page = f.read().decode("utf-8")
        f.close()
        index = page.find("About")
        end_index = index+6
        while page[end_index] != " ":
            end_index += 1
        results = page[index+6:end_index+1]
        print("varient:",varient, "-", results)
        appearances.append(int(results.replace(",", "")))
    return varients[appearances.index(max(appearances))]
    
print(choose_variant(["five-year anniversary", "fifth anniversary"]))