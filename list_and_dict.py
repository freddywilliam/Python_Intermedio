def run():
    my_list = [1, 'HELLO', True, 4.5]
    my_dict = {'firstname' : 'William', 'lastname' : 'Martinez'}
    
    super_list = [
        {'firstname' : 'William', 'lastname' : 'Martinez'},
        {'firstname' : 'Freddy', 'lastname' : 'Martinez'},
    ]

    super_dict = {
        'natural_nums': [1,2,3,4,5,7],
        'integer_nums': [-1,-2,-3,-4,-5],
    }

    for key, value in super_dict.items():
        print(key, '-', value)
    
    for i in super_list:
        print(i)

if __name__ == '__main__':
    run()