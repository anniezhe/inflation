from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
import dash
import file.inflation_healthcare as inflation_healthcare

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

server = app.server

##Descriptions
EXPLAINER = """Most people live in a delicate balance between income, saving for retirement, 
    if any, and spending for basic services such as food, clothing, housing, utilities, and medical care. 
    Inflation, as it refers to prices everyone pays for the basics of living, catches the attention of 
    everyone except for the wealthy 1% or 2%. Persistent price inflation above 2% to 3% can 
    cause people to change their standard of living in their choices of food, clothing, medical care, 
    and housing affordability. The goal is to explore the relationship between the inflation rate and 
    the healthcare cost published by the US Bureau of Labor Statistics."""

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([dbc.Container(
    
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
                                "The following data from the Bureau of Labor Statistics (BLS) will be used to perform basic analysis on the US inflation and healthcare costs. All data collection procedures for the list below are performed by the BLS. For each data, all available years will be reviewed to identify any significant differences. Research on each significance that is identified will use past news reports and government and universities staff's work for sources. **Please note that this dashboard will have all data on or before October 2024.**"
                            )
                        ),
                        html.Ul(
                            id="BLS-data",
                            children=[
                                html.Li(
                                    dcc.Markdown(
                                        "**[Civilian Labor Force Participation Rate - seasonally adjusted](https://data.bls.gov/dataViewer/view/timeseries/LNS11300000)**. Percentage of people who are actively working (employed) and/or looking for a job (unemployed) according to the Current Population Survey, which is a collaboration between the BLS and the Census Bureau. The first piece of data from the Current Population Survey was available in 1948. More info can be found from the [Census Bureau's History of the Current Population Survey](https://www.census.gov/programs-surveys/cps/about/history-of-the-cps.html) and [BLS's How the Government Measures Unemployment](https://www.bls.gov/cps/cps_htgm.htm)."
                                    )
                                ),
                                html.Li(
                                    dcc.Markdown(
                                        """**[Civilian Unemployment Rate - seasonally adjusted](https://data.bls.gov/dataViewer/view/timeseries/LNS14000000)**. Percentage of people in the labor force who are unemployed a job (unemployed) according to the Current Population Survey, which is a collaboration between the BLS and the Census Bureau. The first piece of data from the Current Population Survey was available in 1948. More info can be found from the [Census Bureau's History of the Current Population Survey](https://www.census.gov/programs-surveys/cps/about/history-of-the-cps.html) and [BLS's How the Government Measures Unemployment](https://www.bls.gov/cps/cps_htgm.htm)."""
                                    )
                                ),
                                html.Li(
                                    dcc.Markdown(
                                        "**[Consumer Price Index for All Urban Consumers (CPI-U) - not seasonally adjusted](https://data.bls.gov/dataViewer/view/timeseries/CUUR0000SA0)**. Inflation rate for all goods and services according to the Consumer Price Index. The first piece of this data was available in 1913. 12-month percent change (not net change) is used to see price change annually. More information can be found from the important notes section below."
                                    )
                                ),
                                html.Li(
                                    dcc.Markdown(
                                        "**[Medical Care from Consumer Price Index Survey - not seasonally adjusted](https://data.bls.gov/dataViewer/view/timeseries/CUUR0000SAM)**. Overall price behavior for consumer out-of-pocket spending on all medical goods and services. 12-month percent change (not net change) is used to see price change annually. Please note that the consumer out-of-pocket expenditure component are smaller than what other national health expenditures are reporting, because other national health expenditures are including reimbursements that are fully paid for by public sources and employers. Prior to 1979, data collection procedures were not conducted on a continuous monthly basis as per old collection techniques, so some 12-month percent changes were not available or N/As. More information can be found from the [BLS's Measuring Price Change in the CPI: Medical care](https://www.bls.gov/cpi/factsheets/medical-care.htm), [BLS's First Hundred Years of the Consumer Price Index](https://www.bls.gov/opub/mlr/2014/article/the-first-hundred-years-of-the-consumer-price-index.htm), and [BLS's Chapter 16 Consumer Expenditures and Income](https://www.bls.gov/opub/hom/pdf/cex-20110915.pdf)."
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
                    The "Consumer Price Index for All Urban Consumers (CPI-U) - not seasonally adjusted" **with 12-month percent change (not net change) enabled** should be pulled and used if the purpose is to find out what is the inflation rate annually. When news reporters 
                                     specify what is the inflation rate, the figure comes from this dataset. For more information, see [Overview of BLS Statistics on Inflation and Prices](https://www.bls.gov/bls/inflation.htm), [BLS's "About the CPI Inflation Calculator"](https://www.bls.gov/data/inflation_calculator.htm), [BLS's Consumer Price Index History](https://www.bls.gov/opub/hom/cpi/history.htm), and [BLS's First Hundred Years of the Consumer Price Index](https://www.bls.gov/opub/mlr/2014/article/the-first-hundred-years-of-the-consumer-price-index.htm).
                """)
                                ),
                                html.Li(
                                    dcc.Markdown("""The size of the labor force, employment, and unemployment undergo 
                                     fluctuations due to seasonal events including changes in weather, 
                                     harvests, major holidays, and school schedules. 
                                     Because these seasonal events follow a more or 
                                     less regular pattern each year, their influence on 
                                     statistical trends can be eliminated by seasonally 
                                     adjusting the statistics from month to month, which the seasonal adjustments are
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
                        html.P(
                            dcc.Markdown(
                                """ In the 1930s, patients had to cover all medical expenses -- mainly house visits by doctors, castor oil, and tonsillectomies -- out-of-pocket. Low cost hospitals existed but these places during the 19th century were "a place to be sick and die". The idea 
                                of a private health insurance didn't take off until World War II. Medicare and Medicaid didn't exist until 1965. Out-of-pocket before 
                                  1933 meant gold. After 1933, out-of-pocket meant paper money backed with gold, because
                                   people hoarded gold and deflation reached 10% during the Great Depression, which the Great Depression lasted from 1929 to 1941. During that time, 
                                   the BLS worked with other federal agencies to collect data on consumers' purchases to identify consumption estimates for urban and rural areas across the country including medical care. 
                                   Eventually, the US couldn't afford to continue using gold for goods and services, so the country turned to paper money backed with gold.
                                   
                                   
In World War II, which lasted from 1939-1945, private insurance industry grew faster so did the desire to have better healthcare coverage for those who were not employed as a civilian or who couldn't afford a private health insurance. 
US government eventually heed people's call in 1965 with the establishment of Medicare and Medicaid after series of long and bitter arguments about how to best support the country and allowing lots of opportunities to choose and to make money.
Medicare, as we know it today, is a health insurance program for the elderly. Medicaid is a health insurance program for people who have limited income. In 1973, the US ended using gold to support the dollar, because the demand for dollar kept increasing.
Around that same time, the country experienced great inflation, which started in 1965, where everything including medical care became more expensive thanks to drastic oil price increase from OPEC, a cartel led by Saudi Arabia, failure to continue supporting paper money with gold, and an inadequate metric to 
measure the US economy called the Philips Curve. Chairman Paul Volcker issued series of policies to bring inflation down. Although the road to recovery was painful (2 recessions between 1980 and 1982), Chairman Volcker's policies worked. The Great Inflation ended in 1982.  


Source(s):
* [BLS's Chapter 16 Consumer Expenditures and Income](https://www.bls.gov/opub/hom/pdf/cex-20110915.pdf)
* [Federal Reserve History's Essay on The Great Inflation](https://www.federalreservehistory.org/essays/great-inflation#:~:text=The%20Great%20Inflation%20was%20the%20defining%20macroeconomic%20period,policies%20of%20the%20Fed%20and%20other%20central%20banks.)
* [When Harry Truman Pushed for Universal Health Care](https://www.history.com/news/harry-truman-universal-health-care)
* [Federal Reserve History's Essay on the Great Depression](https://www.federalreservehistory.org/essays/great-depression)
* [Federal Reserve Bank - St. Louis's Article: Here’s Why the U.S. No Longer Follows a Gold Standard](https://www.stlouisfed.org/open-vault/2017/november/why-us-no-longer-follows-gold-standard)
* [BLS's Why This Counts: Medical Care Services in the CPI](https://www.bls.gov/blog/2015/why-this-counts-medical-care-services-in-the-cpi.htm)
* [Social Security Office of Retirement and Disability Policy's Health Insurance and Health Services](https://www.ssa.gov/policy/docs/progdesc/sspus/health-insurance-and-health-services.html)
* [HISTORY.com's World War II](https://www.history.com/topics/world-war-ii/world-war-ii-history)  
* [Brief History of Gold Standard in the United States](https://crsreports.congress.gov/product/pdf/R/R41887)
* [AMA Journal of Ethics: An Architectural History of US Community Hospitals](https://journalofethics.ama-assn.org/article/architectural-history-us-community-hospitals/2019-03)                                 """
                            )
                        ),
                        dcc.Graph(figure=inflation_healthcare.fig7, responsive=True),
                        html.P(dcc.Markdown('''
Post 1973 US currency change, the medical landscape was in the middle of implementing a new health insurance from the Health Maintenance Organization Act to 
encourage proactiveness in maintaining one's health and to combat soaring healthcare costs. It worked eventually in the mid-1990s, but it was not perfect. Patients and physicians saw
that system as a major hinderance to full recovery because "treatment decisions were being taken from their hands and their clinical 
judgements were being second-guessed". The health spending during the late 1980s and early 1990s increased rapidly because of "expensive new medical technologies and curtailing ambitious HMO-promoting programs".
Prior to 2008, there were 45 million uninsured Americans. After the Affordable Care Act was passed, 92% of Americans in 2023 had health insurance. In 2020, COVID-19 pandemic hit, which badly affected everything from 
getting supplies to unemployment to the nation's health. Health wise, the country got out of COVID-19 thanks to modern technological advancement in vaccines. In other aspects, the country is still dealing with the
aftermath of constricting supply lines during the COVID-19 pandemic (constricting supply lines leads to the need for hiring more people and increasing prices for products) and unsustainable increases for employment.
The aftermath is a sticky inflation, 2.6% in October 2024 and 2.4% in September 2024, which are not within the Federal Reserve Board's 2% inflation target. 2% inflation target would lead to achieving price stability.
                                            
Source(s):
* [AMA Journal of Ethics: The US Health Care Non-System, 1908-2008](https://journalofethics.ama-assn.org/article/us-health-care-non-system-1908-2008/2008-05)
* [An Architectural History of US Community Hospitals](https://journalofethics.ama-assn.org/article/architectural-history-us-community-hospitals/2019-03)
* [Health Insurance Coverage in the United States: 2023](https://www.census.gov/library/publications/2024/demo/p60-284.html)
* [BLS's What caused the high inflation during the COVID-19 period?](https://www.bls.gov/opub/mlr/2023/beyond-bls/what-caused-the-high-inflation-during-the-covid-19-period.htm)
* [Federal Reserve Board's Statement on Longer-Run Goals and Monetary Policy Strategy](https://www.federalreserve.gov/monetarypolicy/files/FOMC_LongerRunGoals_202008.pdf) ''')),
                        dcc.Graph(figure=inflation_healthcare.fig9, responsive=True),
                        html.P(dcc.Markdown('''
In 2023, the median personal income is about $42,000. According to the [US Bureau of Economic Analysis (BEA)'s Personal Income](https://apps.bea.gov/iTable/?reqid=19&step=2&isuri=1&categories=survey&_gl=1*9tge84*_ga*MTYxOTk1NTUzNy4xNzMxMDAzMzAy*_ga_J4698JNNFT*MTczMzQ1Mzc5My45LjEuMTczMzQ1MzgzNy4xNi4wLjA.#eyJhcHBpZCI6MTksInN0ZXBzIjpbMSwyLDNdLCJkYXRhIjpbWyJjYXRlZ29yaWVzIiwiU3VydmV5Il0sWyJOSVBBX1RhYmxlX0xpc3QiLCI1OCJdXX0=), the country amassed $23.8 trillion dollar in 2023 quarter 4. 

''')),
                        dcc.Graph(figure=inflation_healthcare.fig2, responsive=True),
                        dcc.Graph(figure=inflation_healthcare.fig3, responsive=True),
                        dcc.Graph(figure=inflation_healthcare.fig4, responsive=True),
                        html.P(dcc.Markdown("The unemployment rate shows the percentage of people **who are actively looking for a job**.")),
                        dcc.Graph(figure=inflation_healthcare.fig5, responsive=True),
                        html.P(dcc.Markdown('''
The "Civilian Not in Labor Force" graph represents people who are not eligible to be in the labor force -- people who are younger than 16 years old -- or who decided to not be in the labor force for multitude of reasons, **which are completely different from the unemployment rate graph**.
'''))
                    ],
                ),
                dcc.Tab(
                    label="Demo",
                    children=[
                        html.P(dcc.Markdown('''
To demonstrate what $100 medical cost would look like from 1974 to 2024, the medical cost data from the same source as the "Report" section was used.
This time, "1-month % change" (not net change) was selected to see the percent change on every month. The formula being used to calculate the changes in dollars is cost(new) = cost(old) * (1 + (1-month % change/100)).
Below is the graph showing what the $100 cost from 1974 would look like as time goes on.
''')),
                        dcc.Graph(figure=inflation_healthcare.fig8, responsive=True)
                    ],
                ),
                dcc.Tab(label="Conclusion", children=[html.P(dcc.Markdown('''
The "Report" and "Demo" tabs point to a continuous need to support the country's healthcare system and to improve the system. Recent records of the country's income were reviewed. Below are additional findings.
* 2024 Quarter 3: the BEA reported $5.1 trillion in income for federal level, but its current expenditure is about $7 trillion. It's on the path to spend $9.7 trillion for FY 2024 according to [USASpending.gov](https://www.usaspending.gov/).
* From BEA's report, the taxes on corporate income is noticeably low from the federal's perspective, which is about $483 billion for the same quarter in 2024. The overall (meaning from the federal, state, and local governments combined) is $647 billion.
* More information for the previous two bullets can be found from the [BEA's Government Current Receipts and Expenditures](https://apps.bea.gov/iTable/?reqid=19&step=2&isuri=1&categories=survey&_gl=1*s3gg1p*_ga*MTYxOTk1NTUzNy4xNzMxMDAzMzAy*_ga_J4698JNNFT*MTczMzUwODI5OS4xMC4xLjE3MzM1MDg5NDcuNjAuMC4w#eyJhcHBpZCI6MTksInN0ZXBzIjpbMSwyLDNdLCJkYXRhIjpbWyJDYXRlZ29yaWVzIiwiU3VydmV5Il0sWyJOSVBBX1RhYmxlX0xpc3QiLCI4NiJdXX0=) and the [BEA's Federal Government Current Receipts and Expenditures](https://apps.bea.gov/iTable/?reqid=19&step=2&isuri=1&categories=survey&_gl=1*s3gg1p*_ga*MTYxOTk1NTUzNy4xNzMxMDAzMzAy*_ga_J4698JNNFT*MTczMzUwODI5OS4xMC4xLjE3MzM1MDg5NDcuNjAuMC4w#eyJhcHBpZCI6MTksInN0ZXBzIjpbMSwyLDNdLCJkYXRhIjpbWyJjYXRlZ29yaWVzIiwiU3VydmV5Il0sWyJOSVBBX1RhYmxlX0xpc3QiLCI4NyJdXX0=).
* The [US Treasury](https://fiscaldata.treasury.gov/americas-finance-guide/national-deficit/) currently reports $1.83 trillion in total deficit for FY2024, and it is continuing to rise.
* For FY 2023, the [IRS](https://www.irs.gov/statistics/soi-tax-stats-irs-data-book) reported $456 billion in taxes from business income whereas individual income was $2.5 trillion and others (employment, estate and gift, and excise taxes) reported $1.6 trillion. 
* One major reason why is the list of all deductions on [Form 1120](https://www.irs.gov/pub/irs-pdf/f1120.pdf) and [business tax credits that any businesses can claim](https://www.irs.gov/credits-deductions/businesses). Any businesses can use all of them for each tax year as long as they fulfill all the requirements when filing a tax return. 
* IRS reported on [its website](https://www.irs.gov/newsroom/the-tax-gap) that roughly 87% of taxes were paid for tax years 2014-2016, which meant 13% of the taxes were still not paid. 

The country needs at least $3 trillion more to cover all expenditures and some portions of the annual deficit. In order to continue supporting the country's healthcare system, there needs to be a review and a revision to the tax system in order to better distribute resources to people who need support and to continue protect and look after this country. 
        
'''))]),
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
                                                                
                                                             
Within the Federal Reserve, the Federal Open Market Committee (FOMC) announced in 2020 that it believed that "inflation at the rate of 2 percent, as measured by the annual change in the price index for personal consumption expenditures, is most consistent over the longer run with the Federal Reserve's statutory mandate". So, the FOMC's objective to have a 2 percent inflation rate was chosen, because they found, from analyzing the personal consumption expenditure data, that 2 percent would bring the country closer to achieving its goals of maximum employment and stable prices.


**Important: please note that there's a difference between stable prices and affordable prices.** Stable prices in this case mean that there's no inflation or deflation. Even with a 2% inflation rate, if you want to be able to afford goods and services like food, housing, laundromat, clothing, etc., your wages need to catch up. That's why you hear discussions about increasing the minimum wage and why certain support programs such as Social Security are adjusted upwards to offset the inflation rate.                                                                
                                                                
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
                                always_open=False,
                            )
                        )
                    ],
                ),
            ]
        ),
    
)
])

if __name__ == "__main__":
    app.run(debug=True)
