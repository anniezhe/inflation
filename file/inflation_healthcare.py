#!/usr/bin/env python
# coding: utf-8

#Inflation and Healthcare Costs

#%%
#import data
import pandas as pd
import plotly.express as px

 
# Historical Inflation Rate

#find out the inflation rate by year
inflation_rate = pd.read_csv("data/historical_inflation_rate_as_of_20241124_not_seasonally_adj.csv")
inflation_rate["Month"] = inflation_rate["Label"].str[5:]


#change the data type for inflation rate table's 12-month % change to numeric using pandas libary
inflation_rate["12-Month % Change"] = pd.to_numeric(inflation_rate["12-Month % Change"], errors = 'coerce')


fig1 = px.line(inflation_rate, x="Year", y="12-Month % Change", 
                 hover_name="Label", labels={'12-Month % Change': '12-Month % Change <br><sup>not seasonally adjusted</sup>'},
              title = 'Inflation Rate 1913-2024 <br><sup>Source: <a href="https://data.bls.gov/dataViewer/view/timeseries/CUUR0000SA0">BLS.gov Consumer Price Index for All Urban Consumers (CPI-U) - not seasonally adjusted</a><br>See "Methods" tab for important notes.</sup>')

fig1.add_annotation(x=1900,
            text="1913: BLS's first piece <br> of data available.", showarrow=False)
fig1.add_annotation(x=1933, y=16,
            text="1933: Classic Gold <br> Standard ended.", showarrow=False)
fig1.add_annotation(x=1973, y=20,
            text="1973: Using gold to back paper money ended. <br> Switched to Fiat money.", showarrow=False)



#Civilian Labor Force Participation Rate


#find out civilian labor force participation rate
labor_force_participation = pd.read_csv("data/seasonally_adjusted_labor_force_participation_rate_as_of_20241124.csv")
labor_force_participation["Month"] = labor_force_participation["Label"].str[5:]



fig2 = px.line(labor_force_participation, x="Year", y="Value", 
              labels = {"Year":"year", "Value":"participation rate (%) <br><sup>seasonally adjusted</sup>"},
              hover_name = "Label",
              title = 'Civilian Labor Force Participation Rate 1948-2024 <br><sup>Source: <a href="https://data.bls.gov/dataViewer/view/timeseries/LNS11300000">BLS.gov Civilian Labor Force Participation Rate - seasonally adjusted</a><br> See "Methods" tab for important notes.</sup>')
fig2.add_annotation(x=1940, y=60,
            text="1948: BLS's first piece <br> of data available.", showarrow=False)

#Employment-Population Ratio


employed_rate = pd.read_csv("data/Employment_Population_Ratio_as_of_20241201_seasonally_adj.csv")
employed_rate["Month"] = employed_rate["Label"].str[5:]

fig3 = px.line(employed_rate, x="Year", y="Value", 
              labels = {"Year":"year", "Value":"Employed People (%) <br> <sup>seasonally adjusted</sup>"},
              hover_name = "Label",
              title = 'Percentage of People who are Employed 1948-2024 <br><sup>Source: <a href ="https://data.bls.gov/dataViewer/view/timeseries/LNS12300000">BLS.gov Employment-Population Ratio from the Current Population Survey - seasonally adjusted</a><br>See "Methods" for important notes.</sup>')
fig3.add_annotation(x=1940, y=58,
            text="1948: BLS's first piece <br> of data available.", showarrow=False)

# Civilian Unemployment Rate


# find out unemployment rate
unemployment_rate = pd.read_csv("data/seasonally_adjusted_unemployment_rate_as_of_20241124.csv")
unemployment_rate["Month"] = unemployment_rate["Label"].str[5:]

fig4 = px.line(unemployment_rate, x="Year", y="Value", 
              labels = {"Year":"year", "Value":"unemployment rate (%) <br> <sup>seasonally adjusted</sup>"},
              hover_name = "Label",
              title = 'Civilian Unemployment Rate 1948-2024 <br><sup>Source: <a href="https://data.bls.gov/dataViewer/view/timeseries/LNS14000000">BLS.gov Civilian Unemployment Rate - seasonally adjusted</a> <br> See "Methods" for important notes.</sup>')

fig4.add_annotation(x=1940, y=4,
            text="1948: BLS's first piece <br> of data available.", showarrow=False)

# Percent of People Not in Labor Force

labor_force_participation["Not in Labor Force"] = 100 - labor_force_participation["Value"]




fig5 = px.line(labor_force_participation, x="Year", y="Not in Labor Force", 
              labels = {"Year":"year", "Not in Labor Force":"Not Labor Force (%)"},
              hover_name = "Month",
              title = 'Civilian Not in Labor Force 1948-2024 <br><sup>Percentage is identified using this formula: 100 - rate from Civilian Labor Force Participation data</sup>')


# Medical Care Cost Rate


#find out healthcare costs by year
healthcare_cost_cpi = pd.read_csv("data/medical_care_cpi_not_seasonally_adjusted_as_of_20241124.csv")
healthcare_cost_cpi["Month"] = healthcare_cost_cpi["Label"].str[5:]




healthcare_cost_cpi["12-Month % Change"] = pd.to_numeric(healthcare_cost_cpi["12-Month % Change"], errors = 'coerce')


fig6 = px.line(healthcare_cost_cpi, x="Year", y="12-Month % Change", 
                 hover_name="Label", labels={"12-Month % Change": "12-Month % Change <br><sup>not seasonally adjusted</sup>"},
              title = 'Consumer Medical Care Cost Rate 1936-2024 <br><sup>Source: <a href="https://data.bls.gov/dataViewer/view/timeseries/CUUR0000SAM">BLS.gov Medical Care from Consumer Price Index Survey - not seasonally adjusted</a><br> See "Methods" for important notes.</sup>')

fig6.add_annotation(x=1936, y=10,
            text="1936: BLS's first piece of data available.", showarrow=False)
fig6.add_annotation(x=1973, y=20,
            text="1973: Using gold to back paper money ended. <br> Switched to Fiat money.", showarrow=False)


#Medical Care Cost Rate vs Inflation Rate



inflation_rate_1974_onward = inflation_rate[inflation_rate["Year"] >= 1974]



medical_cost_1974_onward = healthcare_cost_cpi[healthcare_cost_cpi["Year"] >= 1974]



inflation_rate_1974_onward_v2 = inflation_rate_1974_onward.rename({'12-Month % Change': 'inflation_rate_12-month_%_change'}, axis='columns')




medical_cost_1974_onward_v2 = medical_cost_1974_onward.rename({'12-Month % Change': 'medical_cost_rate_12-month_%_change'}, axis='columns')



inflation_rate_1974_onward_v2_year_rate = inflation_rate_1974_onward_v2[["Label", "inflation_rate_12-month_%_change"]]



medical_cost_1974_onward_v2_year_rate = medical_cost_1974_onward_v2[["Label", "medical_cost_rate_12-month_%_change"]]



inflation_rate_1974_onward_v2_year_rate.set_index('Label', inplace=True)
medical_cost_1974_onward_v2_year_rate.set_index('Label', inplace=True)




medical_cost_inflation_rate_table = pd.concat([inflation_rate_1974_onward_v2_year_rate, medical_cost_1974_onward_v2_year_rate], axis=1)
medical_cost_inflation_rate_table.reset_index(inplace=True)
medical_cost_inflation_rate_table["Year"] = medical_cost_inflation_rate_table["Label"].str[:5]




fig7 = px.line(medical_cost_inflation_rate_table, x="Year", y=medical_cost_inflation_rate_table.columns[1:],title="Medical Care Cost Rate vs Inflation Rate <br>Post 1973 US Currency Change", hover_name="Label")
fig7.update_yaxes(title="Percent (%)")



#grab the total personal income from a government agency website

#research what is the current federal budget and what is the deficit and what is the revenue and provide an estimate of how much more do we need

#get the actual medical cost in today's dollars -- 2024 -- using c(new) = c(old) * (1+M/100)

medical_cost_table = pd.read_excel("data/medical_inflation_table.xlsx")
medical_cost_table["Year"] = medical_cost_table["Label"].str[:5]
medical_cost_table["$100_out-of-pocket_w/o_inflation_adj"] = medical_cost_table["$100_out-of-pocket_w/o_inflation_adj"].round(2)


fig8 = px.line(medical_cost_table, x="Year", y="$100_out-of-pocket_w/o_inflation_adj", 
                 hover_name="Label",
              title = "$100 out-of-pocket medical cost without inflation rate adj")

#get personal income
personal_income_US = pd.read_csv("data/PI.csv")
personal_income_US["Billions of Dollars"] = personal_income_US["PI"]
fig9 = px.line(personal_income_US, x="DATE", y="Billions of Dollars", title='Personal Income in US in Billions of Dollars <br><sup>Source: <a href= "https://fred.stlouisfed.org/seriesBeta/PI">Federal Reserve Bank - St.Louis Branch Personal Income</a></sup>')

personal_outlays_US = pd.read_csv("data/Personal_Outlays_AH_20241208.csv")
personal_outlays_US["Billions of Dollars"] = personal_outlays_US["A068RC1"]
fig10 = px.line(personal_outlays_US, x="DATE", y="Billions of Dollars", title='Personal Outlays in Billions of Dollars <br><sup>Source: <a href="https://fred.stlouisfed.org/seriesBeta/A068RC1">Federal Reserve Bank - St.Louis Branch Personal Outlays</a></sup>')

US_corporate_profit = pd.read_csv("data/CPROFIT.csv")
US_corporate_profit["Billions of Dollars"] = US_corporate_profit["CPROFIT"]
fig11 = px.line(US_corporate_profit, x="DATE", y="Billions of Dollars", title='US Corporate Profits w/ Inventory and Capital Consumption Adjustments <br><sup>Source: <a href="https://fred.stlouisfed.org/seriesBeta/CPROFIT">Federal Reserve Bank - St.Louis Corporate Profits w/ Inventory and Capital Consumption Adjs</a></sup>')

#get mean and median income from FRED
mean_personal_income = pd.read_csv("data/Mean_Personal_Income_US_AH_20241208.csv")
mean_personal_income2 = mean_personal_income.rename({"MAPAINUSA646N":"Avg Personal income in Current Dollars"}, axis='columns')
fig12 = px.line(mean_personal_income2, x="DATE", y="Avg Personal income in Current Dollars", title = 'Average Personal Income in the US in Current Dollars <br> <sup><a href = "https://fred.stlouisfed.org/seriesBeta/MAPAINUSA646N">Federal Reserve Bank - St.Louis Mean Personal Income in the US</a></sup>')

median_personal_income=pd.read_csv("data/Personal_Income_Median_US_AH_20241205.csv")
median_personal_income2 = median_personal_income.rename({"MEPAINUSA646N":"Median Personal Income in Current Dollars"}, axis='columns')
fig13 = px.line(median_personal_income2, x="DATE", y="Median Personal Income in Current Dollars", title = 'Median Personal Income in the US in Current Dollars <br><sup><a href = "https://fred.stlouisfed.org/seriesBeta/MEPAINUSA646N">Federal Reserve Bank St.Louis - Median Personal Income in the US</a></sup>')

mean_personal_income2.set_index('DATE', inplace=True)
median_personal_income2.set_index('DATE', inplace=True)

mean_median_personal_income_US = pd.concat([mean_personal_income2, median_personal_income2], axis=1)
mean_median_personal_income_US.reset_index(inplace=True)
fig14 = px.line(mean_median_personal_income_US, x="DATE", y=mean_median_personal_income_US.columns[1:], title="Historical Comparison Between Average Personal Income and Median Personal Income")
fig14.update_yaxes(title="Current Dollars")
# %%
