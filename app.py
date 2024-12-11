from dash import dcc, html
import dash_bootstrap_components as dbc
import dash
import file.inflation_healthcare as inflation_healthcare


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

##Descriptions
EXPLAINER = """Most people live in a delicate balance between income, saving for retirement, 
    if any, and spending for basic services such as food, clothing, housing, utilities, and medical care. 
    Inflation, as it refers to prices that we all pay for the basics of living, catches the attention of 
    everyone except for the wealthy 1% or 2%. Persistent price inflation above 2% to 3% can 
    cause people to change their standard of living in their choices of food, clothing, medical care, 
    and housing affordability. The goal is to explore the relationship between the inflation rate and 
    the healthcare costs published by the US Bureau of Labor Statistics."""



app.layout = dbc.Container(
    [
        html.H1("Inflation and Healthcare Costs"),
        html.H3(dcc.Markdown("By: [Annie He](https://www.anniezhe.com)")),
        dcc.Markdown(EXPLAINER),
        dcc.Tabs(
            [
                dcc.Tab(
                    label="Methods",
                    children=[
                        html.P(
                            dcc.Markdown(
                                "The following data from the Bureau of Labor Statistics (BLS) will be used to perform basic analysis on US inflation and healthcare costs. All data collection procedures for the list below are performed by the BLS. For each dataset, all available years will be reviewed to identify any significant differences. Research on each difference that is identified will use past news reports, government, and universities staff's work for sources. **Please note that this dashboard website will have all data on or before October 2024.**"
                            )
                        ),
                        html.Ul(
                            id="BLS-data",
                            children=[
                                html.Li(
                                    dcc.Markdown(
                                        "**[Civilian Labor Force Participation Rate - seasonally adjusted](https://data.bls.gov/dataViewer/view/timeseries/LNS11300000)**. Percentage of people who are in the labor force regardless of their employment status according to the Current Population Survey, which is a collaboration between the BLS and the Census Bureau. The first piece of data from the Current Population Survey was available in 1948. More info can be found from the [Census Bureau's History of the Current Population Survey](https://www.census.gov/programs-surveys/cps/about/history-of-the-cps.html) and [BLS's How the Government Measures Unemployment](https://www.bls.gov/cps/cps_htgm.htm)."
                                    )
                                ),
                                html.Li(
                                    dcc.Markdown(
                                        """**[Civilian Unemployment Rate - seasonally adjusted](https://data.bls.gov/dataViewer/view/timeseries/LNS14000000)**. Percentage of people in the labor force who are unemployed and are looking for a job according to the Current Population Survey, which is a collaboration between the BLS and the Census Bureau. The first piece of data from the Current Population Survey was available in 1948. More info can be found from the [Census Bureau's History of the Current Population Survey](https://www.census.gov/programs-surveys/cps/about/history-of-the-cps.html) and [BLS's How the Government Measures Unemployment](https://www.bls.gov/cps/cps_htgm.htm)."""
                                    )
                                ),
                                html.Li(
                                    dcc.Markdown(
                                        "**[Consumer Price Index for All Urban Consumers (CPI-U) - not seasonally adjusted](https://data.bls.gov/dataViewer/view/timeseries/CUUR0000SA0)**. Inflation rate for a BLS specified basket of goods and services according to the Consumer Price Index. The first piece of this data was available in 1913. 12-month percent change (not net change) is used to see price change annually. More information can be found from the important notes section below."
                                    )
                                ),
                                html.Li(
                                    dcc.Markdown(
                                        "**[Medical Care from Consumer Price Index Survey - not seasonally adjusted](https://data.bls.gov/dataViewer/view/timeseries/CUUR0000SAM)**. Overall price behavior for consumer out-of-pocket spending on all medical goods and services. 12-month percent change (not net change) is used to see price change annually. Please note that the consumer out-of-pocket expenditure components are smaller than what other national health expenditures are reporting. Other national health expenditures include reimbursements that are fully paid for by public sources and employers. Prior to 1979, data collection procedures were not conducted on a continuous monthly basis as per old collection techniques, so some 12-month percent changes were not available or N/As. More information can be found from the [BLS's Measuring Price Change in the CPI: Medical care](https://www.bls.gov/cpi/factsheets/medical-care.htm), [BLS's First Hundred Years of the Consumer Price Index](https://www.bls.gov/opub/mlr/2014/article/the-first-hundred-years-of-the-consumer-price-index.htm), and [BLS's Chapter 16 Consumer Expenditures and Income](https://www.bls.gov/opub/hom/pdf/cex-20110915.pdf)."
                                    )
                                ),
                                html.Li(
                                    dcc.Markdown(
                                        """**[Employment-Population Ratio from the Current Population Survey - seasonally adjusted](https://data.bls.gov/dataViewer/view/timeseries/LNS12300000)**. Percentage of people who are currently working. More information regarding this definition can be found from the [BLS's "Labor Force Statistics Concepts and Definitions"](https://www.bls.gov/cps/definitions.htm)"""
                                    )
                                ),
                            ],
                        ),
                        html.H5(
                            "Important note about all of these data from the BLS website"
                        ),
                        html.Ul(
                            id="important-note",
                            children=[
                                html.Li(
                                    dcc.Markdown("""
                    The "Consumer Price Index for All Urban Consumers (CPI-U) - not seasonally adjusted" **with 12-month percent change (not net change) enabled** should be pulled and used if the purpose is to find out the annual inflation rate. When news reporters 
                                     specify the inflation rate, the figure comes from this dataset. For more information, see [Overview of BLS Statistics on Inflation and Prices](https://www.bls.gov/bls/inflation.htm), [BLS's "About the CPI Inflation Calculator"](https://www.bls.gov/data/inflation_calculator.htm), [BLS's Consumer Price Index History](https://www.bls.gov/opub/hom/cpi/history.htm), and [BLS's First Hundred Years of the Consumer Price Index](https://www.bls.gov/opub/mlr/2014/article/the-first-hundred-years-of-the-consumer-price-index.htm).
                """)
                                ),
                                html.Li(
                                    dcc.Markdown("""The size of the labor force, employment, and unemployment undergo 
                                     fluctuations due to seasonal events including changes in weather, 
                                     harvests, major holidays, and school schedules. 
                                     Because these seasonal events follow a more or 
                                     less regular pattern each year, their influence on 
                                     statistical trends can be eliminated by seasonally 
                                     adjusting the statistics from month to month. The seasonal adjustments are
                                     done by the Bureau of Labor Statistics employees. More information can be found from the [BLS's "What is Seasonal Adjustment?" article](https://www.bls.gov/cps/seasfaq.htm).
                                     """)
                                ),
                            ],
                        ),
                    ],
                ),
                dcc.Tab(
                    label="Report",
                    children=[
                        dcc.Graph(figure=inflation_healthcare.fig1, responsive=True),
                        dcc.Graph(figure=inflation_healthcare.fig6, responsive=True),
                        dcc.Graph(figure=inflation_healthcare.fig7, responsive=True),
                        html.H5("Below is a list of important events related to inflation and healthcare costs to better understand people's financial situation related to healthcare and the efforts being made to support them."),
                        dbc.Accordion(
        [
            dbc.AccordionItem(
                dcc.Markdown('''
* The year 1929 marked the beginning of the Great Depression era. 
The Baylor Plan was established to help people afford hospital care. It was the country’s very first prepaid hospital insurance plan.      
* Unemployment rate reached 22.9% in 1932 and 12.5% in 1938. Deflation reached 9.8% also in 1932. Hospitals provided free services for people who lost their income but were struggling to financially support its operations and its staff. Drastic measures were taken to continue providing free services to unemployed people. 
* The Bureau of Labor Statistics (BLS) worked with four other federal agencies to collect data on the nation’s well-being from 1935 to 1936. The first piece of BLS data for medical care cost was available in 1936.
* In 1939, in an attempt to strengthen the Social Security Act, which was passed in 1935, President Franklin Roosevelt revised it so that not only workers’ spouses and children will receive benefits, but also people could receive their benefits as promised earlier.
* The Great Depression ended when World War II began. The Roosevelt’s administration ended on April 12, 1945, when the President died from a cerebral hemorrhage. Roosevelt’s Vice President, Harry S. Truman, took over as the new President.

                             
Source(s): [BLS's Chapter 16 Consumer Expenditures and Income](https://www.bls.gov/opub/hom/pdf/cex-20110915.pdf),
[BLS's First Hundred Years of the Consumer Price Index](https://www.bls.gov/opub/mlr/2014/article/the-first-hundred-years-of-the-consumer-price-index.htm),
[Life and Death During the Great Depression](https://www.pnas.org/doi/epdf/10.1073/pnas.0904491106),
[Medical Care During the Depression](https://pmc.ncbi.nlm.nih.gov/articles/PMC2690273/),
[Why Social Security Was the Cornerstone of FDR’s New Deal]( https://www.history.com/news/social-security-history-fdr-new-deal),
[Franklin D. Roosevelt](https://www.whitehouse.gov/about-the-white-house/presidents/franklin-d-roosevelt/),
[Baylor Scott & White’s “A Moment in History”](https://blog.bswhealth.med/a-moment-in-history/#:~:text=The%20%E2%80%9CBaylor%20Plan%E2%80%9D%20was%20established%20in%201929%20by,the%20United%20States%20and%20predecessor%20of%20Blue%20Cross),
[HISTORY.com's World War II](https://www.history.com/topics/world-war-ii/world-war-ii-history)  
'''), title="1929 to 1940: Great Depression"
            ),
            dbc.AccordionItem(
                dcc.Markdown('''
* The idea to establish a national healthcare program was born from President Truman’s experience when he was enlisted in the army to fight in World War I. Truman noticed that many men were deemed unfit for army enlistment. The archivist at the Harry S. Truman Presidential Library and Museum said, “He `[President Truman]` felt it was a reflection of inadequate health care for parts of the population”.
* When Truman became President, he expressed an urgent need to establish a universal health care system where all medical costs were paid from a payroll tax. That idea was not received well, because it was thought to be too expensive. The federal individual income tax rate for 1946 and 1947 was 20% if a person made anywhere more than $0 but less than $2000. 22% if a person made anywhere more than $2000 but less than $4000. 26% if a person made anywhere more than $4000 but less than $6000.
* In 1947, which was two years after the World War II ended, McCarthyism took hold of the country with its claims that there were perpetrators who desired to replace democracy with communism. Some people thought that the idea of universal healthcare aligned with communist values.
* Although the universal healthcare bill died, the Hill Burton Act was passed in 1946 to provide federal funds to build hospitals, which was why medical costs spiked between 1946 and 1947. 
* In 1950, BLS collected data only from urban consumers. In 1953, Truman’s administration ended with little success on its national healthcare initiatives. From 1960 to 1961, BLS collected another set of data on the nation’s wellbeing, which was why some pieces of data were missing in the medical care cost graph.
* In 1965, President Lyndon B. Johnson signed Medicare and Medicaid Act into law.
                             

Source(s): [Harry S. Truman](https://www.whitehouse.gov/about-the-white-house/presidents/harry-s-truman/),
[The Challenge of National Healthcare](https://www.trumanlibrary.gov/education/presidential-inquiries/challenge-national-healthcare),
[When Harry Truman Pushed for Universal Health Care](https://www.history.com/news/harry-truman-universal-health-care),
[Red Scare]( https://www.history.com/topics/cold-war/red-scare),
[Federal Individual Income Tax Rates History]( https://files.taxfoundation.org/legacy/docs/fed_individual_rate_history_nominal.pdf),
[BLS's Chapter 16 Consumer Expenditures and Income](https://www.bls.gov/opub/hom/pdf/cex-20110915.pdf)
'''), title="1945 to 1965: Struggle to Establish National Healthcare"
            ),
            dbc.AccordionItem(
                dcc.Markdown('''
* The Medicare and Medicaid programs became a major reason why there was an acceleration for the healthcare price rate. These programs together were the biggest purchasers for healthcare services.
* The combination of the following was what brought the country into the Great Inflation period: 1) many other national initiatives along with Medicare and Medicaid programs, 2) being financially strained by the Vietnam War, 3) inability to support US dollar with gold as per global monetary agreement from post-World War II, and 4) repeated spikes in oil prices thanks to OPEC, a Saudi Arabia-led cartel. 
* There were attempts to lower health care costs like passing the Health Maintenance Organization Act of 1973 to reduce hospital admissions and lengths of stay. 
* The Nixon administration ended the gold standard in 1971 where the US dollar cannot be converted to gold anymore. The Nixon administration also used wage and price controls 3 times between 1971 and 1974 to end inflation; none of these attempts worked. 
* The Ford administration developed the Whip Inflation Now (WIN) program, which also didn’t work.
* The BLS started collecting data on the nation’s well being annually in 1979.
* Chairman Paul Volcker increased interest rates and decreased the rate of money supply. Although Chairman Volcker’s strategy resulted with 2 recessions (one in 1980 and another in 1981), the inflation rate gradually decreased to under 5%. His strategy was necessary in order to bring down the country’s unacceptably high inflation rate.
                             

Source(s): [BLS's Chapter 16 Consumer Expenditures and Income]( https://www.bls.gov/opub/hom/pdf/cex-20110915.pdf),
[Federal Reserve History's Essay on The Great Inflation](https://www.federalreservehistory.org/essays/great-inflation#:~:text=The%20Great%20Inflation%20was%20the%20defining%20macroeconomic%20period,policies%20of%20the%20Fed%20and%20other%20central%20banks),
[The US Health Care Non-System, 1908-2008](https://journalofethics.ama-assn.org/article/us-health-care-non-system-1908-2008/2008-05)
'''), title="1965 to 1982: Great Inflation"
            ),
            dbc.AccordionItem(
                dcc.Markdown('''
* Since 1973, health maintenance organization plans became popular among patients and hospitals. 
* Later on, many other types of cost containment methods were introduced such as Prospective Payment Systems (PPS) for Medicare, preferred provider organizations (PPOs) also for managed care, and resource-based relative value scale (RBRVS) for physician services. 
* In the early 1990s, health care spending increased at a rapid pace because of expensive new medical technologies. The link to see a list of new medical technologies is [here](https://www.mddionline.com/new-technologies/30-years-30-devices-1979-the-1980s-the-1990s-the-2000s-older-technologies).
* Later on, many different types of cost containment methods were introduced such as Prospective Payment Systems (PPS) for Medicare, health maintenance organizations (HMOs) for managed care, preferred provider organizations (PPOs) also for managed care, and resource-based relative value scale (RBRVS) for physician services.
* Hospital inpatient admissions declined by roughly 15%, and occupancy rates nationwide fell from 76% to 63% between 1980 and 1995. Morbidity associated with smallpox and polio were completely eliminated in 1990s thanks to vaccine developments from 1950s and 1960s. 

                             
Source(s):
[The Changing Economics of Medical Technology](https://www.ncbi.nlm.nih.gov/books/NBK234316/),
[Health Care in the 1990s: Changes in Health Care Delivery Models for Survival]( https://www.jognn.org/article/S0884-2175(15)33446-8/fulltext),
[Achievements in Public Health, 1900-1999 Impact of Vaccines Universally Recommended for Children – United States, 1990-1998]( https://www.cdc.gov/mmwr/preview/mmwrhtml/00056803.htm)

'''), title="1980s and 1990s: Modernizing Healthcare"
            ),
            dbc.AccordionItem(
                dcc.Markdown('''
* After the Affordable Care Act (ACA) became a law in 2008, more people began to sign up for health insurance plans that were created thanks to ACA. Between 2013 and 2023, the uninsured rate for all ages fell from 14.4% to 7.7%.
* The rise of telemedicine, which began in the 1950s, where a “closed-circuit television link was established between the Nebraska Psychiatric Institute and Norfolk State Hospital for psychiatric consultations”, started to expand rapidly in the late 2010s. 
* mRNA vaccines made the headlines during COVID-19 pandemic as saviors. mRNA vaccines were successfully developed after spending time since 1990s on solving the biggest challenge. The biggest challenge was that the initial version of mRNA quickly got destroyed in the body before reaching to the cells that were responsible for protecting and defending the human body.
* On the flip side of the COVID-19 pandemic, hospital systems were overwhelmed due to sudden increase in hospital admissions. Prior to COVID-19, hospitals had already experienced strained capacity because of the rise of HMOs, doctor and nurse shortages,1997 Balanced Budget Act (BBA), and increasing cost for malpractice liability insurance.
* Inflation also occurred during the COVID 19 pandemic. It was caused by “volatility of energy prices, backlogs of work orders for goods and services” thanks to supply chain issues, and “price changes in the auto-related industries”. 
* Starting in March 2022, the Federal Reserve raised interest rates to combat inflation. In June 2022, inflation reached 9.1% thanks to Russia-Ukraine war and OPEC’s decision to cut back oil production in the early months of the COVID-19 pandemic. The Federal Reserve continued to raise interest rates until 2023.
* The reason why inflation was painful even though slowly moving towards the Federal Reserve's target inflation rate of 2% from 2023 to 2024 was because of the volatility in food and gasoline prices.
* In 2024, there was an increase in medical care cost because medical providers pushed for larger cost increases to cover wages and supplies as soon as their contracts with medical insurers ended. In addition, there was a significant increase in the use of specialty drugs for diabetes and weight loss.


Source(s):
[BLS's What caused the high inflation during the COVID-19 period?](https://www.bls.gov/opub/mlr/2023/beyond-bls/what-caused-the-high-inflation-during-the-covid-19-period.htm),
[Federal Reserve Board's Statement on Longer-Run Goals and Monetary Policy Strategy](https://www.federalreserve.gov/monetarypolicy/files/FOMC_LongerRunGoals_202008.pdf),
[The Transition from Excess Capacity to Strained Capacity in US Hospitals]( https://pmc.ncbi.nlm.nih.gov/articles/PMC2690165/),
[In Celebration of 10 Years of ACA Marketplaces, the Biden-Harris Administration Releases Historic Enrollment Data]( https://www.hhs.gov/about/news/2024/03/22/celebration-10-years-aca-marketplaces-biden-harris-administration-releases-historic-enrollment-data.html),
[The Transition from Excess Capacity to Strained Capacity in US Hospitals]( https://pmc.ncbi.nlm.nih.gov/articles/PMC2690165/),
[The Evolution of Telehealth: Where Have We Been and Where Are We Going]( https://www.ncbi.nlm.nih.gov/books/NBK207141/),
[The Long History of mRNA Vaccines]( https://publichealth.jhu.edu/2021/the-long-history-of-mrna-vaccines),
[Impact of Hospital Strain on Excess Deaths During the COVID-19 Pandemic – United States, July 2020 – July 2021](https://www.cdc.gov/mmwr/volumes/70/wr/mm7046a5.htm),
[What caused inflation to spike after 2020?]( https://www.bls.gov/opub/mlr/2023/beyond-bls/what-caused-inflation-to-spike-after-2020.htm),
[Federal Reserve raises US Interest Rates to Highest Levels in 22 Years]( https://www.ft.com/content/110bd237-cbf2-463d-b1b5-edcb98245851),
[Average US gas price hits $5 for first time]( https://www.cnn.com/2022/06/11/business/gas-prices-five-dollars-national-june/index.html),
[The Federal Reserve finally hits pause on raising interest rates]( https://www.npr.org/2023/06/17/1182941206/the-federal-reserve-finally-hits-pause-on-raising-interest-rates),
[Inflation dropped to 4% in May – but the ‘biggest risk’ is that core prices will remain sticky](https://www.cnbc.com/2023/06/13/inflation-rate-drops-but-sticky-inflation-persists.html),
[Health care costs at work set to rise steeply in 2024]( https://www.cnn.com/2023/10/31/politics/health-care-costs-job/index.html)
            
'''), title="2008 and Onwards: Affordable Care Act and the Evolution in Healthcare Services"
            ),
        ],
        start_collapsed=True,
    ),
                        dcc.Graph(figure=inflation_healthcare.fig9, responsive=True),
                        dcc.Graph(figure=inflation_healthcare.fig10, responsive=True),
                        dcc.Graph(figure=inflation_healthcare.fig11, responsive=True),
                        dcc.Graph(figure=inflation_healthcare.fig2, responsive=True),
                        dcc.Graph(figure=inflation_healthcare.fig3, responsive=True),
                        dcc.Graph(figure=inflation_healthcare.fig12, responsive=True),
                        dcc.Graph(figure=inflation_healthcare.fig13, responsive=True),
                        dcc.Graph(figure=inflation_healthcare.fig14, responsive=True),
                        dcc.Graph(figure=inflation_healthcare.fig4, responsive=True),
                        html.P(
                            dcc.Markdown(
                                "The unemployment rate shows the percentage of people in the labor force who are unemployed **and are actively looking for a job**."
                            )
                        ),
                        dcc.Graph(figure=inflation_healthcare.fig5, responsive=True),
                        html.P(
                            dcc.Markdown("""
The "Civilian Not in Labor Force" graph represents people who have decided to not be in the labor force for multitude of reasons, **which are completely different from the unemployment rate graph**.
""")
                        ),
                    ],
                ),
                dcc.Tab(
                    label="Demo",
                    children=[
                        html.P(
                            dcc.Markdown("""
To demonstrate what a $100 medical cost would look like from 1974 to 2024, the medical cost data from the same source as the "Report" section was used.
This time, "1-month % change" (not net change) was selected to see the percent change on every month. The formula being used to calculate the changes in dollars is cost(new) = cost(old) * (1 + (1-month % change/100)).
Below is the graph showing what the $100 cost from 1974 would look like as time goes on.
""")
                        ),
                        dcc.Graph(figure=inflation_healthcare.fig8, responsive=True),
                    ],
                ),
                dcc.Tab(
                    label="Conclusion",
                    children=[
                        html.P(
                            dcc.Markdown("""
The "Report" and "Demo" tabs point to a continuous need to support the country's healthcare system and to improve the system. Recent records of the country's income were reviewed. Below are additional findings.
* In 2024, the US Bureau of Economic Analysis (BEA) reported $5.1 trillion in annual income for the federal government, but its current annual expenditure is about $7 trillion. Interest costs for borrowing are now a major budget item. More information can be found from the [BEA's Government Current Receipts and Expenditures](https://apps.bea.gov/iTable/?reqid=19&step=2&isuri=1&categories=survey&_gl=1*s3gg1p*_ga*MTYxOTk1NTUzNy4xNzMxMDAzMzAy*_ga_J4698JNNFT*MTczMzUwODI5OS4xMC4xLjE3MzM1MDg5NDcuNjAuMC4w#eyJhcHBpZCI6MTksInN0ZXBzIjpbMSwyLDNdLCJkYXRhIjpbWyJDYXRlZ29yaWVzIiwiU3VydmV5Il0sWyJOSVBBX1RhYmxlX0xpc3QiLCI4NiJdXX0=) and the [BEA's Federal Government Current Receipts and Expenditures](https://apps.bea.gov/iTable/?reqid=19&step=2&isuri=1&categories=survey&_gl=1*s3gg1p*_ga*MTYxOTk1NTUzNy4xNzMxMDAzMzAy*_ga_J4698JNNFT*MTczMzUwODI5OS4xMC4xLjE3MzM1MDg5NDcuNjAuMC4w#eyJhcHBpZCI6MTksInN0ZXBzIjpbMSwyLDNdLCJkYXRhIjpbWyJjYXRlZ29yaWVzIiwiU3VydmV5Il0sWyJOSVBBX1RhYmxlX0xpc3QiLCI4NyJdXX0=).
* From BEA's report, the tax on corporate income is noticeably low from the federal's perspective, which is about $483 billion for 2024. The overall (meaning from the federal, state, and local governments combined) corporate tax is $647 billion. More information can be found from the [BEA's Government Current Receipts and Expenditures](https://apps.bea.gov/iTable/?reqid=19&step=2&isuri=1&categories=survey&_gl=1*s3gg1p*_ga*MTYxOTk1NTUzNy4xNzMxMDAzMzAy*_ga_J4698JNNFT*MTczMzUwODI5OS4xMC4xLjE3MzM1MDg5NDcuNjAuMC4w#eyJhcHBpZCI6MTksInN0ZXBzIjpbMSwyLDNdLCJkYXRhIjpbWyJDYXRlZ29yaWVzIiwiU3VydmV5Il0sWyJOSVBBX1RhYmxlX0xpc3QiLCI4NiJdXX0=) and the [BEA's Federal Government Current Receipts and Expenditures](https://apps.bea.gov/iTable/?reqid=19&step=2&isuri=1&categories=survey&_gl=1*s3gg1p*_ga*MTYxOTk1NTUzNy4xNzMxMDAzMzAy*_ga_J4698JNNFT*MTczMzUwODI5OS4xMC4xLjE3MzM1MDg5NDcuNjAuMC4w#eyJhcHBpZCI6MTksInN0ZXBzIjpbMSwyLDNdLCJkYXRhIjpbWyJjYXRlZ29yaWVzIiwiU3VydmV5Il0sWyJOSVBBX1RhYmxlX0xpc3QiLCI4NyJdXX0=).
* The [US Treasury](https://fiscaldata.treasury.gov/americas-finance-guide/national-deficit/) currently reports $1.83 trillion in total deficit for FY2024, and it is continuing to rise.
* For FY 2023, the [IRS](https://www.irs.gov/statistics/soi-tax-stats-irs-data-book) reported $456 billion in taxes from business income whereas individual income was $2.5 trillion and others (employment, estate and gift, and excise taxes) reported $1.6 trillion.
* At the end of FY 2023, which is July 2023, US corporations reported a profit of $3.5 trillion dollars.
* One major reason why businesses pay low taxes is the list of all deductions on [Form 1120](https://www.irs.gov/pub/irs-pdf/f1120.pdf) and [business tax credits that any businesses can claim](https://www.irs.gov/credits-deductions/businesses). Any businesses can use all of them for each tax year as long as they fulfill all the requirements when filing a tax return. 
* IRS reported on [its website](https://www.irs.gov/newsroom/the-tax-gap) that roughly 87% of taxes were paid for tax years 2014-2016, which meant 13% of the taxes were still not paid. 
* IRS also reported on the existence of fake charities on [its website](https://www.irs.gov/newsroom/irs-dirty-dozen-list-warns-people-to-watch-out-for-tax-related-scams-involving-fake-charities-ghost-preparers-and-other-schemes). [Loeb & Loeb LLP](https://www.loeb.com/en/newsevents/news/2022/07/76-fake-charities-shared-a-mailbox-the-irs-approved-them-all), a law firm, pointed out flaws in the IRS's ability to detect signs of fraud, which was the struggle to distinguish sound-alike names from actual names.
* Charles Schwab reported in [its 2019 annual equity compensation survey](https://content.schwab.com/web/sps/sps_employee_study/) that 41% of millenials' net worth was made up of equity compensation. Forbes [reported](https://www.forbes.com/sites/lcarrel/2019/11/28/only-41-of-employees-receiving-stock-compensation-sold-any-study/) that the participants in equity compensation plans hold nearly $100,000 in vested stock, and the workers that Charles Schwab "surveyed had a significant amount of their wealth in their equity compensation plans".

                                         
The country needs at least $3 trillion more to cover all expenditures and some portions of the annual deficit. In order to continue supporting the country's healthcare system, food aid, etc., **there needs to be a review and a revision to the tax system** in order to better distribute resources to people who are badly affected by the inflation and cannot afford to cover healthcare on their own -- especially ones who are making less than the average of about $63,000 (median salary in 2023 is about $42,000) -- and to continue protect and look after this country. History dictates that the road to recovery from inflation is difficult but necessary. It's **strongly recommended** to vote for candidates who promise to push the country towards desired result in all elections (presidential, midterm, and local).
        
""")
                        )
                    ],
                ),
                dcc.Tab(
                    label="Questions & Answers",
                    children=[
                        html.Div(
                            dbc.Accordion(
                                [
                                    dbc.AccordionItem(
                                        [
                                            html.P(
                                                dcc.Markdown("""
Inflation occurs when the prices of many of the things we commonly buy increase over an extended period. 
                                                                Recent price increases that were termed inflationary were caused mostly by interference with the supply of products and manufacturing materials, mostly due to external events. Most recently, the event was the worldwide COVID pandemic and in the past, an artificial interference with oil supplies from the cartel led by Saudi Arabia named OPEC.
                                                                
                                                    
In the United States, the Federal Reserve Bank attempts to limit inflation and balance employment by adjusting the cost of borrowing money, also known as the interest rate, in order to maintain a stable economy with moderate growth rates in industry and services.
                                                                
                                                             
The Federal Reserve's Open Market Committee (FOMC) announced in 2020 that it believed that an inflation at the rate of about "2 percent, as measured by the annual change in the price index for personal consumption expenditures, is most consistent over the longer run with the Federal Reserve's statutory mandate". The FOMC's objective to have a 2 percent inflation rate was chosen, because they found, from analyzing the personal consumption expenditure data, that 2 percent would bring the country closer to achieving its goals of maximum employment and reasonably stable prices and wages.


**Important: please note that there's a difference between stable prices and affordable prices.** Stable prices in this case mean that there's only small inflation and no deflation. Even with a 2% inflation rate, if you want to be able to afford goods and services like food, housing, laundromat, clothing, etc., your wages need to catch up. That's why you hear discussions about increasing the minimum wage and why certain support programs such as Social Security are adjusted upwards to offset the inflation rate.                                                                
                                                                
Source(s): 
* [What is inflation by Federal Reserve Bank -- Cleveland branch](https://www.clevelandfed.org/center-for-inflation-research/inflation-101/what-is-inflation-start), [How does the government measure inflation by Brookings](https://www.brookings.edu/articles/how-does-the-government-measure-inflation/)
* [Federal Reserve's Statement on Longer-Run Goals and Moneotry Policy Strategy Q&A](https://www.federalreserve.gov/faqs/statement-on-longer-run-goals-monetary-policy-strategy-fomc.htm)
* [How does the Federal Reserve affect inflation and employment?](https://www.federalreserve.gov/faqs/money_12856.htm)
* [Oil Cartel Leader Says Demand Expected to Grow](https://www.bbc.com/news/business-66985654)
* [The Great Inflation: A Historical Overview and Lessons Learned from Federal Bank -- St. Louis branch](https://www.stlouisfed.org/publications/page-one-economics/2012/10/01/the-great-inflation-a-historical-overview-and-lessons-learned)
* [Energy History by Yale University](https://energyhistory.yale.edu/the-oil-shocks-of-the-1970s/)
* [Federal Reserve Board's Statement on Longer-Run Goals and Monetary Policy Strategy](https://www.federalreserve.gov/monetarypolicy/files/FOMC_LongerRunGoals_202008.pdf) 
""")
                                            ),
                                        ],
                                        title="What is inflation?",
                                    ),
                                    dbc.AccordionItem(
                                        [
                                            html.P(
                                                dcc.Markdown("""
Almost never. Put it simply, deflation is a continued decrease in the prices of many things. Decreasing prices leads to reduced purchases as consumers wait for further price reductions. After an extended period, it would lead to massive unemployment and reduced economic activity. That's why we're sticking to 2-percent inflation rate, which encourages employment and is perceived as price stability for essential consumer goods and services.
                                                               

Source(s): [Inflation, Disinflation, and Deflation by Federal Rserve Bank -- St. Louis branch](https://www.stlouisfed.org/open-vault/2023/august/explaining-inflation-disinflation-deflation)
                                                              """)
                                            ),
                                        ],
                                        title="Is the opposite of inflation ever good?",
                                    ),
                                    dbc.AccordionItem(
                                        [
                                            html.P(
                                                dcc.Markdown(
                                                    """
The stock market has almost nothing to do with inflation. The stock market is where companies and investors buy or sell a portion of the ownership in companies. Stocks are also known as equities. As an example, if I own 20% of NVIDIA's stocks, then 20% of NVIDIA corporation belongs to me. Wow, that would be a dream.


The value of a stock -- or stock price -- is determined by a combination of the company's assets, liabilities, earnings potential, growth prospects, etc., which would require analysts (financial analysts that specialize in stock market, not me) and investors to estimate the value of a company's stock. In short, stock market prices are set by a complicated mix of speculation, investor’s assessment of future profitability of companies based on current and anticipated sales, and the possibility of external events interfering with commerce. 


Stock prices are weakly associated with inflation mainly through the need for retired people to withdraw invested funds for their living expenses and through retirement funds set aside by working people throughout their career. If you are dependent on stocks for income, it can be a nightmare if the stocks that you've picked lose value.


**Important note: The stock market is not a measure of how well the US economy is doing.**


Source(s): [Understanding Stock Price and Value](https://www.investopedia.com/articles/stocks/08/stock-prices-fool.asp), [Stocks: What They Are, Main Types, and How They Differ From Bonds](https://www.investopedia.com/terms/s/stock.asp)
"""
                                                )
                                            ),
                                        ],
                                        title="What's the relationship between the stock market and the inflation?",
                                    ),
                                ],
                                flush=True,
                                start_collapsed=True,
                            )
                        )
                    ],
                ),
            ]
        ),
    ]
)

if __name__ == "__main__":
    app.run(debug=True)
