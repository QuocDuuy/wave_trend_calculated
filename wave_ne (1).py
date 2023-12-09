import pandas as pd
from datetime import datetime
import math
import statistics
data = pd.read_json('report_3.json')
#khoi tao dataFrame moi
df = pd.DataFrame({
    "id": None,
    "total": None,
}, index=[0])
df.dropna(axis=0,inplace=True)

# for comment
timestamps = []
ind = 0
for i in data["comment"]:
    timestamp = []
    for j in i["times"]:
        j = datetime.strptime(j,"%Y-%m-%dT%H:%M:%S.%fZ")
        timestamp.append(j)
    timestamp.sort()
    timestamps.append(timestamp)
    
    tam = pd.DataFrame(
        {
            "id": data.iloc[ind,0],
            "total": i["total"],
        },index=[ind]
    )
    ind +=1
    df = pd.concat([df,tam],axis=0)

# for like
# like_timestamps = []
# like_idx = 0
# for i in data["like"]:
#     like_timestamp = []
#     try:
#         for j in i["times"]:
#             j = datetime.strptime(j, "%Y-%m-%dT%H:%M:%S.%fZ")
#             like_timestamp.append(j)
#         like_timestamp.sort()
#         like_timestamps.append(like_timestamp)
#     except: continue
#     tam_2 = pd.DataFrame(
#         {
#             "total": i["total"]
#         } ,index=[like_idx]
#     )
#     like_idx += 1
#     df = pd.concat([df, tam_2], axis = 0)



#tao cot "timestamp"
df["timestamp"] = timestamps
# df["like_timestamp"] = like_timestamps

print(df)
m_median = df["total"].median()
print("Trung binh tuong tac: ",m_median)
print("Tong so luong tuong tac: ",df["total"].sum())
print("Tong so bai viet:", df["id"].count())

# tính toán ( sóng ngắn đang có vấn đề ở ngưỡng dưới nên note lại)
# dem = 0

# #save
# s_wave_short = []
# s_wave_mean = []
# s_wave_long = []

# wave_short = []

# cham_nguong = []
# #index
# ind = 0

# for i in df["timestamp"]:
#     first_time = i[0]
#     for j in range(0,len(i)):
#         if i[j].replace(second=0, microsecond = 0) not in tam:
#             tam = []
#             tam.append(i[j].replace(second =0,microsecond = 0))
#             dem = 1
                
#         else:
#             dem += 1
#             if dem > 44 and j+1 <len(i) and i[j].replace(second =0,microsecond = 0) != i[j+1].replace(second =0,microsecond = 0):
#                 #wave short
#                 time_active = (i[j] - first_time).seconds
#                 wave_short.append(time_active)
#                 # first_time = i[j]
#                 #wave median
#                 # if first_time != i[0] and time_active > 18:
#                 #     print(df["timestamp"][0])
#                 #     print("id: ",df["id"][ind],"\n wave short:",wave_short,"\n wave median:",time_active,"\n timestart:",i[0],"\n timeend:",i[j])
#                 #     break
#                 # dic_time.setdefault(df["id"][ind],time_active)
#                 # print(first_time," ",j) 
#                 # print(dic_time)
#     try:
#         s_wave_short.append(wave_short[0]) if wave_short[0] != 0 or wave_short[0] is not None else None
#     except:
#         pass
#     try:
#         for k in range(0,len(wave_short),1):
#             if wave_short[k] >= (wave_short[0])*2:
#                 s_wave_mean.append(wave_short[k])
#                 print("id: ",df["id"][ind],"\n wave short:",wave_short[0] if wave_short[0] != 0 else None,"\n wave median: ",wave_short[k],"\n timestart:",i[0],"\n timeend:",i[j],"\n time cham nguong: ",cham_nguong[0])
#                 # print("thoi gian tu luc cham nguong toi luc vuot nguong: ",wave_short[0] - cham_nguong[0])
#                 for k1 in range(k,len(wave_short),1):
#                     if wave_short[k1] > (wave_short[k])*2:
#                         s_wave_long.append(wave_short[k1])
#                         break
#                 break
#     except:
#         try:
#             print("id: ",df["id"][ind],"\n wave short:",wave_short[0] if wave_short[0] != 0 else None,"\n timestart:",i[0],"\n timeend:",i[j],"\n time cham nguong: ",cham_nguong[0])
#         except:
#             pass
#     wave_short = []
#     cham_nguong = []
#     ind += 1
    
#     #if ind == 2: 
# print("wave ngan: ",s_wave_short,"\n Thoi gian (trung vi) de co mot song ngan: ",statistics.median(s_wave_short),"\n wave trung binh: ",s_wave_mean,"\nThoi gian (trung vi) de co mot song trung binh: ",statistics.median(s_wave_mean),"\n wave long: ",s_wave_long) 






