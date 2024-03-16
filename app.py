import streamlit as st

st.title('球志アプリ')
st.caption('これは球志の動画用のテストアプリです')

# "Say hello"というキャプションのボタンを作成する
if st.button('ボタン'):
    # ボタンが押されればこちらが表示される
    st.write('ボタンを押しました')
else:
    # ボタンが押されなければこちらが表示される
    st.write('何も実行してません')

st.subheader('自己紹介')
st.text('河野球志（13）野球選手で身長は159cm、体重は57kgです。五十市タイガースでは、4番捕手で活躍❗\n'
        '中学は硬式野球チーム「都城ボーイズ」に所属して、主将を務めています❗')
code = '''
import streamlit as st

st.title('きゅうchannel')
'''
st.code(code, language='python')