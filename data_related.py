import json
def save_json(data):
    with open("grupos.json", "w") as write_file:
        json.dump(data, write_file)
        write_file.close()
    print('Você salvou seu arquivo json')

def open_json():
    f = open('grupos.json')  # Opening JSON file
    data = json.load(f)  # returns JSON object as a dictionary
    return(data)
    # Closing file
    f.close()