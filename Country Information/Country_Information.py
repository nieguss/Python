# Created as exercise to OR!ON's code.

"""After pressing RUN, enter a country name or leave it empty to see Poland"""

from urllib import request
from urllib import error
import json


api_endpoint = "https://restcountries.eu/rest/v2/name/"
user_input = input() or "poland"
api_query = f"{api_endpoint}{user_input}?fullText=true"

line1 = "─" * 34


def space(my_str):
    """This inserts necessary spaces between key and value"""
    return ' ' * (16 - len(my_str))


def simplify(word):
    """This function simplify camelCase or snake_case words to Camel Case
    and Snake Case respectively"""
    new = ""
    for index, char in enumerate(word):
        if index == 0:  # capitalizing first letter
            new += char.upper()
        elif char.isupper():  # inserting space and letter if capital letter
            new += " " + char
        elif char == "_":  # inserting space and next letter after capitalizing
            new += " "
            new += word[index + 1].upper()
        else:  # if there is not a underscore behind that letter add that
            if word[index - 1] != "_":
                new += char
    return new  # returning the new simplified word


try:  # trying to catch 404 error
    country_info = json.load(request.urlopen(api_query))[0]
except error.HTTPError:
    print(f"Name Error! Specified country '{user_input}' was not found.")
else:  # if no error happens this runs
    # printing info in beautiful format
    # looping over key value of the country_info
    for key, val in country_info.items():
        print(line1)
        # if val is neither a list nor a dictionary
        if type(val) is not list and type(val) is not dict:
            simple_key = simplify(key)
            print(f"{simple_key}{space(simple_key)}: {val}")
        # if val is a dictionary getting key values out of it
        elif type(val) is dict:
            simple_key = simplify(key)
            print(f"{simple_key}{space(simple_key)}: ")
            for subkey, subval in val.items():
                print("\t" * 14, f"{simplify(subkey)}: {subval}")
        # if val is a list
        elif type(val) is list:

            # making sure that the list is not empty
            if len(val) != 0:
                # if key is latlng (latitude and longitude)
                # custom defined its keys because the key provided is not
                # appropriate
                if key == "latlng":
                    print(f"Latitude{space('latitude')}:" +
                          f"{val[0]}\nLongitude{space('longitude')}: {val[1]}")
                # checking whether there is a dictionary inside the list or not
                elif type(val[0]) is dict:
                    simple_key = simplify(key)
                    print(f"{simple_key}{space(simple_key)}: ")

                    # if there is a dictionary inside the list looping over its
                    # items
                    for lang_info in val:
                        for subkey, subval in lang_info.items():
                            if type(subval) is list:
                                # if there is a list inside a dictionary and
                                # that list is empty it inserts a '-' (hyphen)
                                print("\t" * 14, f"{simplify(subkey)}:", end="")
                                if len(subval) != 0:
                                    print(', '.join(subval))
                                else:
                                    print("-")
                            # if there is not a list inside the dictionary
                            else:
                                print(
                                    "\t" * 14, f"{simplify(subkey)}: {subval}")

                else:  # if above conditions doesn't meet
                    simple_key = simplify(key)
                    print(f"{simple_key}{space(simple_key)}: {', '.join(val)}")
