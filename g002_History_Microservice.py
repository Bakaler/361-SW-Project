# Author: Sean Grady
# Assignment: CS361 Assignment 6 - Micro Service Design for Teammate
# Description: Microservice being set up for Alex Baker's graphing calculator app.  This is tracking stored equations so the calculator can restore them for use.

import time
import json

def write_to_data(eq):

    with open("Data.txt", "a") as f:
        f.write(eq)
        f.close()

def listen_for_request():
    status = False

    with open("Instruction.txt", "r+") as f:
        status = f.read()
        f.truncate(0)
        f.seek(0)
        f.close()

    return status

def fetch_data():
    equation_list=[]
    with open("Data.txt", "r+") as f:
        jsonData = json.load(f)
        f.truncate(0)
        f.seek(0)
        f.close()

    equation = jsonData['equation']
    equation_list.append(equation)

    return equation_list

def fetch_equation(line):

    with open("List.txt", "r+") as f:
        lines = f.readlines()
        desired_equation = lines[line:line+1]
        f.close()

    return desired_equation[0][:-2]

def store_data_into_list(data):
    print(data)

    with open("List.txt", "r+") as f:
        f.truncate(0)
        f.seek(0)

        for item in data:
            f.write("%s\n" % item)

        f.close()

if __name__ == "__main__":

    while True:
        time.sleep(1)
        request = listen_for_request()
        print(request)
        if request:
            if request == "Store":
                store_data_into_list(fetch_data())
                break

            elif request[0:8] == "Retrieve":
                retrieve_item = int(request[-1])
                eq = fetch_equation(retrieve_item)
                print(eq)
                write_to_data(eq)
                break

