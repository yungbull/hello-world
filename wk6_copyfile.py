# copyfile.py
# Prompts for two file names and copies the contents
# of the first file into the second file

sourceFileName = input("Enter the name of the source file: ")
targetFileName = input("Enter the name of the target file: ")

try:
    # Open the source file for reading
    with open(sourceFileName, 'r') as sourceFile:
        contents = sourceFile.read()

    # Open the target file for writing
    with open(targetFileName, 'w') as targetFile:
        targetFile.write(contents)

    print("File copied successfully.")

except FileNotFoundError:
    print("Error: The source file was not found.")
except Exception as e:
    print("An error occurred:", e)
