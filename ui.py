import streamlit as st
from PIL import Image
import os
import re

def write_html(pr_name, reg_name, link, st=None, rdr=False, m_accts=False):
    import jinja2

    from main import template_text

    html_file = open("snowflake_data_sharing.html", "w")

    environment = jinja2.Environment()
    template = environment.from_string(template_text)

    html = template.render(
        provider_name=pr_name,
        region_name=reg_name,
        spn_referral_link=link,
        steps=st,
        reader=rdr,
        managed_accounts=m_accts
    )

    # close output file
    html_file.write(html)
    html_file.close()
    return html_file

def main():
    region_list = [
        'AWS Asia Pacific (Jakarta)',
        'AWS Asia Pacific (Mumbai)',
        'AWS Asia Pacific (Osaka)',
        'AWS Asia Pacific (Seoul)',
        'AWS Asia Pacific (Singapore)',
        'AWS Asia Pacific (Sydney)',
        'AWS Asia Pacific (Tokyo)',
        'AWS Canada (Central)',
        'AWS EU (Frankfurt)',
        'AWS EU (Ireland)',
        'AWS EU (Paris)',
        'AWS EU (Stockholm)',
        'AWS EU (Zurich)',
        'AWS Europe (London)',
        'AWS South America (Sao Paulo)',
        'AWS US East (N. Virginia)',
        'AWS US East (Ohio)',
        'AWS US Gov East 1 (FedRAMP High Plus)',
        'AWS US Gov West 1 (FedRAMP High Plus)',
        'AWS US West (Oregon)',
        'GCP Europe West2 (London)',
        'GCP Europe West3 (Frankfurt)',
        'GCP Europe West4 (Netherlands)',
        'GCP Middle East Central2 (Dammam)',
        'GCP US Central1 (Iowa)',
        'GCP US East4 (N. Virginia)',
        'Microsoft Azure Australia East (New South Wales)',
        'Microsoft Azure Canada Central (Toronto)',
        'Microsoft Azure Central India (Pune)',
        'Microsoft Azure Central US (Iowa)',
        'Microsoft Azure East US 2 (Virginia)',
        'Microsoft Azure Japan East (Tokyo)',
        'Microsoft Azure North Europe (Ireland)',
        'Microsoft Azure South Central US (Texas)',
        'Microsoft Azure Southeast Asia (Singapore)',
        'Microsoft Azure Switzerland North (Zurich)',
        'Microsoft Azure UAE North (Dubai)',
        'Microsoft Azure UK South (London)',
        'Microsoft Azure US Gov Virginia (FedRAMP High Plus)',
        'Microsoft Azure West Europe (Netherlands)',
        'Microsoft Azure West US 2 (Washington)']

    image = Image.open('./assets/image3.jpg')
    st.image('./assets/image3.jpg')

    st.title("Customize a Guidelines Doc for Sharing Data via Snowflake")

    st.write("Simplify the process of sharing data with your customers or requesting data from providers: give them a how-to-share document customized with your company's name and preferences. This app will create a set of data sharing guidelines to help your customer or your provider connect with you through their existing Snowflake account or by setting up a new Snowflake account.")

    st.markdown("[Click here to see a sample PDF.](https://www.snowflake.com/wp-content/uploads/2024/03/Sample-Doc-How-to-Use-Snowflake-to-Share-Data.pdf)")

    st.write("To get started, please select if you want to provide or receive data and fill out the form as completely as possible. The app will generate a customized HTML document that you can save as a PDF and distribute. You can return to the app and create additional versions as needed.")

    st.markdown('**Choose the type of document you need**')
    form_type = st.selectbox(label="", index=None, options=["Receiver", "Provider"], format_func=lambda x: {"Receiver": "I want to receive data", "Provider": "I want to provide data"}[x], label_visibility="collapsed")

    if form_type:
        # Create a form
        with st.form(key='user_input_form'):
            # Name required
            if form_type == 'Provider':
                name_field_name = "Provider Name"
            else:
                name_field_name = "Your Company Name"
            st.markdown(f'**{name_field_name} (required)**')
            name = st.text_input('How do you want to refer to your organization in this document? The text you enter will be used to customize the document.')

            # Region required
            if form_type == 'Provider':
                region_field_name = "Provider Region"
                st.markdown(f'**{region_field_name} (required)**')
                region = st.selectbox(
                    label='Please select your relevant cloud region from the menu. This will make it easy for the customer to match it to the region options they see during account setup.',
                    options=region_list,
                    index=None
                    )
            else:
                region_field_name = "Your Cloud Region"
                st.markdown(f'**{region_field_name} (required)**')
                region = st.selectbox(
                    label='Please select your relevant cloud region from the menu. This will make it easy for the provider to match it to the region options they see during account setup.',
                    options=region_list,
                    index=None
                    )

            # optional
            if form_type == 'Provider':
                st.markdown('**SPN Referral Link (if available)**')
                spn_referral_link = st.text_input('If you have a personalized link to the Snowflake free trial for Snowflake referral partners, insert it here. To learn more about this program, contact your Snowflake account team. If you leave this field blank, your customer will be directed to the default Snowflake trial signup page.')
            else:
                spn_referral_link = ''

            # Instructions optional
            if form_type == 'Provider':
                st.markdown('**Instructions to submit Snowflake ID**')
                desc_steps = '''Customers will need to send you their Snowflake account identifier before you can share data with them. Please provide written instructions for how they should give you their account identifier. For example: "Send your account identifier to [email address]” or “Contact your account rep and give them your account ID."'''
                steps = st.text_area(desc_steps)
            else:
                steps = ''

            # reader accounts optional
            if form_type == 'Provider':
                reader = st.checkbox("Check this box if you will support reader accounts for companies that don't have a Snowflake account.")
            else:
                reader = False

            # managed accounts optional
            if form_type == 'Provider':
                managed_accounts = False
            else:
                managed_accounts = st.checkbox("**Check this box if you will support Managed Accounts for companies that don’t have a Snowflake account.**  Selecting this option will add language that describes a Managed Account and invites the provider to contact your organization to request a Managed Account.")

            submit_button = st.form_submit_button('Submit')

        # Capture inputs
        # When button is clicked:
        # Check for errors
        # Check for optional fields set
        # Generate the file with required fields and optional fields
        if submit_button:
            # Validate inputs when button is clicked
            if name == '':
                return st.error(f"File not generated. Required field **{name_field_name}** is not set.")
            elif not region:
                return st.error(f"File not generated. Required field **{region_field_name}** is not set.")

            if spn_referral_link == '':
                spn_referral_link = '<a href="https://signup.snowflake.com/">signup.snowflake.com</a>'
            else:
                spn_referral_link = f'<a href="{spn_referral_link}">{spn_referral_link}</a>'

            # This won't render them in list order, instead 
            # in block rendering, and it's hard to read
            write_html(name, region, spn_referral_link, steps, reader)

            f = open("snowflake_data_sharing.html", "r")

            st.download_button(label="Download HTML file", data=f, file_name="snowflake_data_sharing.html")
            st.write("Once the download is complete, open the HTML file and save the page as a PDF with the file name of your choice. You can then send the PDF to your customer.")

if __name__ == "__main__":
    main()
