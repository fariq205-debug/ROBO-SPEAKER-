import os

if __name__ == "__main__":
    print("Welcome to RoboSpeaker created by Mohammed Fariq")

    while True:
        x = input("Enter what you want me to speak: ")

        if x.lower() == "q":
            os.system(
                'PowerShell -Command "Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'Goodbye\')"'
            )
            break

        command = f'PowerShell -Command "Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{x}\')"'
        os.system(command)