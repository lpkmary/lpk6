import streamlit as st
st.title('Penyetaraan reaksi antara asam kuat dengan basa kuat')
tab1,tab2,tab3=st.tabs(['Informasi mengenai asam kuat','Informasi mengenai basa kuat','Penyetaraan reaksi'])

with tab1:
    st.header('Informasi mengenai asam kuat', divider='rainbow')
    st.write('Asam kuat adalah asam yang dapat terionisasi sempurna di dalam air')
    st.write('beberapa contoh asam kuat adalah:')
    st.write('Asam klorida (HCL)')
    st.write('Asam nitrat (HNO3)')
    st.write('Asam sulfat (H2SO4)')
    st.write('Asam bromida (HBr)')
    st.write('Asam iodida (HI)')
    st.write('Asam klorat (HClO3)')
    st.write('Asam peklorat (HClO4)')

with tab2:
    st.header('Informasi mengenai basa kuat', divider='rainbow')
    st.write('Asam kuat adalah basa yang dapat terionisasi sempurna di dalam air')
    st.write('beberapa contoh basa kuat adalah:')
    st.write('Litium hidroksida (LiOH)')
    st.write('Natrium hidroksida (NaOH)')
    st.write('Kalium hidroksida (KOH)')
    st.write('Kalsium hidroksida (Ca(OH)2)')
    st.write('Rubidium hidroksida (RbOH)')
    st.write('Stronsium hidroksida (Sr(OH)2)')
    st.write('Sesium hidroksida (CsOH)')
    st.write('Barium hidroksida (Ba(OH)2)')
    st.write('Magnesium hidroksida (Mg(OH)2)')
    st.write('Berilium hidroksida (Be(OH)2)')

with tab3:
    st.header('Penyetaraan reaksi', divider='rainbow')
    st.write('Reaksi antara asam kuat dengan basa kuat akan menghasilkan pH larutan yang dihasilkan bersifat netral atau pH = 7')
    options=st.multiselect(
        'pilih senyawa asam kuat',
        ['HCL','HNO3','H2SO4','HBr','HI','HClO3','HClO4'])
    
    options=st.multiselect(
        'pilih senyawa basa kuat',
        ['LiOH','NaOH','KOH','Ca(OH)2','RbOH','Sr(OH)2','CsOH','Ba(OH)2','Mg(OH)2','Be(OH)2'])
    
    tombol = st.button('Hasil penyetaraan reaksi')