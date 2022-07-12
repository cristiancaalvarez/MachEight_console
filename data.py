import json
from urllib import request
from os import system
import time

def get_jason(url):
    """Gets the json file

    Parameters
    ----------
    url : string
        contains the url where the data in json format are located

    Returns
    -------
    json_decode
        contains decoded json
    """
    data = request.urlopen(url)
    json_decode = json.loads(data.read().decode('utf-8'))
    return json_decode

def in_input():
    """Gets the height to search for

    Parameters
    ----------
    None

    Returns
    -------
    find_height : int
        contains the height 
    """
    while True:
        try:
            find_height = int(input("Enter the height (in) to search: "))
            system("cls")
            if find_height >= 0:
                break
        except ValueError:
            print("Please enter a number!")
    return find_height

def search_sum(inches, data):
    """Gets the sum of the height of pairs of players that meet the height entered in the in_input() function.

    Parameters
    ----------
    inches : in
        contains the height 
    data : dictionary
        contains the players' data

    Returns
    -------
    None
    """
    height_list, name1, name2 = [], [], []
    for count in range(len(data)):
        value = data[count]['h_in']
        height_list.append(value)
        height_list = [int(value) for value in height_list]
    for count in range(0, len(height_list)):
        for next in range(count+1, len(height_list)-1):
            if height_list[count] + height_list[next] == inches:
                fname1 = data[count]['first_name']
                lname1 = data[count]['last_name']
                fname2 = data[next]['first_name']
                lname2 = data[next]['last_name']
                name1.append(fname1 + " " + lname1)
                name2.append(fname2 + " " + lname2)
    print_function(inches, name1, name2)
    return None

def print_function(inches, Name_1=None, Name_2=None):
    """Prints the pairs of players that when adding their height meet the height entered.

    Parameters
    ----------
    inches : in
        contains the height 
    Name_1 : str
        contains the name of player 1.
    Name_2 : str
        contains the name of player 2.
    
    Returns
    -------
    None
    """
    if len(Name_1) > 0:
        print(inches)
        for i in range(len(Name_1)):
            print('{:^2}{:<20} {:<20}'.format("-",Name_1[i], Name_2[i]))
    else:
        print('No matches found')
    return None

def print_time(TI, TF, output=False):
    """Prints the execution time of the code (by default this function is omitted, if you want to display it you must add a third parameter with value True to the function call).

    Parameters
    ----------
    TI : float
        contains the start time.
    TF : float
        contains the end time.
    Output : boolean
        contains the value whether or not to print the runtime.
    
    Returns
    -------
    None
    """
    if output==False:
        pass
    else:
        print(TF-TI)
    return None

if __name__ == '__main__':
    t1 = time.time()
    url = 'https://mach-eight.uc.r.appspot.com/'
    dict_height = list(get_jason(url).values())[0]
    in_number = in_input()
    search_sum(in_number, dict_height)
    t2 = time.time()
    print_time(t1, t2)