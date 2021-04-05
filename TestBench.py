#!/usr/bin/env python3
import os
while True:
    print("0: Salir")
    print("1: Abrir gtkwave")
    print("2: Generar simulacion de FrequencyDivider")
    x = int(input("ingrese numero: "))
    if x == 0:
        print("salir")
        os.system("clear") 
        break
    elif x == 1:
        os.system("clear")
        os.system("gtkwave *.vcd")        
    elif x == 2:
        os.system("clear")
        print("Generando...")
        os.system("iverilog -o verilogTestBench Hardware/common/frequencyDivider_TB.v Hardware/common/frequencyDivider.v")
        os.system("./verilogTestBench")


        


