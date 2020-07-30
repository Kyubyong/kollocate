# Kollocate: Collocation Search of Korean

Let's find out which words are used together with a certain word. 

## Requirements
* python >=3.6
* whoosh


## Example
```
>>> from kollocate import Kollocate
>>> k = Kollocate()
>>> query = "먹" # drop the final ending "-다" for verbs/adjectives.
>>> collocates = k(query)
>>> for pos, cols in collocates.items():
>>>    print(q + " as " + pos)
>>>    for pos2, cols2 in cols.items():
>>>        print(pos2, ", ".join(word + "(" + str(cnt) + ")" for word, cnt in cols2))
먹 as verb
noun 것(39), 수(29), 음식(23), 등(16), 고기(14), ..
verb 하(33), 않(21), 살(17), 즐기(11), 굽(9), ..
adverb 많이(10), 주로(7), 다(5), 같이(4), 잘(4), ...
determiner 다른(5), 그(2), 여러(1), 세(1), 몇몇(1), 새(1)
adjective 싶(5), 어리(1), 편하(1), 작(1), 좋(1), 손쉽(1), 못하(1)

먹 as noun
noun 붓(3), 종이(2), 묘선(1), 청자(1), 은장도(1), 제조(1), ..
verb 의하(1), 그리(1), 찍(1), 차(1), 늘어놓(1)
adverb 하지만(1)
```