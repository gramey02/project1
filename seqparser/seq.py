# DNA -> RNA Transcription


def transcribe(seq: str) -> str:
    """
    transcribes DNA to RNA by replacing
    all `T` to `U`
    """
    transcript = seq.replace("T", "U") #.replace() function iterates through seq & replaces "T" with "U" (effectively transcribing the DNA sequence)
    
    return transcript


def reverse_transcribe(seq: str) -> str:
    """
    transcribes DNA to RNA by replacing
    all `T` to `U` then reverses the sequence
    """
    transcript = transcribe(seq) #call transcribe function to transcribe the sequence (convert Ts to Us)
    
    reverseDict = {"A":"U", "C":"G", "T":"A", "G":"C"} #create a dictionary to reverse letters in the transcript. A to U, C to G, T to U, and G to C (following what was in the README file)
    
    reverse = seq.maketrans(reverseDict) #make a translation table from the reverse dictionary
    revTranscript = seq.translate(reverse) #create the reverse transcript by calling the translate function, which replaces letters in seq based on the translation table 'reverse'
    
    return revTranscript
