'''Semantic Similarity

Author: Rafiu Hossain
'''

from cmath import sqrt
import math
from operator import index

from itsdangerous import encoding
from sympy import re


def norm(vec):
    '''Return the norm of a vector stored as a dictionary,
    as described in the handout for Project 3.
    '''
    
    sum_of_squares = 0.0  
    for x in vec:
        sum_of_squares += vec[x] * vec[x]
    
    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
    top_sum = 0

    for word in vec1:
        if word in list(vec2.keys()):
            top_sum += vec1[word]*vec2[word]

    if (norm(vec1)*norm(vec2)) == 0:
        return -1
    return top_sum / (norm(vec1)*norm(vec2))


def build_semantic_descriptors(sentences):
    descriptors = {}
    for sentence in sentences:
        print(sentence) #####################################
        for i in range(len(sentence)):
            sentence[i] = sentence[i].lower()
        for word in sentence:
            if word == '':
                continue
            if word not in descriptors:
                descriptors[word] = {}
            # May need to add the following commented out code
            #added = []
            for other_word in sentence:
                if other_word == '':
                    continue
                if (other_word != word):    # and (other_word not in added):
                    if other_word not in list(descriptors[word].keys()):
                        descriptors[word][other_word] = 0
                    descriptors[word][other_word] += 1
                    #added.append(other_word)
    return descriptors

def build_semantic_descriptors_from_files(filenames):
    all_sentences = []
    for file in filenames:
        f = open(file, "r", encoding="utf-8")
        text = f.read()
        f.close()
        text = text.replace("\n"," ")
        text = text.replace(",","")
        text = text.replace("--"," ") # replaces with space
        text = text.replace(":","")
        text = text.replace(";","")
        #text = text.replace("\"","")
        
        text = text.replace("!",".")
        text = text.replace("?",".")
        sentences = text.split(".")
        for i in range(len(sentences)):
            sentences[i] = sentences[i].lower().split(" ")
        all_sentences.extend(sentences)
    #return all_sentences
    return build_semantic_descriptors(all_sentences)


def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    choices_scores = []
    for choice in choices:
        if (word not in list(semantic_descriptors.keys())) or (choice not in list(semantic_descriptors.keys())):
            choices_scores.append(-1)
            continue
        print(semantic_descriptors[word])
        print(semantic_descriptors[choice])
        score = similarity_fn(semantic_descriptors[word], semantic_descriptors[choice])
        print(score)
        choices_scores.append(score)
    return choices[choices_scores.index(max(choices_scores))]


def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    right = 0
    wrong = 0
    f = open(filename, "r", encoding="utf-8")
    tests = f.read().split("\n")
    f.close()
    for test in tests:
        if test == "":
            continue
        print(test) ############################
        test = test.split(" ")
        word = test[0]
        answer = test[1]
        choices = test[2:]
        my_answer = most_similar_word(word, choices, semantic_descriptors, similarity_fn)
        print("--",answer,my_answer)
        if my_answer == answer:
            right += 1
        else:
            wrong += 1
    return (right/(right+wrong))*100

if __name__ == "__main__":
    # print(cosine_similarity({"a": 1, "b": 2, "c": 3}, {"b": 4, "c": 5, "d": 6}))
    # print(build_semantic_descriptors([["i", "am", "a", "sick", "man"],
    #     ["i", "am", "a", "spiteful", "man"],
    #     ["i", "am", "an", "unattractive", "man"],
    #     ["i", "believe", "my", "liver", "is", "diseased"],
    #     ["however", "i", "know", "nothing", "at", "all", "about", "my",
    #     "disease", "and", "do", "not", "know", "for", "certain", "what", "ails", "me"]]))
    sem_descriptors = build_semantic_descriptors_from_files(["wp.txt", "sw.txt"])
    res = run_similarity_test("test.txt", sem_descriptors, cosine_similarity)
    print(res, "of the guesses were correct")