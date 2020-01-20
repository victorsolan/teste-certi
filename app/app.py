import socket
from flask import Flask , abort , jsonify
from fullnumbers import unidades,dezenas,centenas,milhares


app = Flask(__name__)

@app.route("/<number>")
def translate(number):
    try:
        if int(number) in range(-99999,99999):
            translated = translate(number) if int(number) >= 0 else f"menos {translate(int(str(number)[1:]))}"
            response = { 'extenso': translated}
            return jsonify(response) ,200
        pass
    except ValueError as error:
        abort(400,"Number out of range , try any number between -99999 and 99999 .")
    

def translate(number):
    return {

        1 : lambda number: unidade(number) ,
        2 : lambda number: dezena(number) ,
        3 : lambda number: centena(number) ,
        4 : lambda number: milhar(number) ,
        5 : lambda number: dezena_milhar(number)
        
    }.get(len(str(number)))(number)


def unidade(number):
    return unidades[number]

def dezena(number):
    num_str = str(number)
    return dezenas[number] if dezenas.get(number) != None  else f"{dezenas[int(num_str[0])]} e {unidades[int(num_str[1])]}"

def centena(number):
    num_str = str(number)
    
    if centenas.get(number) != None:
        return centenas[number]
    elif num_str[1] == "0":
       return f"{centenas[int(num_str[0])]} e {translate(num_str[2:3])}"
    else: 
        return f"{centenas[int(num_str[0])]} e {translate(num_str[1:3])}"

def milhar(number):
    num_str = str(number)

    if milhares.get(number) != None:
        return milhares[number]
    elif num_str[1:3] == "00":
       return f"{milhares[int(num_str[0])]} e {translate(num_str[3:4])}"
    elif num_str[1:2] == "0":
        print("ok")
        return f"{milhares[int(num_str[0])]} e {translate(num_str[2:4])}"
    else: 
        return f"{milhares[int(num_str[0])]} e {translate(num_str[1:4])}"

def dezena_milhar(number):
    num_str = str(number)

    return f"{translate(num_str[0:2])} mil e {translate(num_str[2:5])}"

if __name__ == "__main__":
    app.run(host="0.0.0.0")