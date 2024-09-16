import streamlit as st
import streamlit.components.v1 as components

# Define the HTML content (your complete CV)
st.markdown(
    """
    <style>
       
        .st-emotion-cache-jmw8un {
            background-color: rgb(0, 107, 184);
        }
        .st-emotion-cache-4zpzjl{
            background-color: rgb(255, 202, 75);
        }
        [data-testid="stToolbar"].st-emotion-cache-15ecox0.ezrtsby0 {
            display: none;
        }
        [data-testid="stChatMessageContent"] p{
        font-family: 'Arial', sans-serif;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ankita Bhivgade CV</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Roboto', sans-serif;
            background-color: #f8f9fa;
            margin: 0;
            padding: 0;
            color: #333;
            line-height: 1.6;
        }
        .container {
            max-width: 900px;
            margin: 40px auto;
            padding: 40px;
            background-color: #fff;
            box-shadow: 0 0 30px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
        }
        .header {
            text-align: center;
            margin-bottom: 40px;
        }
        .header h1 {
            font-size: 36px;
            color: #2c3e50;
            margin-bottom: 10px;
        }
        .header p {
            font-size: 18px;
            color: #7f8c8d;
        }
        h2 {
            color: #3498db;
            font-size: 24px;
            border-bottom: 2px solid #3498db;
            padding-bottom: 10px;
            margin-top: 40px;
            margin-bottom: 20px;
        }
        h3 {
            color: #2c3e50;
            font-size: 20px;
            margin-top: 30px;
            margin-bottom: 15px;
        }
        ul {
            padding-left: 20px;
        }
        ul li {
            margin-bottom: 10px;
        }
        .skills-section, .languages-section {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
        }
        .skills-section ul, .languages-section ul {
            flex-basis: 48%;
        }
        .contact-info {
            margin-top: 40px;
            text-align: center;
            color: #7f8c8d;
        }
        @media (max-width: 768px) {
            .container {
                padding: 20px;
            }
            .skills-section ul, .languages-section ul {
                flex-basis: 100%;
            }
        }
    </style>
</head>
<body>

<div class="container">
    <div class="header">
        <h1>Ankita Bhivgade</h1>
        <p>Budapest, Hungary | +36-202765479 | anki19b@gmail.com</p>
    </div>

    <h2>Professional Summary</h2>
    <p>Results-driven Manager with over 7 years of comprehensive experience in operations, financial management, and team leadership within diverse sectors. Highly skilled in enhancing operational efficiency, directing high-performing teams, and optimizing profitability in retail environments. Demonstrated proficiency in store operations, sales strategy development, P&L management, inventory control, and customer satisfaction. Committed to leveraging expertise to achieve exceptional business outcomes and support organizational growth in challenging roles.</p>

    <h2>Professional Experience</h2>

    <h3>Manager, Reliance Retail (April 2023 – June 2024)</h3>
    <ul>
        <li>Led channel partner and distributor relationships to drive Zivame brand growth.</li>
        <li>Collaborated with planning, merchandising, and marketing teams for effective sales strategies.</li>
        <li>Recruited, trained, and led a high-performing sales team.</li>
        <li>Managed P&L, ensuring revenue targets were consistently met or surpassed.</li>
        <li>Spearheaded retail expansion by launching new stores and expanding into new territories.</li>
        <li>Enhanced customer satisfaction and retention through innovative product offerings and seamless experiences.</li>
        <li>Ensured operational efficiency by managing daily store activities, inventory levels, and financial aspects.</li>
        <li>Analyzed performance data to propose strategies for market growth and operational efficiency.</li>
        <li>Developed and executed business strategies to increase store traffic, optimize profitability, and meet sales goals.</li>
        <li>Implemented security measures and conducted audits to minimize shrinkage.</li>
        <li>Established and maintained a successful work culture. Recruited, retained, and developed a star team.</li>
    </ul>

    <h3>Lead Operations, Walmart Retail (April 2021 – April 2023)</h3>
    <ul>
        <li>Led daily store operations, ensuring efficient workflow, staff scheduling, and adherence to Walmart standards.</li>
        <li>Oversaw daily order fulfillment activities, including order processing, picking, packing, and shipping preparation.</li>
        <li>Worked alongside a 3PL and utilized their WMS software to optimize warehouse and fulfillment operations.</li>
        <li>Optimized procurement of inventory by improving vendor relationships, performance, and lead times.</li>
        <li>Managed a dynamic team of production supervisors, full-time and part-time warehouse staff, and other direct reports.</li>
        <li>Maintained positive and mutually beneficial relationships with vendors, suppliers, manufacturers, and 3PL vendor.</li>
        <li>Reported weekly on multiple fulfillment and performance KPIs.</li>
        <li>Provided data-backed and actionable updates to senior management to improve order fulfillment SLAs and vendor performance.</li>
        <li>Handled customer complaints and issues, ensuring timely and satisfactory resolutions to maintain customer loyalty.</li>
        <li>Coordinated with the marketing department to execute in-store promotions, seasonal displays, and events.</li>
        <li>Prepared and analyzed business reports to identify operational improvements and enhance overall store performance.</li>
    </ul>

    <h3>Department Manager, Reliance Retail Ltd (October 2019 – April 2021)</h3>
    <ul>
        <li>Managed P&L for the department, focusing on increasing profitability through effective cost control and margin improvement.</li>
        <li>Ensured accurate pricing and promotional displays, driving customer engagement and sales.</li>
        <li>Led inventory management efforts, minimizing shrinkage and maintaining optimal stock levels.</li>
        <li>Implemented and enforced SOPs, ensuring 100% compliance and operational efficiency.</li>
        <li>Trained and mentored team members, improving productivity and fostering talent development within the department.</li>
        <li>Analyzed sales data to drive business strategies, enhancing department performance and customer satisfaction.</li>
        <li>Managed vendor relationships to secure quality products at competitive prices, contributing to department profitability.</li>
        <li>Conducted regular performance reviews and implemented improvement plans to boost team effectiveness and customer service.</li>
    </ul>

    <h3>Assistant Store Manager, Easy Day (Future Group) (January 2019 – October 2019)</h3>
    <ul>
        <li>Assisted in managing daily store operations, including staff scheduling, inventory management, task delegation, and ensuring adherence to store policies.</li>
        <li>Maintained high visual merchandising standards, regularly updating displays to enhance customer experience and drive sales.</li>
        <li>Played a key role in achieving sales targets and improving store margins through effective planning and execution of promotions.</li>
        <li>Recruited, trained, and supervised store staff, fostering a positive work environment and ensuring high performance.</li>
        <li>Ensured compliance with SOPs, hygiene standards, and safety protocols to maintain a well-organized and secure store environment.</li>
        <li>Developed systems to control pilferage and minimize shrinkage, contributing to improved store profitability.</li>
        <li>Handled customer complaints professionally, resolving issues promptly to maintain high levels of customer satisfaction.</li>
        <li>Collaborated with the Store Manager on marketing campaigns and promotional activities to boost foot traffic and sales.</li>
    </ul>

    <h3>Account Receivables Executive, Ascent Business Solutions (October 2014 – August 2016)</h3>
    <ul>
        <li>Handled medical claims billing, ensured accurate payment processing, and maintained detailed records.</li>
        <li>Processed and uploaded claims and statements to a billing software, ensuring timely and accurate submission to insurance companies.</li>
        <li>Posted received payments into the system and generated weekly cash collection reports for management review.</li>
        <li>Resolved billing discrepancies and customer inquiries, collaborating with sales and customer service teams to address issues.</li>
        <li>Streamlined accounts receivable processes through automation tools, improving departmental efficiency and accuracy.</li>
        <li>Performed full cycle of accounts receivable past due balances, handling research, analysis, and account reconciliations.</li>
    </ul>

    <h3>Acquisition Manager, IndusInd Bank (September 2013 – September 2014)</h3>
    <ul>
        <li>Acquired new high-net-worth clients and generated referrals from existing customers to meet and exceed acquisition targets.</li>
        <li>Developed and executed strategies for selling financial products and services to both B2B and B2C clients.</li>
        <li>Cross-sold banking and insurance products, providing comprehensive solutions to enhance customer relationships and revenue.</li>
        <li>Managed risk and internal controls, adhering to regulatory and compliance requirements to ensure smooth operations.</li>
        <li>Built and maintained strong client relationships, delivering tailored financial solutions and exceptional service.</li>
        <li>Achieved daily, weekly, and monthly acquisition targets through a focus on customer needs and efficient sales execution.</li>
    </ul>

    <h2>Education</h2>
    <ul>
        <li>Master of Business Administration - Operations and Finance Management, Nagpur University, India (2019)</li>
        <li>Bachelor of Engineering - Electronics, Nagpur University, India (2013)</li>
    </ul>

    <h2>Certifications</h2>
    <ul>
        <li>Project Management Foundations by PMI</li>
        <li>Lean Six Sigma Yellow Belt</li>
        <li>CDAC - Diploma in Advanced Computing</li>
    </ul>

    <h2>Technical Skills</h2>
    <p>SAP ERP, SAP S/4HANA Cloud, SAP SuccessFactors, Microsoft Power BI, WMS, POS systems, MS Office Suite</p>

    <h2>Other Skills</h2>
    <div class="skills-section">
        <ul>
            <li>Financial Reporting</li>
            <li>Budget Administration</li>
            <li>Sales Strategies</li>
            <li>Vendor Management</li>
            <li>Project Management</li>
            <li>Process Improvement</li>
        </ul>
    </div>

    <h2>Languages</h2>
    <div class="languages-section">
        <ul>
            <li>Hindi: Native</li>
            <li>English: Fluent</li>
            <li>German: A1</li>
        </ul>
    </div>

    <div class="contact-info">
        <p>Budapest, Hungary | +36-202765479 | anki19b@gmail.com</p>
    </div>
</div>

</body>
</html>
"""

# Streamlit app
def main():
    st.set_page_config(page_title="Ankita Bhivgade CV", layout="wide")
    
    st.title("Ankita Bhivgade's CV")
    
    # Render the HTML content
    components.html(html_content, height=800, scrolling=True)

if __name__ == "__main__":
    main()
