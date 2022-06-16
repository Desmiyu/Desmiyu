import pandas as pd
path=r'G:\.shortcut-targets-by-id\1qNiN--9Qfnfgk1CC9BHaQ2lkqUOfo_JN\WD Testing\WD_EIB\2022-06-14-10-44-32\Canada\df.csv'
ChaFile= pd.read_csv(path)
NewDF= ChaFile
# NewDF= ChaFile[
#             ((ChaFile.ACTNUMBR_5>=40000) & (ChaFile.ACTNUMBR_5 <50000)) #filtering just the revenue accounts
#             #&ChaFile["gp_trip_code"].str.startswith("GAP",na = False) #begins with GAP
#             | (ChaFile.ACTNUMBR_5==22500) #or account is  equal to 22500 test
#             ] 
# print(NewDF)
df=NewDF
print(df)
df_Tripcode_blank=df[
                    (pd.isnull(df['gp_trip_code'])!=True)  #
                    &
                    (pd.isnull(df['trip_code'])==True) #
                    # &
                    # (pd.isnull(df['service_id'])==True) #
                    # &
                    # (pd.isnull(df['Legacy ID CC_CODE_LEGACY'])==True) #Not sure why, but this correct the remaining issues. lol             
                    ]
print(df_Tripcode_blank)
df_Tripcode_blank.to_csv('df_tripcode_blank.csv')





#GP_REC_ID: 91538913, 91698348, 91698350
    ###somethign special with 3817771, in list of missing, yet criteria is all available
    ##Missing is basically in final reportr after all filters.
    #missing 3 transactions

## MIssing booking ID, so it needs to be joined manually.
# select trip_code, deleted ,* from compass_public.trip t 
# where trip_code in ('GNANUPN210912-O1'
# ,'GAPzSPAAT211011-O1'
# ,'GAPzSPIDT211004-O1'
# ,'GAPzSPAAT211011-O1'
# ,'GAPzSPIDT211004-O1'
# ,'GPXXLQCSX211222-O1'
# ,'GPXzXVUHSX211221-O1'
# ,'GPAAHRA211003-O1'
# ,'GPFDPBE210625-O1'
# ,'GPFDPEE210627-O1')



#####Waiting in QUeenie
##GP_Rec_ID: 91362475, Region name change is not expected. It is related to booking. should be one agent per booking: 1649050
    #Not quite sure the issue here. Need to check table: 
    # select b.id, a.sub_territory from compass_public.booking b
    # left join compass_public.agent a
    # on b.agent = a.id 
    # where b.id=1649050
    # EXPECTED RESULT: EU NEU Northern Europe
    #     ST_Agency_EU__NEU__Northern_Europe ()
    #     ST_Direct_EU__NEU__Northern_Europe (Not sure how this this possible, must be two agents per name)
#This is fixed.. kind of. FDM mapping.


#Example of Duplications
# -91362475 - Who Regions, Mapping issue.
# -91495772,91495775  - # Two different Travel Styules

#######  Working on now
##GP_Rec_ID: 91361653, 91361654, 91361655, 91361656--- reporting office 
    #Line: 850  df_compass_tripcodes = df_compass_booking_tripcodes[['trip_code','parent_trip_code','revenue_fraction','revenue_stream','travel_style']].drop_duplicates()
    #Line: 851 df_compass_booking = df_compass_booking_tripcodes[['id','billing_group_name','reporting_office_name','agent','associated_agent','online','agent_code','sub_territory','service_id']].drop_duplicates()
    #Move 'reporting_office_name' to from 851 to 850.







# df1= NewDF[[
#     'ACTNUMBR_5'
#     ,'gp_rec_id'
#     ,'CRDTAMNT'
#     ,'DEBITAMT'
#     ,'REFRENCE'
#     ,'DSCRIPTN'
#     ,'bookingno'
#     ,'gp_service_id'
#     ,'gp_trip_code'
#     ,'trip_code'
#     ,'parent_trip_code'
#     ]]
# df1['Teest']=df1["gp_trip_code"].str.startswith("GAP",na = False) #df1['Teest'] adds a new column

# #df2=df1["gp_trip_code"].str.startswith("GAP",na = False)
# df3=df1[
#         df1["gp_trip_code"].str.startswith("GAP",na = False) #begins with GAP
#         ]


# print(df3)


#     df_compass_tripcodes = df_compass_booking_tripcodes[['trip_code','parent_trip_code','reporting_office_name','revenue_fraction','revenue_stream','travel_style']].drop_duplicates()
#     df_compass_booking = df_compass_booking_tripcodes[['id','billing_group_name','agent','associated_agent','online','agent_code','sub_territory','service_id']].drop_duplicates()
# # Load the excel_file's Sheet1 as a dataframe
#df = excel_file.parse('LookerSchemaData')
#print(df)

 