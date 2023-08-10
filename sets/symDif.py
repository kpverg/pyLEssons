#symmetric differeccnce
morningLAng={'java','python','c','Ruby','lisp'}
AfternoonLang={'python','c','Ruby','lisp','C++'}
#possibleCorses=morningLAng^AfternoonLang
possibleCorses=morningLAng.symmetric_difference(AfternoonLang)
print(possibleCorses)