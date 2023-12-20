from main import base, shares, reader, end
import streamlit as st
from PIL import Image
import os
import re

def write_html(pr_name, reg_name, link, st=None, rdr=False):
    global base
    global shares
    global reader
    html_file = open("snowflake_data_sharing.html", "w")

    # Update all provider names
    base = re.sub(r'ProviderName', pr_name, base)
    shares = re.sub(r'ProviderName', pr_name, shares)
    reader = re.sub(r'ProviderName', pr_name, reader)

    # Update all region names
    base = re.sub(r'ProviderRegion', reg_name, base)

    # Update link
    base = re.sub(r'SPN_ReferralLink', link, base)

    # Has steps, supports reader
    if st is not None and rdr is True:
        html = base + shares + st + reader + end
    elif st is not None:
        # Has steps, does not support reader
        html = base + shares + st + end
    elif rdr is True:
        html = base + shares + reader + end
    else:
        html = base + shares + end

    # close output file
    html_file.write(html)
    html_file.close()
    return html_file

def main():
    
    image = Image.open('./assets/image3.jpg')
    st.image('./assets/image3.jpg')
    
    st.title("Create a Personalized Doc with Data Sharing Guidelines")

    st.write("Simplify the process of sharing data with your customers by giving them a document that walks them through the process of connecting with you via Snowflake. This app will create a set of data sharing guidelines customized with your company's information to help your customer set up a Snowflake account and connect with you.")

    st.write("To start, please input the requested information, including directions for how a customer can share their Snowflake ID with you. The app will generate a customized HTML document that you can save as a PDF and send to your customers.")

    # Create a form
    with st.form(key='user_input_form'):

        # required
        provider_name = st.text_input('Provider Name (required):')

        # required
        provider_region = st.text_input('Provider Region (required):')

        # optional
        spn_referral_link = st.text_input('SPN Referral Link:')

        # optional
        desc_steps = '''Customers will need to send you their Snowflake account identifier before you can share data with them. Please provide written instructions for how they should give you their account identifier. For example: "Send your account identifier to [email address]” or “Contact your account rep and give them your account ID."'''

        steps = st.text_area(desc_steps)

        # optional
        reader = st.checkbox("Check this box if you will support reader accounts for companies that don't have a Snowflake account")
        
        submit_button = st.form_submit_button('Generate file')
       
    # Capture inputs
    # When button is clicked:
    # Check for errors
    # Check for optional fields set
    # Generate the file with required fields and optional fields
    if submit_button:
        # Validate inputs when button is clicked
        if provider_name == '' or provider_region == '':
            return st.error("File not generated. Required field is not set.")
        
        if spn_referral_link == '':
            spn_referral_link = '<a href="https://signup.snowflake.com/">signup.snowflake.com</a>'
        else:
            spn_referral_link = f'<a href="{spn_referral_link}">{spn_referral_link}</a>'

        # This won't render them in list order, instead 
        # in block rendering, and it's hard to read
        if steps != '':
            steps = "<p>" + steps + "</p>"

        if steps != '' and reader:
            # render everything
            write_html(provider_name, provider_region, spn_referral_link, steps, reader)
        elif steps != '':
            # render portion
            write_html(provider_name, provider_region, spn_referral_link, steps)
        elif reader:
            # render portion
            write_html(provider_name, provider_region, spn_referral_link, reader)
        else:
            # render base
            write_html(provider_name, provider_region, spn_referral_link)

        f = open("snowflake_data_sharing.html", "r")

        st.download_button(label="Download file", data=f, file_name="snowflake_data_sharing.html")

if __name__ == "__main__":
    main()
