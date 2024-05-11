import streamlit as st
st.title("My title ")
import streamlit as st

st.markdown('text *element* **Neelaj**')
st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors].''')
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

md = st.text_area('Type in your markdown string (without outer quotes)',
                  "Happy Streamlit-ing! :balloon:")

st.markdown('''{Neelaj}''')

st.markdown(md)
st.title('Data analyst')
st.title('Neel@j is :blue[cool] :sunglasses:')
st.header('This is kolkata knight Riders', divider='rainbow')
st.header('Streamlit is :blue[cool] :sunglasses:')
st.subheader('This is a subheader with a divider', divider='rainbow')
st.subheader('Streamlit is :blue[cool] :sunglasses:')
st.caption('This is a string that explains something above.')
st.caption('A kkr with :blue[colors] and emojis :sunglasses:')
import streamlit as st
code = '''def hello():
    print("Hello kolkata!")'''
st.code(code, language='python')
import streamlit as st

def get_user_name():
    return 'John'

with st.echo():


    def get_punctuation():
        return '!!!'

    greeting = "Hi there, "
    value = get_user_name()
    punctuation = get_punctuation()

    st.write(greeting, value, punctuation)

foo = 'bar'
st.write('Done!')
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')
st.write("This is some text.")

st.slider("This is a slider", 0, 100, (25, 75))

st.divider()  # 👈 Draws a horizontal rule

st.write("This text is between the horizontal rules.")

st.divider()