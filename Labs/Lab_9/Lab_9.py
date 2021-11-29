import urllib.request

def top10(L):
	top = []
	
	for i in range(10):
		x = max(L)
		top.append(x)
		L.remove(x)

	return top

def inv_dict(d):
	new = {}
	
	for key, value in d.items():
		if value in new.keys():
			new[value].append(key)
		else:
			new[value] = [key]

	return new

def top10words(d):
	top = []
	
	while len(top)<10:
		count = max(d.keys())
		
		for word in d[count]:
			if len(top)<10:
				top.append(word)
		
		del d[count]
	
	return top

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


print(choose_variant( ["top ranked school uoft", "top ranked school waterloo"]))