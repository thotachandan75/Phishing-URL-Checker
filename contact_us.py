import streamlit as st
import streamlit.components.v1 as components
import main_app


def read_file(filename):
    with open(filename, "r") as f:
        return f.read()


style = '''
<style>
.card {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  max-width: 300px;
  margin: auto;
  text-align: center;
  font-family: arial;
}

.title {
  color: grey;
  font-size: 18px;
}

button {
  border: none;
  outline: 0;
  display: inline-block;
  padding: 8px;
  color: white;
  background-color: #000;
  text-align: center;
  cursor: pointer;
  width: 100%;
  font-size: 18px;
}

a {
  text-decoration: none;
  font-size: 22px;
  color: black;
}

button:hover, a:hover {
  opacity: 0.7;
}
</style>
'''

photo = ["Ankit", "Janhavi", "Chandan", "Sreeprada", "Dakshal", "Nakul", "Mitesh", "Aagusthya"]
name = ["Ankit George Kujur", "Janhavi Anandrao Kulkarni", "Thota Chandan", "Sreeprada Chintaginjala", "Dakshal "
                                                                                                       "Dalsania",
        "Nakul Pandit", "Mitesh Sharma", "Aagusthya Shanker"]
branch = ["CyberSecurity", "CyberSecurity", "Data Science", "Data Science", "CSE Core", "CSE Core", "CSE AI & ML",
          "CSE Core"]
phone = ["9870309656", "7676253668", "7981060514", "7981860686", "7016210624", "6261795202", "9131807413", "7600647562"]


def main():
    style_page = """
    #MainMenu {
        visibility: hidden;
    }

    h1 {
        text-align: center;
    }
    
    h2 {
        text-align: center;
    }
    
    h3 {
        text-align: center;
    }

    footer {
        visibility: hidden;
    }
    """
    st.markdown(style_page, unsafe_allow_html=True)
    
    columns = st.columns([0.75, 0.25])
    with columns[0]:
        st.title("Contact US")
    with columns[1]:
        st.image(f"data:image/png;"
                 f"base64,{main_app.image_to_bytes('contact_us/vit_logo.png')}",
                 caption=None,
                 channels="RGB")

    st.write('This Webapp is curriculum-based project, which is constructed as a part of "Engineering Project in '
             'Community Services" by the students of VIT Bhopal The Key contributors for the project are')

    st.markdown(style, unsafe_allow_html=True)
    columns = st.columns(4)
    with columns[0]:
        image = f"data:image/png;base64,{main_app.image_to_bytes(f'contact_us/{photo[6]}.png')}"
        st.markdown(f'<div class="card"><img src="{image}"'
                    f' alt="{name[6]}" style="width:100%"><h1>{name[6]}'
                    f'</h1><p class="title">{branch[6]}</p><p>VIT Bhopal</p>'
                    f'<p><button>{phone[6]}</button></p>', unsafe_allow_html=True)

        image = f"data:image/png;base64,{main_app.image_to_bytes(f'contact_us/{photo[0]}.png')}"
        st.markdown(f'<div class="card"><img src="{image}"'
                    f' alt="{name[0]}" style="width:100%"><h1>{name[0]}'
                    f'</h1><p class="title">{branch[0]}</p><p>VIT Bhopal</p>'
                    f'<p><button>{phone[0]}</button></p>', unsafe_allow_html=True)

    with columns[1]:
        image = f"data:image/png;base64,{main_app.image_to_bytes(f'contact_us/{photo[2]}.png')}"
        st.markdown(f'<div class="card"><img src="{image}"'
                    f' alt="{name[2]}" style="width:100%"><h1>{name[2]}'
                    f'</h1><p class="title">{branch[2]}</p><p>VIT Bhopal</p>'
                    f'<p><button>{phone[2]}</button></p>', unsafe_allow_html=True)

        image = f"data:image/png;base64,{main_app.image_to_bytes(f'contact_us/{photo[1]}.png')}"
        st.markdown(f'<div class="card"><img src="{image}"'
                    f' alt="{name[1]}" style="width:100%"><h1>{name[1]}'
                    f'</h1><p class="title">{branch[1]}</p><p>VIT Bhopal</p>'
                    f'<p><button>{phone[1]}</button></p>', unsafe_allow_html=True)

    with columns[2]:
        image = f"data:image/png;base64,{main_app.image_to_bytes(f'contact_us/{photo[4]}.png')}"
        st.markdown(f'<div class="card"><img src="{image}"'
                    f' alt="{name[4]}" style="width:100%"><h1>{name[4]}'
                    f'</h1><p class="title">{branch[4]}</p><p>VIT Bhopal</p>'
                    f'<p><button>{phone[4]}</button></p>', unsafe_allow_html=True)

        image = f"data:image/png;base64,{main_app.image_to_bytes(f'contact_us/{photo[5]}.png')}"
        st.markdown(f'<div class="card"><img src="{image}"'
                    f' alt="{name[5]}" style="width:100%"><h1>{name[5]}'
                    f'</h1><p class="title">{branch[5]}</p><p>VIT Bhopal</p>'
                    f'<p><button>{phone[5]}</button></p>', unsafe_allow_html=True)

    with columns[3]:
        image = f"data:image/png;base64,{main_app.image_to_bytes(f'contact_us/{photo[3]}.png')}"
        st.markdown(f'<div class="card"><img src="{image}"'
                    f' alt="{name[3]}" style="width:100%"><h1>{name[3]}'
                    f'</h1><p class="title">{branch[3]}</p><p>VIT Bhopal</p>'
                    f'<p><button>{phone[3]}</button></p>', unsafe_allow_html=True)

        image = f"data:image/png;base64,{main_app.image_to_bytes(f'contact_us/{photo[7]}.png')}"
        st.markdown(f'<div class="card"><img src="{image}"'
                    f' alt="{name[7]}" style="width:100%"><h1>{name[7]}'
                    f'</h1><p class="title">{branch[7]}</p><p>VIT Bhopal</p>'
                    f'<p><button>{phone[7]}</button></p>', unsafe_allow_html=True)
