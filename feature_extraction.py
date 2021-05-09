import re
import pandas as pd
import numpy as np
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
txt = "Th'e r \is placed $be before & filename TO prevent THE characters in filename string to be treated as special character. For example, if there is \temp in the file address, then \t is treated as the tab character and error is raised of invalid address. The r makes the string raw, that is, it tells that the string is without any special characters. The r can be ignored if the file is in same directory and address is not being placed."

def sent_token(sample_text):
    word = []
    tag = []
    tokenized = sent_tokenize(sample_text)
    for i in tokenized:
        sent_word = i.replace(".", " .")
        wordsList = sent_word.split(" ")
        tagged = nltk.pos_tag(wordsList)
        for t in tagged:
           word.append(t[0])
           tag.append(t[1])
    return word, tag;

def check_upper_first_letter(sample_word):
    try:
        if sample_word[0].isupper():
            result = "true"        
        else:
            result = "flase"
        return result
    except Exception as error:
        return error
        
def check_prev_next_word(word_list):
    try:
       previousWord = ["empty"]+ word_list
       previousWord.pop()
       nextWord = word_list + ["empty"]
       nextWord.pop(0)
       return previousWord, nextWord;
    except Exception as error:
        return error
        
def check_all_case_caps(sample_word):
    try:
        if sample_word.isupper():
             result = "true"
        else:
             result = "false"
        return result
    except Exception as error:
        return error
        
def check_spl_char(sample_word):
    special_characters = "'[@_!#$%^&*()<>?/\|}{~:]'"
    try:
        if any(c in special_characters for c in sample_word):
             result = "true"
        else:
             result = "false"
        return result
    except Exception as error:
        return error
        
def check_len_word(sample_word):
    try:
       lenegth= len(sample_word)
       return lenegth
    except Exception as error:
        return error
        
def check_word_freq(sample_word, word):
    try:
       word_freq = word.count(sample_word)
       return word_freq
    except Exception as error:
        return error

def sample_funct(sample_text):    
    capital = []
    all_caps = []
    len_word = []
    any_spl = []
    wordfreq = []
    
    word, tag = sent_token(sample_text)    
    previousWord, nextWord = check_prev_next_word(word)
    previousTag, nextTag = check_prev_next_word(tag)
    
    for w in word:
        word_freq = check_word_freq(w, word)
        wordfreq.append(word_freq)
        length = check_len_word(w)
        len_word.append(length)
        check_upper = check_upper_first_letter(w)
        capital.append(check_upper)
        all_case_caps = check_all_case_caps(w)
        all_caps.append(all_case_caps)
        spl_char = check_spl_char(w)
        any_spl.append(spl_char)
        previous_capital_let, next_capital_let = check_prev_next_word(capital)
        previous_all_cap_let, next_all_cap_let = check_prev_next_word(all_caps)
        previous_spl_char, next_spl_char = check_prev_next_word(any_spl)
        previous_word_len, next_word_len = check_prev_next_word(len_word)
        previous_word_feq, next_word_feq = check_prev_next_word(wordfreq)
              
    df = pd.DataFrame()
    df["word"] = word
    df["tag"] = tag
    df["previousWord"] = previousWord
    df["nextWord"] = nextWord
    df["previousTag"] = previousTag
    df["nextTag"] = nextTag
    df["first_caps"] = capital
    df["previous_first_caps"] = previous_capital_let
    df["next_first_caps"] = next_capital_let
    df["previous_all_caps"] = previous_all_cap_let
    df["next_all_caps"] = next_all_cap_let
    df["previous_spl_char"] = previous_spl_char
    df["next_spl_char"] = next_spl_char
    df["previous_word_len"] = previous_word_len
    df["next_word_len"] = next_word_len
    df["previous_word_feq"] = previous_word_feq
    df["next_word_feq"] = next_word_feq
    df["len_word"] = len_word
    df["allCaps"] = all_caps
    df["any_spl"] = any_spl
    df["wordfreq"] = wordfreq
    return df
 
test_sample = sample_funct(txt)
test_sample.to_excel("test_sample.xlsx")
