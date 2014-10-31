# concat.py


def concat(filestoconcat):
    files = []
    for i in range(0, len(filestoconcat)):
        if filestoconcat[i] == __file__:
            continue
        files.append(filestoconcat[i])

    outputFile = files[-1]
    outputContent = ""
    output = open(outputFile, "a")
    for i in range(0, len(filestoconcat) - 1):
        file = filestoconcat[i]
        Input = open(file, "r")
        toWrite = Input.read().split("\n")
        output.write("\n".join(toWrite))
        output.write("\n")
        outputContent += ("\n".join(toWrite))
        outputContent += ("\n")
        Input.close()
    output.close
    return outputContent


def main():
    return concat(["file.txt", "file1.txt", "megaaatron.txt"])

if __name__ == "__main__":
    main()
