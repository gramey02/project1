# DNA -> RNA Transcription


def transcribe(seq: str) -> str:
    """
    transcribes DNA to RNA by replacing
    all `T` to `U`
    """
    #.replace() function iterates through letters of seq & replaces "T" with "U" (effectively transcribing the DNA sequence)
    transcript = seq.replace("T", "U") 
    
    return transcript


def reverse_transcribe(seq: str) -> str:
    """
    transcribes DNA to RNA by replacing
    all `T` to `U` then reverses the sequence
    """
    transcript = transcribe(seq) #call transcribe function to transcribe the sequence (convert Ts to Us)
    revTranscript = transcript[::-1] #then reverse the transcribed string using this notation
    
    return revTranscript
