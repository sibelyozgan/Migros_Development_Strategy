import math

def distance(lat1, lat2, lng1, lng2):

    lat1 = math.radians(lat1)
    lon1 = math.radians(lng1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lng2)
    a = (math.sin((lat2 - lat1)/2))**2 + math.cos(lat1) * math.cos(lat2) * (math.sin((lon2 - lon1)/2))**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    dist = 6373 * c

    return dist




def av_dist(stores_lat,stores_lng,closer):
    distance_list=[]
    min_dist=[]
    
    for i in range(len(stores_lat)):
        for j in range(len(stores_lat)):
            
              distance_list.append(distance(stores_lat[i],stores_lat[j],stores_lng[i],stores_lng[j]))
                
        l1 = sorted(distance_list)[:closer]
        min_dist.append(sum(l1)/(closer-1))
        
    return sum(min_dist)/len(min_dist)



def dis_rad(stores_lat,stores_lng,mesh_lat,mesh_lng,RAD):
    index_list=[]

    for i in range(len(stores_lat)):
        for j in range(len(mesh_lat)):

             if lib_dist.distance(stores_lat[i],mesh_lat[j],stores_lng[i],mesh_lng[j])<RAD:
                index_list.append(j)
    return index_list