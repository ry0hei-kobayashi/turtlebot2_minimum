from pocketsphinx import LiveSpeech

for phrase in LiveSpeech(
    lm = False,
    dic = "../dictionary/yes_no.dict",
    #dic = "../dictionary/with_noise.dict",
    jsgf = "../dictionary/yes_no.gram"):
    #jsgf = "../dictionary/with_noise.gram"):
    print(phrase)
