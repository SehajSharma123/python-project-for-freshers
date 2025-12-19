import os
from difflib import SequenceMatcher

def read_file(path):
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()
    except:
        return ""

def similarity(text1, text2):
    return SequenceMatcher(None, text1, text2).ratio() * 100

def check_folder(folder_path):
    files = [f for f in os.listdir(folder_path) if f.endswith(".txt")]

    if len(files) < 2:
        print("Need at least 2 text files.")
        return

    print("\n--- PLAGIARISM REPORT ---\n")

    for i in range(len(files)):
        for j in range(i + 1, len(files)):
            f1 = os.path.join(folder_path, files[i])
            f2 = os.path.join(folder_path, files[j])

            t1 = read_file(f1)
            t2 = read_file(f2)

            score = similarity(t1, t2)
            print(f"{files[i]} <--> {files[j]} : {score:.2f}% similar")

folder = input("Enter folder path containing .txt files: ")
check_folder(folder)
