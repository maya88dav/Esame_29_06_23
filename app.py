#streamlit
import streamlit as st
import requests
import json


def main():
    st.title("Esame del 29/06/23")
    url_API =st.text_input("inserisci url dell'api","http://localhost:8000/predict")
    rdSpend = st.number_input("Inserisci Rdspend")
    administration = st.number_input("Inserisci administration")
    marketingSpend = st.number_input("Inserisci Marketing Spend")

    if st.button("Predict with GET"):
        url = url_API
        url2 = f"?rdSpend={rdSpend}&administration={administration}&marketingSpend={marketingSpend}"
        link = url+url2
        st.write('"{}"'.format(link))
        response = requests.get(link)
        result =response.json()
        st.success(f"The result is: {result['prediction']}")

    if st.button("Predict with POST"):
        url = url_API
        response =requests.post(url,
                                headers={"Content-Type": "application/json"},
                                data = json.dumps({
                                                   "rdSpend": rdSpend,
                                                   "administration":administration,
                                                   "marketingSpend":marketingSpend,
                                                   })
                                )
        result =response.json()
        st.success(f"The result is: {result['prediction']}")   






  



if __name__=="__main__":
    main()   
