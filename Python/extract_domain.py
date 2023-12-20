#function that extracts the domain name from a URL, or returns the original string if it's not a valid URL
#optimized solution
def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]

#test
print(domain_name("http://google.com"), "google")
print(domain_name("http://google.co.jp"), "google")
print(domain_name("www.xakep.ru"), "xakep")
print(domain_name("https://youtube.com"), "youtube")
print(domain_name("http://www.codewars.com/kata/"), "codewars")
print(domain_name("http://codewars.com"), "codewars") 