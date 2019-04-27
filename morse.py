import RPi.GPIO as GPIO
from tkinter import *
import tkinter.font
import time
from gpiozero import LED

MORSE = {' ': ' ',
        "'": '.----.',
        '(': '-.--.-',
        ')': '-.--.-',
        ',': '--..--',
        '-': '-....-',
        '.': '.-.-.-',
        '/': '-..-.',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        ':': '---...',
        ';': '-.-.-.',
        '?': '..--..',
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '_': '..--.-'}

GPIO.setmode(GPIO.BCM)
LED = 18
GPIO.setup(LED, GPIO.OUT)

win = Tk()
win.title("MORSE Code Converter")
myFont = tkinter.font.Font(family = 'Helverica', size = 14, weight = "bold")

def dot():
    GPIO.output(LED, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(LED, GPIO.LOW)
    time.sleep(0.2)
    
def dash():
    GPIO.output(LED, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(LED, GPIO.LOW)
    time.sleep(0.2)

def convert():
    input = user_input.get()
    for letter in input:
        for symbol in MORSE[letter.upper()]:
            if symbol == '-':
                dash()
            elif symbol == '.':
                dot()
            else:
                time.sleep(0.5)
        time.sleep(0.5)

user_input = Entry(win, font = myFont, width=24, bg= 'yellow')
user_input.grid(row=0, column=0)

button = Button(win, text = 'convert' ,font= myFont, command = convert, bg = 'blue', height=1, width=12)
button.grid(row=1, column=0)                
			