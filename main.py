
import re

def open_file(file_path: str):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None


def count_words(content:str):
    words = content.split()
    count = 0
    for word in words:
        count += 1
        
    return count

def count_character(string: str):
    character_dic = {}
    
    letters = re.findall(r'[a-zA-Z]', string)

    for char in letters:
        char = char.lower()
        if char in character_dic:
            character_dic[char] += 1
        else:
            character_dic[char] = 1

    return character_dic


def create_report(file_path:str):
    content = open_file(file_path)
    if content is None:
        return
    word_count = count_words(content)
    character_count = count_character(content)
    sorted_characters = sorted(character_count.items(), key=lambda x: x[1], reverse=True)
    
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document\n")
    
    for key,value in sorted_characters:
        print(f"The '{key}' character was found {value} times")
        
    print("\n--- End report ---")


def main():
    file_path = "books/frankenstein.txt"
    create_report(file_path)
    
main()