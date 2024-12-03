#!/usr/bin/env python
# coding: utf-8

#Inflation and Healthcare Costs

#import data
import pandas as pd
import plotly.express as px

 
# Historical Inflation Rate

#%%
#find out the inflation rate by year
inflation_rate = pd.read_csv("historical_inflation_rate_as_of_20241124_not_seasonally_adj.csv")
inflation_rate["Month"] = inflation_rate["Label"].str[5:]
inflation_rate

#%%
#change the data type for inflation rate table's 12-month % change to numeric using pandas libary
inflation_rate["12-Month % Change"] = pd.to_numeric(inflation_rate["12-Month % Change"], errors = 'coerce')
inflation_rate


#%%
fig1 = px.line(inflation_rate, x="Year", y="12-Month % Change", 
                 hover_name="Month",
              title = "Inflation Rate Not Seasonally Adjusted 1914-2024")

fig1.add_annotation(x=1900,
            text="1913: BLS's first piece <br> of inflation data.", showarrow=False)
fig1.add_annotation(x=1933, y=16,
            text="1933: Classic Gold <br> Standard ended.", showarrow=False)
fig1.add_annotation(x=1973, y=20,
            text="1973: Using gold to back paper money ended. <br> Switched to Fiat money.", showarrow=False)
#fig1.show()



# <b>Fig 1</b>. The historical inflation rate data was provided by the BLS to see the general price behavior in goods and services. Data regarding goods and services are collected by the BLS's staff periodically. Below are sources regarding the history of BLS's data collection to identify the inflation rate.  
# 
# Source(s): [BLS's Consumer Price Index History](https://www.bls.gov/opub/hom/cpi/history.htm), [BLS's First Hundred Years of the Consumer Price Index](https://www.bls.gov/opub/mlr/2014/article/the-first-hundred-years-of-the-consumer-price-index.htm)

# ##### Below is a list of important events related to the historical inflation data, because these will help providing more context into analyzing historical medical cost data:
# 
# - <b>1914-1919: United States taking advantage of the economic expansion thanks to World War I without any protection</b>. University of California: Berkeley's staff wrote an essay, "The United States emerged from the First World War riding an enormous economic expansion. Unemployment had fallen to just 1.4%; while inflation and productivity rose in unison, a prosperity fuelled the demand for wartime deliveries, which provided a boost to the nation’s surging manufacturing sector. But the cost of achieving this growth, unbeknownst to the populace, was perilously high. The Federal Reserve, chartered only in 1913, had been compelled to maintain low interest rates by the need to finance military operations. After the armistice, however, monetary policy remained lax, a stance designed to prevent capital losses on the final war bond offering, lower the costs of servicing outstanding debt, and facilitate a smooth shift to peacetime conditions. As a result, inflation increased unchecked, to the growing consternation of policy advisors, and in 1919, the incumbent Wilson administration initiated austerity reforms". Source(s): [In the Shadow of the Slump: The Depression of 1920-1921 by University of California: Berkeley's staff](https://econreview.studentorg.berkeley.edu/in-the-shadow-of-the-slump-the-depression-of-1920-1921/)
# - <b>1920-1921: Extreme price deflation</b>. University of California: Berkeley's staff wrote in the same essay, "Wilson's administration managed to quickly balance the budget, but the disinflationary retrenchment presaged recession, especially coupled with the swarm of malignant economic factors then at work. These included the closure or retooling of munitions factories, the return of 1.6 million soldiers to the civilian labor force (a growth of 4.1%), and the weakening of union power. The erosion of workers’ bargaining power, against the backdrop of the transition from military to peacetime production, further suppressed wages and increased the short-term gravity of the inevitable slump. In January of 1920, when postwar industrial production reached its zenith, the promised downturn began to take hold. Production fell by 32.5% over the following year, a decline second only to the Great Depression in American economic history and occurring over a shorter span. At the same time, prices plunged by over 15%, and unemployment approached a startling 12%. The rate of business failures tripled and surviving enterprises saw average decreases of 75% in profits". Source(s): [In the Shadow of the Slump: The Depression of 1920-1921 by University of California: Berkeley's staff](https://econreview.studentorg.berkeley.edu/in-the-shadow-of-the-slump-the-depression-of-1920-1921/)
# - <b>1929-1939: Great Depression</b>. People hoarded gold instead of depositing it in banks in the beginning, which created an international gold shortage. Eventually, countries around the world ran out of supply and were forced off the gold standard. Source(s): [Here’s Why the U.S. No Longer Follows a Gold Standard by the Federal Reserve Bank -- St. Louis branch](https://www.stlouisfed.org/open-vault/2017/november/why-us-no-longer-follows-gold-standard), [Great Depression by HISTORY.com](https://www.history.com/topics/great-depression/great-depression-history)
# - <b>1930-1933: Federal Reserve's failure to stem the decline in the supply of money. Classic Gold Standard for the US ended in 1933</b>. From Universities' and Federal Reserve's staff who wrote an essay about the Great Depression, "From the fall of 1930 through the winter of 1933, the money supply fell by nearly 30 percent. Federal Reserve's failure caused deflation increased debt burdens; distorted economic decision-making; reduced consumption; increased unemployment; and forced banks, firms, and individuals into bankruptcy. The deflation stemmed from the collapse of the banking system, as explained in the essay on the banking panics of 1930 and 1931". Source(s): [The Great Depression Essay by Universities' and Federal Reserve's staff](https://www.federalreservehistory.org/essays/great-depression)
# - <b>Cumulative inflation in 1939 and 1949: Periods of very high inflation with periods of lower inflation</b>. This inflation volatility was 
# largely related to wartime inflationary pressures -- World War II -- combined with government price (and wage) controls. Source(s): [A Real Great Compression: Inflation and Inequality in the 1940s](https://www.nber.org/system/files/chapters/c14842/c14842.pdf)
# - <b>1950-1953: Korean War inflation and price control</b>. Some of the jump in prices was attributable to consumers moving up their purchasing to avoid a feared absence of consumer goods like that experienced during World War II. Eventually, the Treasury-Federal Reserve Accord agreement allowed the Federal Reserve to do what it needed to do to combat the inflation. Although the US economy experienced a short but sharp recession after the agreement from July 1953 through May 1954, the recession was characterized by a rapid drop in growth followed by a quick recovery, known as a V-shaped recovery. Source(s): [Council on Foreign Relations's What the Korean War Era Reveals About the Fed’s Inflation Dilemma](https://www.cfr.org/article/what-korean-war-era-reveals-about-feds-inflation-dilemma)
# - <b>1965-1982: Great Inflation</b>. The combination of the inability to continue backing the dollar with gold as the demand for dollar increased, OPEC's massive cut in oil production multiple times, and horrible economic policies -- one of them being the Philips Curve as a metric for defining what constituted a good US economy -- created an opportunity for a massive inflation rate. The Nixon administration tried to resolve inflation using wage and price controls, which exacerbated shortages for many goods and services. The Ford administration introduced a program called "Whip Inflation Now", which also failed horribly. Eventually, in 1979, a new chairperson of the Federal Reserve Board named Paul Volcker decided to increase interest rate and slower the growth of the money -- or dollar -- supply. Chairman Volcker's method worked but the road to recovery was painful. The country entered a recession that lasted for a year, but the inflation rate continued to decrease to eventually under 5 percent. Source(s): [The Great Inflation Essay by Universities' and Federal Reserve's staff](https://www.federalreservehistory.org/essays/great-inflation)
# - <b>1990 - 1991: Oil and Gas spike</b>.  Iraq invaded Kuwait, which became the Gulf War. The U.S. economy was hit by a major oil price shock thanks to the war along with the Savings and Loan (S&L) Crisis. To combat the recession, Congress made new laws like the Omnibus Budget Reconciliation Act of 1990 and the Financial Institutions Reform, Recovery, and Enforcement Act. The Federal Reserve Board tightened monetary policy then adjust it as time went on. The oil prices also declined eventually. Source(s): [The Current Economic Recession (2001 - 2002): How Long, How Deep, and How Different From the Past? by the Congressional Research Service](https://www.everycrsreport.com/files/20020110_RL31237_3dfa2a994f8c6dc60ab14bb2daab081a32bfed92.pdf)
# - <b>2007 to 2009: Great Recession</b>. Housing market crashed. Unemployment rate increased from 5% to 10%. Congress passed Economic Stimulus Act of 2008 and the American Recovery and Reinvestment Act of 2009 to help people who were badly affected by the housing market crash. The Federal Reserve Board used alot of nontraditional methods to also address the housing market while keeping an eye on the inflation rate and the unemployment rate, which was why and how the inflation rate didn't increase drastically as it did in the past. Source(s): [The Great Recession Essay by a Federal Reserve's staff](https://www.federalreservehistory.org/essays/great-recession-of-200709)
# - <b>2020 - present: COVID-19 pandemic and trying to deal with current events</b>. Source(s): [BLS's What caused the high inflation during the COVID-19 period?](https://www.bls.gov/opub/mlr/2023/beyond-bls/what-caused-the-high-inflation-during-the-covid-19-period.htm), [BLS's Unemployment rate returned to its prepandemic level in 2022](https://www.bls.gov/opub/mlr/2023/article/unemployment-rate-returned-to-its-prepandemic-level-in-2022.htm)

# ### Civilian Labor Force Participation Rate

# %%


#find out civilian labor force participation rate
labor_force_participation = pd.read_csv("seasonally_adjusted_labor_force_participation_rate_as_of_20241124.csv")
labor_force_participation["Month"] = labor_force_participation["Label"].str[5:]
labor_force_participation


#%%


fig2 = px.line(labor_force_participation, x="Year", y="Value", 
              labels = {"Year":"year", "Value":"participation rate (%)"},
              hover_name = "Month",
              title = "Civilian Labor Force Participation Rate Seasonally Adjusted 1948-2024")

#fig2.show()
#fig2.write_html("labor_force_participation.html")


# <b>Fig 2</b>. The labor force participation graph shows the percentage of people who are either actively working (employed) or who are actively looking for a job (unemployed).

# #### Employment-Population Ratio

# %%


employed_rate = pd.read_csv("Employment_Population_Ratio_as_of_20241201_seasonally_adj.csv")
employed_rate["Month"] = employed_rate["Label"].str[5:]
employed_rate


# %%


fig3 = px.line(employed_rate, x="Year", y="Value", 
              labels = {"Year":"year", "Value":"Employed People (%)"},
              hover_name = "Month",
              title = "Percentage of People who are Employed Seasonally Adjusted 1948-2024")

#fig3.show()
#fig3.write_html("employed_percent.html")


# <b>Fig 3</b>.

# #### Civilian Unemployment Rate

# %%


# find out unemployment rate
unemployment_rate = pd.read_csv("seasonally_adjusted_unemployment_rate_as_of_20241124.csv")
unemployment_rate["Month"] = unemployment_rate["Label"].str[5:]
unemployment_rate


# %%


fig4 = px.line(unemployment_rate, x="Year", y="Value", 
              labels = {"Year":"year", "Value":"unemployment rate (%)"},
              hover_name = "Month",
              title = "Civilian Unemployment Rate Seasonally Adjusted 1948-2024")

#fig4.show()
#fig4.write_html("civilian_unemployment_rate.html")


# <b>Fig 4</b>. The unemployment graph shows the percentage of people in the labor force who are unemployed.

# ##### Important note regarding the civilian labor force participation rate and unemployment rate data
# 
# Both datasets come from the Current Population Survey. The BLS and the Census Bureau work together on this survey. The first piece of data from the Current Population Survey was available starting in 1948. Below are sources to read more on the history and the methodology of this survey.
# 
# Source(s): [Census Bureau's History of the Current Population Survey](https://www.census.gov/programs-surveys/cps/about/history-of-the-cps.html), [BLS's How the Government Measures Unemployment](https://www.bls.gov/cps/cps_htgm.htm)

# #### Percent of People Not in Labor Force

# %%


labor_force_participation["Not in Labor Force"] = 100 - labor_force_participation["Value"]
labor_force_participation


# %%


fig5 = px.line(labor_force_participation, x="Year", y="Not in Labor Force", 
              labels = {"Year":"year", "Not in Labor Force":"Not Labor Force (%)"},
              hover_name = "Month",
              title = "Civilian Not in Labor Force Seasonally Adjusted 1948-2024")

#fig5.show()
#fig5.write_html("not_labor_force_rate.html")


# <b>Fig 5</b>.

# ### Medical Care Cost Rate

# %%


#find out healthcare costs by year
healthcare_cost_cpi = pd.read_csv("medical_care_cpi_not_seasonally_adjusted_as_of_20241124.csv")
healthcare_cost_cpi["Month"] = healthcare_cost_cpi["Label"].str[5:]
healthcare_cost_cpi


#%%


healthcare_cost_cpi["12-Month % Change"] = pd.to_numeric(healthcare_cost_cpi["12-Month % Change"], errors = 'coerce')
#healthcare_cost_cpi.info()


# %%


fig6 = px.line(healthcare_cost_cpi, x="Year", y="12-Month % Change", 
                 hover_name="Month",
              title = "Medical Care Cost Rate Not Seasonally Adjusted 1936-2024")
fig6.add_annotation(x=1933, y=16,
            text="1933: Classic Gold <br> Standard ended.", showarrow=False)
fig6.add_annotation(x=1973, y=20,
            text="1973: Using gold to back paper money ended. <br> Switched to Fiat money.", showarrow=False)
#fig6.show()
#fig6.write_html("medical_care_cost_rate.html")


# <b>Fig 6</b>. The medical care cost rate shows the overall price behavior for all medical goods and services. Below is the source describinng all components for medical care.
# 
# Source(s): [BLS's Measuring Price Change in the CPI: Medical care](https://www.bls.gov/cpi/factsheets/medical-care.htm)

# ### Medical Care Cost Rate vs Inflation Rate

# %%


inflation_rate_1974_onward = inflation_rate[inflation_rate["Year"] >= 1974]
inflation_rate_1974_onward


# %%


medical_cost_1974_onward = healthcare_cost_cpi[healthcare_cost_cpi["Year"] >= 1974]
medical_cost_1974_onward




#%%
inflation_rate_1974_onward_v2 = inflation_rate_1974_onward.rename({'12-Month % Change': 'inflation_rate_12-month_%_change'}, axis='columns')
inflation_rate_1974_onward_v2




#%%
medical_cost_1974_onward_v2 = medical_cost_1974_onward.rename({'12-Month % Change': 'medical_cost_rate_12-month_%_change'}, axis='columns')
medical_cost_1974_onward_v2



#%%

inflation_rate_1974_onward_v2_year_rate = inflation_rate_1974_onward_v2[["Label", "inflation_rate_12-month_%_change"]]
inflation_rate_1974_onward_v2_year_rate


# %%


medical_cost_1974_onward_v2_year_rate = medical_cost_1974_onward_v2[["Label", "medical_cost_rate_12-month_%_change"]]
medical_cost_1974_onward_v2_year_rate


# In[109]:


inflation_rate_1974_onward_v2_year_rate.set_index('Label', inplace=True)
medical_cost_1974_onward_v2_year_rate.set_index('Label', inplace=True)


# In[110]:


medical_cost_inflation_rate_table = pd.concat([inflation_rate_1974_onward_v2_year_rate, medical_cost_1974_onward_v2_year_rate], axis=1)
medical_cost_inflation_rate_table.reset_index(inplace=True)
medical_cost_inflation_rate_table


# In[111]:


fig7 = px.line(medical_cost_inflation_rate_table, x="Label", y=medical_cost_inflation_rate_table.columns[1:], title="Medical Care Cost Rate vs Inflation Rate Not Seasonally Adjusted 1974 - 2024")
fig7.update_yaxes(title="12-Month % Change")
#fig7.show()
#fig7.write_html("medical_care_vs_inflation_rate.html")


# <b>Fig 7</b>.

# #### Medical Services

# In[112]:


medical_services_cpi = pd.read_csv("Medical_care_services_not_seasonally_adjusted_as_of_20241129.csv")
medical_services_cpi["Month"] = medical_services_cpi["Label"].str[5:]
medical_services_cpi


# In[113]:


medical_services_cpi["12-Month % Change"] = pd.to_numeric(medical_services_cpi["12-Month % Change"], errors = 'coerce')
#medical_services_cpi.info()


# In[114]:


fig8 = px.line(medical_services_cpi, x="Year", y="12-Month % Change", 
                 hover_name = "Month",
              title = "Medical Services Cost Rate Not Seasonally Adjusted 1936 - 2024")
#fig8.show()
#fig8.write_html("medical_services_cost.html")


# <b>Fig 8</b>. The medical services cost rate graph covers the overall price behavior for professional medical services, hospital services, nursing home services, adult day care, and health insurance combined.
# 
# Source(s): [BLS's Measuring Price Change in the CPI: Medical care](https://www.bls.gov/cpi/factsheets/medical-care.htm)

# #### Prescription Drugs

# In[115]:


prescription_drugs_cpi = pd.read_csv("Prescription_Drugs_Not_Seasonally_Adj_as_of_20241129.csv")
prescription_drugs_cpi["Month"] = prescription_drugs_cpi["Label"].str[5:]
prescription_drugs_cpi


# In[116]:


prescription_drugs_cpi["12-Month % Change"] = pd.to_numeric(prescription_drugs_cpi["12-Month % Change"], errors = 'coerce')
#prescription_drugs_cpi.info()


# In[117]:


fig9 = px.line(prescription_drugs_cpi, x="Year", y="12-Month % Change", 
                 hover_name="Month",
              title = "Prescription Drugs Cost Rate Not Seasonally Adjusted 1948 - 2024")
#fig9.show()
#fig9.write_html("prescription_drugs_cost.html")


# <b>Fig 9</b>. The prescription drugs cost rate covers price behavior for all drugs dispensed by prescription combined including mail order outlets. Prices reported represent transaction prices between the pharmacy, patient, and third party payer, if applicable.
# 
# Source(s): [BLS's Measuring Price Change in the CPI: Medical care](https://www.bls.gov/cpi/factsheets/medical-care.htm)

# #### Over-the-Counter Drugs

# %%


nonprescription_drugs_cpi = pd.read_csv("Nonprescription_Drugs_Not_Seasonally_Adj_as_of_20241129.csv")
nonprescription_drugs_cpi["Month"] = prescription_drugs_cpi["Label"].str[5:]
nonprescription_drugs_cpi


# In[119]:


nonprescription_drugs_cpi["12-Month % Change"] = pd.to_numeric(nonprescription_drugs_cpi["12-Month % Change"], errors = 'coerce')



# %%


fig10 = px.line(nonprescription_drugs_cpi, x="Year", y="12-Month % Change", 
                 hover_name="Month",
              title = "Over-the-Counter Drugs Cost Rate Not Seasonally Adjusted 2010 - 2024")
#fig10.show()



# <b>Fig 10</b>. The over-the-counter drugs cost rate covers price behavior for all nonprescription drugs, including topicals combined.
# 
# Source(s): [BLS's Measuring Price Change in the CPI: Medical care](https://www.bls.gov/cpi/factsheets/medical-care.htm)


#grab the total personal income from the BEA website

#research what is the current federal budget and what is the deficit and what is the revenue and provide an estimate of how much more do we need

#get the actual medical cost in today's dollars -- 2024 -- using c(new) = c(old) * (1+M/100)


