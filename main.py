base = '''<html>
  <head>
		<title>How to use Snowflake to share data</title>
		<style type="text/css">
			@page {
				size: letter;
				margin: 5in;
			}
			body {
				font-family: sans-serif;
				margin: 4% 22%;
			}
			p {
				line-height: 1.3em;
			}
			p.legal {
				font-size: small;
			}
			img.header {
				height: 62px;
				width: auto;
			}
			img.snowflake {
				height: 20px;
				width: 20px;
			}
			img.step {
				height: 400px;
				width: auto;
			}
			h4 {
				color: #29b5e8;
			}
			h4.end {
				color: black;
			}
			a.end {
				color: #29b5e8;
			}
            li {
				margin-bottom: 10px;
			}
		</style>
	</head>
	<body>
		<img src="https://raw.githubusercontent.com/Snowflake-Labs/sf-samples/main/samples/img/image3.jpg" class="header"/>
		<h1>How to use Snowflake to share data</h1>
		<p>
		  ProviderName would like to share data with you via Snowflake to support your partnership and joint goals. This guide provides information about how to connect with ProviderName.
		</p>
		<p>
			Have Snowflake-specific questions about data sharing and Snowflake account creation? If you're an existing Snowflake customer, contact your Snowflake account team for help; otherwise, please <a href="https://www.snowflake.com/marketplace-contact-us" target="_blank">click here</a>. 
		</p>
		<h3><span><img src="https://raw.githubusercontent.com/Snowflake-Labs/sf-samples/main/samples/img/image1.png" class="snowflake"/></span> What is Snowflake?</h3>
		<p>
			Snowflake's Data Cloud is a global network where thousands of organizations mobilize data with near-unlimited scale, concurrency and performance. Snowflake provides organizations with a unified view of data so they can easily discover and securely share governed data, power data applications and execute diverse AI/ML and analytic workloads. All of this is delivered in a single data experience that spans multiple clouds and geographies.

		</p>
		<h3><img src="https://raw.githubusercontent.com/Snowflake-Labs/sf-samples/main/samples/img/image1.png" class="snowflake"/> Why trust Snowflake?</h3>
		<p>
			Security is a core element of the Snowflake platform and the Data Cloud. Layers of network security, identity and access management and end-to-end data encryption protect the data you load and use in Snowflake, helping to keep your data secure so you can spend more time analyzing it. For more details about our approach to security, including levels of compliance and certifications, please visit the <a href="https://www.snowflake.com/product/security-and-trust-center/" target="_blank">Snowflake Security and Trust Center</a>.
		</p>
		<h3><img src="https://raw.githubusercontent.com/Snowflake-Labs/sf-samples/main/samples/img/image1.png" class="snowflake"/> 4 reasons to use Snowflake for data sharing</h3>
		<ul>
			<li><strong>It's easy. </strong>Connect in just a few clicks and start receiving data. With cross-cloud auto-fulfillment, data is available across clouds and regions when and where you need it. </li>
			<li><strong>There's no need to move data.  </strong>Snowflake allows you to share data without transferring it. No need for ETL, FTP or moving data between environments. </li>
			<li><strong>Robust data governance. </strong>You control access to your data in a centralized, flexible way. Share data with one other account, a group of accounts or to any company in the Data Cloud via Snowflake Marketplace.*</li>
			<li><strong>Data is ready to use upon delivery. </strong>Snowflake delivers direct access to live, ready-to-query data. Perform fewer data transformations because the shared data stays in Snowflake, and easily join shared data sets with your own data.
			</li>
		</ul>
		<h3><img src="https://raw.githubusercontent.com/Snowflake-Labs/sf-samples/main/samples/img/image1.png" class="snowflake"/> How does Snowflake Secure Data Sharing work?</h3>
		<p>
			ProviderName creates a share of a database in their Snowflake account and grants access to specific objects (tables, views and functions) in the database. You, as the consumer, will then see a read-only database in your Snowflake account. You can configure access to this database using standard role-based access control (RBAC).
		</p>
		<p>
			For more specific details, see our <a href="https://docs.snowflake.com/en/user-guide/data-sharing-intro" target="_blank">Introduction to Snowflake Secure Data Sharing doc</a>.
		</p>
		<h3><img src="https://raw.githubusercontent.com/Snowflake-Labs/sf-samples/main/samples/img/image1.png" class="snowflake"/> Terms and definitions</h3>
		<p>
			Collaboration depends on a shared, consistent understanding of common words and phrases so everyone can communicate clearly. Here are definitions of several terms that appear in this guide:
		</p>
		<ul>
			<li><strong>Provider: </strong>The account that shares data</li>
			<li><strong>Consumer: </strong>The account that receives data</li>
			<li><strong>Share: </strong>A named Snowflake object that encapsulates all of the information required to share a database</li>
			<li><strong>Direct share: </strong> A way to directly share specific database options (a share) to another account in the same region</li>
			<li><strong>Listing: </strong>A way to offer a share plus metadata as a data product*</li>
			<li><strong>Data Product: </strong>A reusable “building block” that delivers data, data services, app code or data insights for a specific purpose</li>
		</ul>
		<h3><img src="https://raw.githubusercontent.com/Snowflake-Labs/sf-samples/main/samples/img/image1.png" class="snowflake"/> How to receive data from ProviderName on Snowflake</h3>
		<h4>If you are new to Snowflake</h3>
		<p>
			Getting started with Snowflake is easy, and it's a low-risk, no-commitment process.
		</p>
		<ul>
			<li>You can begin with a free trial account that does not require a form of payment to set up</li>
			<li>At the end of your trial, your trial account converts into an on-demand account where you only pay in arrears for the storage and compute resources you actually use; scale up and down as your business needs change</li>
			<li>Your on-demand account will never expire and you will not be forced to make a long-term financial commitment</li>
		</ul>
		<p>To get a free Snowflake trial account, visit SPN_ReferralLink.</p>
		<p><strong>NOTE:</strong> During the sign-up process, you will choose the cloud region for your Snowflake instance. If you have no specific preference, we recommend you save time and costs by using the same cloud region as ProviderName: ProviderRegion.</p>
		<h4>Once your account is set up OR if you are an existing Snowflake customer</h3>
		<p>
			ProviderName will need your Snowflake account identifier to share into your account. To find your Snowflake account identifier, follow these steps:
		</p>
		<ol>
			<li>Open the account selector and review the list of accounts.</li>
            <br />
			<img src="https://raw.githubusercontent.com/Snowflake-Labs/sf-samples/main/samples/img/image2.png" class="step"/>
			<br />
			<br />
			<br />
			<li>Locate the account you want to use.</li>
			<br />
			<li>Hover over the account to view additional details and select the copy icon to copy the account identifier in the format &lt;orgname&gt;.&lt;account_name&gt; to your clipboard.</li>
			<br />
			<img src="https://raw.githubusercontent.com/Snowflake-Labs/sf-samples/main/samples/img/image5.png" class="step"/>
		</ol>
		<br />
		<p>
			Once you have your account identifier, you'll need to provide it to ProviderName.
		</p>'''

shares='''<p>
			To view the ProviderName shares that are available to consume in your Snowflake account in the Snowsight UI, select <strong>Data &gt;&gt; Private Sharing</strong>, then select <strong>Shared With You</strong>. You will see both privately shared listings and direct shares. 
		</p>
		<p>
			For more details, including how to use the Snowflake Classic Console or SQL to view available shares, please check out our <a href="https://docs.snowflake.com/en/user-guide/data-share-consumers#viewing-available-shares" target="_blank">"Consuming Shared Data" doc</a>. 
		</p>'''

reader='''<h4>If you do not have a Snowflake account and do not want to set one up, ProviderName can host a Snowflake Reader Account for you</h3>
		<p>A Snowflake Reader Account is a quick, cost-effective way to share data with a non-Snowflake customer. The Reader Account belongs to the data provider and can only consume data from the provider that created it. Users in a Reader Account can query the data shared with the account, but cannot perform any write operations, such as ingesting new data into the account or storing results of queries run on the shared data (a full Snowflake account is required for those capabilities).</p>
		<p>To request a Reader Account, please contact ProviderName.</p>'''

        
end='''<h4 class="end"><img src="https://raw.githubusercontent.com/Snowflake-Labs/sf-samples/main/samples/img/image1.png" class="snowflake"/> Learn more about Snowflake Collaboration and Secure Data Sharing at <a href="https://www.snowflake.com/en/data-cloud/workloads/collaboration/" target="_blank" class="end">snowflake.com/en/data-cloud/workloads/collaboration</a></h3>
		<p class="legal">
        * Use of Snowflake Marketplace is subject to the Snowflake Provider and Consumer Terms of Service, which is separate from the Snowflake Terms of Service.
        </p> 
        <p class="legal">
			© 2024 Snowflake Inc. All rights reserved. Snowflake, the Snowflake logo, and all other Snowflake product, feature and service names mentioned herein are registered trademarks or trademarks of Snowflake Inc. in the United States and other countries. All other brand names or logos mentioned or used herein are for identification purposes only and may be the trademarks of their respective holder(s). Snowflake may not be associated with, or be sponsored or endorsed by, any such holder(s). 
		</p>
	</body>
</html>'''
