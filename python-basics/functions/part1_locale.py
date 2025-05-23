# Write a function that extracts the language code from a locale. 
# A locale is a combination of a language code, a region, and usually also a character set, e.g en_US.UTF-8.
def extract_language(locale):
    return locale[:2]


print(extract_language('en_US.UTF-8'))      # en
print(extract_language('en_GB.UTF-8'))      # en
print(extract_language('ko_KR.UTF-16'))     # ko

# Alternate solution using the 'split()' method.
def extract_language(locale):
    return locale.split('_')[0]


print(extract_language('en_US.UTF-8'))      # en
print(extract_language('en_GB.UTF-8'))      # en
print(extract_language('ko_KR.UTF-16'))     # ko