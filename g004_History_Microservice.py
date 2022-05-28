# Author: Sean Grady
# Assignment: CS361 Assignment 6 - Micro Service Design for Teammate
# Description: Microservice being set up for Alex Baker's graphing calculator app.  This is tracking stored equations so the calculator can restore them for use.
import json
import time

def write_to_data(eq):

    with open("f001_Data.txt", "r+") as f:
        lines = f.readlines()
        if len(lines) == 10:
            f.truncate(9)
        f.write(eq)
        f.close()

def listen_for_request():
    status = False

    with open("f002_Instruction.txt", "r+") as f:
        status = f.read()
        f.truncate(0)
        f.seek(0)
        f.close()

    return status

def fetch_data():
    equation_list=[]
    with open("f001_Data.txt", "r+") as f:
        jsonData = json.load(f)
        f.truncate(0)
        f.seek(0)
        f.close()

    equation = jsonData['equation']
    equation_list.append(equation)

    return equation_list

def fetch_equation(line):

    with open("f003_List.txt", "r+") as f:
        lines = f.readlines()
        desired_equation = lines[line:line+1]
        f.close()

    return desired_equation[0][:-2]

def store_data_into_list(data):
    with open("f003_List.txt", "r") as f:
        length = len(f.readlines())
        f.close()


    if length == 10:
        with open("f003_List.txt", "r") as f:
            temp_data = f.read().splitlines(True)
            f.close()
        with open("f003_List.txt", "w") as f:
            f.writelines(temp_data[1:])
            for item in data:
                f.write("%s\n" % item)
                f.close()

    else:
        with open("f003_List.txt", "a") as f:
            for item in data:
                f.write("%s\n" % item)
                f.close()

if __name__ == "__main__":

    print("Micro service Started")

    while True:
        request = listen_for_request()
        print(request)
        if request:
            if request == "Store":
                store_data_into_list(fetch_data())
                break

            elif request[0:8] == "Retrieve":
                retrieve_item = int(request[-1])
                eq = fetch_equation(retrieve_item)
                write_to_data(eq)
                break

    print("Micro service Exit")