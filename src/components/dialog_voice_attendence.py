import streamlit as st

import numpy as np
import pandas as pd
from src.pipelines.voice_pipeline import process_bulk_audio
from src.database.config import supabase
from datetime import datetime
from src.components.dialog_attendence_results import show_attendence_results


@st.dialog("Voice Attendence")
def voice_attendence_dialog(selected_subject_id):
    st.write("Record audio of students saying I m present . Then AI will marked your Attendence")

    audio_data = None

    audio_data = st.audio_input("Record class room voice for marked attendence",key='voice_audio')
    
    
    if st.button('Analyze Audio ',width='stretch' , type='primary'):
        if not audio_data:
            st.warning("Please upload students voice")
            return
        with st.spinner('Processing Audio data'):

            enrolled_res = supabase.table('subject_students').select("*, students(*)").eq('subject_id',selected_subject_id).execute()
            enrolled_student = enrolled_res.data

            if not enrolled_student:
                st.warning('No Student enrolled in this course')
            else:
                results, attendence_to_log = [], []

            candidate_dict = {
                s['students']['student_id'] : s['students']['voice_embedding']
                for s in enrolled_student if s['students'].get('voice_embedding')
            }

            if not candidate_dict:
                st.error('No Enrolled students have voice profile registered!')
                return
            
            audio_bytes = audio_data.read()

            detectd_score = process_bulk_audio(audio_bytes, candidate_dict)


            results, attendence_to_log = [], []


            current_timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")


            for node in enrolled_student:
                student = node['students']
                score = detectd_score.get(student['student_id'],0.0)
                is_present = bool(score) > 0

                results.append(# frontend show
                    {
                        "Name": student['name'],
                        "ID":student['student_id'],
                        "Source": score if is_present else "-",
                        "Status":"✅ Present" if is_present else "❌ Absent"
                    }
                )

                attendence_to_log.append(
                    {
                        'student_id':student["student_id"],
                        'subject_id': selected_subject_id,
                        'timestamp':current_timestamp,
                        "is_present": bool(is_present),
                    }
                )

            st.session_state.voice_attendence_results =(pd.DataFrame(results),attendence_to_log)


    if st.session_state.get('voice_attendence_results'):
        st.divider()

        df_results,logs = st.session_state.voice_attendence_results 
        show_attendence_results(df_results,logs) 


