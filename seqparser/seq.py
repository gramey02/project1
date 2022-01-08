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
    
    reverseTranscript = reverse(transcript) #reverse the transcribed string using the reverse function
    
    return revTranscript
