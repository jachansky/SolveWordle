#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 09:26:08 2024

@author: karichansky
"""
import random

def main():
    
    #Get List of Possible Solutions
    file = open("Dictionaries/wordle-La.txt")
    wordList = file.readlines()
    #remove \n
    dictionary = {}
    for word in wordList:
        dictionary[word[:-1]] = Word(word[:-1])
    
    
    #set up letters
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    letters = {}
    for letter in alphabet:
        letters[letter] = Letter(letter)
    
    
    while True:
        #get first guess
        #guess = input("enter guess: ")
        guess = chooseWord(dictionary)
        
        while dictionary.get(guess,-1) == -1:
            guess = input("word not available, try again: ")          
        dictionary.pop(guess)
        print("word chosen: " + guess)
            
        print("enter guess results, by typing 5 digits: ")
        results = input("0 for each gray letter, 1 for each yellow letter, and 2 for each green letter: ")
        if results == "22222":
            print("we win!")
            break
        
        for index in range(0,5):
            letters[guess[index]].updateColor(index,int(results[index]))
            

        wordsForPopping = []
        for word in dictionary:
            if dictionary[word].isPossible(letters) == False:
                wordsForPopping.append(word)
        
        
        for word in wordsForPopping:
            dictionary.pop(word)
                
        for word in dictionary:
            print(word)
    
        
        
class Word:
    
    def __init__(self, word):
        self.word = word
    
    def isPossible(self, letters):
        #for every letter
        for character in letters:
            
            #if any letters aren't available remove the word
            if self.word.find(character) != -1:
                if letters[character].available == False:
                    return False
                
            #for any yellow positions
            for index in letters[character].yellowOn:
                #remove word if yellow position matches letters or if the word doesn't contain the character
                if self.word.find(character) == -1 or self.word[index] == character:
                    return False
                
            #for any green positions
            for index in letters[character].greenOn:
                #remove the word if the green index doesn't match the letter
                if self.word[index] != character:
                    return False
        return True
                
    

class Letter:
    
    def __init__(self, letter):
        self.letter = letter
        self.available = True
        self.yellowOn = []
        self.greenOn = []
    
    def updateColor(self,index,result):
        if result == 0:
            self.available = False
        elif result == 1:
            self.yellowOn.append(index)
        elif result == 2:
            self.greenOn.append(index)
        else:
            print("bad number entered")
        
def chooseWord(dictionary):
    return random.choice(list(dictionary.keys()))
        
        
if __name__ == "__main__":
    main()

