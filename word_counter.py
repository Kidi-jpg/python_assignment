from collections import defaultdict  

def word_counter():
    text = input("Enter a sentence or paragraph: ")
   
    words = text.split()
    word_counts = defaultdict(int)
    
    for word in words:
        word_counts[word.lower()] += 1  
    
 
    print(f"\nTotal words: {len(words)}")
    print("\nWord frequencies:")
    for word, count in word_counts.items():
        print(f"'{word}': {count} times")
   
    if word_counts:
        most_common = max(word_counts.items(), key=lambda x: x[1])
        print(f"\nMost frequent word: '{most_common[0]}' (appears {most_common[1]} times)")


word_counter()