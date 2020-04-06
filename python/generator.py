from textgenrnn import textgenrnn
import sys

# --- Set Model ---
inFile = input("\nModel File To Load: ")

if inFile == "":
    print("No Model File Selected, Quitting!")
    sys.exit()

textgen = textgenrnn(inFile)

# --- Set Texts ---
textAmount = 10

try:
    textAmount = int(input("\nTexts To Output (Default = 10): "))
except:
    print("Invalid Number Of Texts, Setting To 10")

# --- Set Creativity ---
temp = 0.5

try:
    temp = float(input("\nCreativity (Default = 0.5): "))
except:
    print("Invalid Float, Setting To 0.5")


textgen.generate_to_file("output.txt", n=textAmount, temperature=temp)
print("\nDone! Written in output.txt")
