DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():

            # FILTRACION CON LIST COMPREHENSION
    # all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"] 
    # all_python_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi" ]
    
    # for worker in all_python_devs:
    #     print(worker)
        
            # FILTRACION CON HIGH ORDER FUNCTIONS (FILTER Y MAP)

    # adults = list(filter(lambda worker: worker["age"]>18, DATA))

        # Aqui aplico el map sobre los resultados de filter

    # adults = list(map(lambda workers: workers["name"], DATA))
    # print(adults)

        # FILTRACION CON H.O Y  SUMAR DICCIONARIO
    
    # old_people = list(map(lambda worker: worker | {"old":worker["age"] > 70}, DATA))
    # for worker in old_people:
    #     print(worker)

                    # RETO 

        # FILTRACION DE LIST COMPREHENSIONS CON FILTER Y MAP

    # print('-' * 20, 'PYTHON DEVS', '-' * 20)
    # all_python_devs = list(filter(lambda worker: worker["language"] == "python" ,DATA))
    # all_python_devs = list(map(lambda worker: worker["name"], DATA))
    # print(all_python_devs)

    # print('-' * 20, 'PLATZI WORKERS', '-' * 20)
    # all_platzi_workers = list(filter(lambda worker: worker["organization"] == "Platzi", DATA))
    # all_platzi_workers = list(map(lambda worker: worker["name"], DATA))
    # print(all_platzi_workers)

        # FILTRACION DE FILTER Y MAP CON LIST COMPREHENSIONS
    
    # adults = [worker["name"] for worker in DATA if worker["age"] > 70]
    # print(adults)


    # old_people = [worker | {'old': worker["age"]} for worker in DATA if worker["age"] > 70 ]
    # print(old_people)




if __name__ =='__main__':
    run()