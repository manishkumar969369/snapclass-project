import numpy as np
import io
import librosa
import streamlit as st
from resemblyzer import VoiceEncoder, preprocess_wav

@st.cache_resource
def load_voice_encoder():
    return VoiceEncoder()


def get_voice_embedding(audio_bytes):
    try:
        encoder=load_voice_encoder()

        audio,sr = librosa.load(io.BytesIO(audio_bytes),sr=16000) # convert audio to voice embedding
        wav = preprocess_wav(audio) # removing unncessary silence voice and ready for traning 
        embedding = encoder.embed_utterance(wav)# The pretrained model converts the processed audio into a voice embedding.
        return embedding.tolist()
    except Exception as e:
        st.error('Voice recog error')
        return None
    
def identify_speaker(new_embedding,candidates_dict,thresold=0.65):
    if new_embedding is None or not candidates_dict:
        return None,0.0
    
    best_sid = None
    best_score = -1.0

    for sid,stored_embedding in candidates_dict.items():# check all students embedding
        if stored_embedding:
            similarity = np.dot(new_embedding,stored_embedding)# act like cosine similarity score ==> becz for normalized embeddings, the dot product is equivalent to cosine similarity.
            if similarity > best_score:# cosine score > best score ==> user verified
                best_score = similarity
                best_sid = sid

    if best_score >= thresold:
        return best_sid,best_score
    return None, best_score


def process_bulk_audio(audio_bytes, candidate_dict,thresold=0.65):
    try:
        encoder = load_voice_encoder()

        audio, sr = librosa.load(io.BytesIO(audio_bytes),sr=16000)
        segments = librosa.effects.split(audio,top_db=30)# split silence voice for entire audio clips

        identify_results = {}

        for start, end in segments:
            if(end - start) < sr * 0.5:# voice time should be large like 4 to 5 sec ==> do not very short audio clips
                continue
            segment_audio = audio[start:end]
            wav = preprocess_wav(segment_audio)
            embedding = encoder.embed_utterance(wav)

            sid,score = identify_speaker(embedding, candidate_dict,thresold)

            if sid:
                if sid not in identify_results or score > identify_results[sid]:
                    identify_results[sid] = score

        return identify_results
    except Exception as e:
        st.error('Bulk process error')
        return {}