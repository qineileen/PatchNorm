import torch
import time
def groupByRelations(adj):
    startTime=time.time()   #开始计时
    timeTH=0.5              #时间阈值设为0.5秒
    adj_fornorm=adj
    adj_fornorm=adj_fornorm+adj_fornorm.transpose(0,1)
    adj_fornorm=torch.where(adj_fornorm>0.0,1.0,0.0)
    sizeofAdj = adj_fornorm.size()[0]
    relationGroups=[]#初始化关系集合的列表
    relationGroup={0}               #初始化第一个关系列表
    noRelationGroup=set()           #初始化无关系index
    indexUsed=set()                 #初始化查找过关系index标记
    relationAll=set(range(0,sizeofAdj))     #初始化待询关系集合,即节点号全列表
    relationList=torch.nonzero(adj_fornorm==1).squeeze().cpu().numpy()  #求出其中所有有关系的位置坐标，形成List
    if len(relationList)==sizeofAdj: 
        return [[range(0,sizeofAdj)],]
    while (len(relationAll) != 0):       #当关系没有找完时不断循环，relationAll是待询关系列表
        relationStart = sorted(relationAll)[0] #初始化，从排序后首个节点开始找关系（从小到大开始找关系）
        relationGroup=set([relationStart])  #初始化关系集合
        while (len(relationGroup) != len(indexUsed)):   #indexUsed是relationGroup中找过关系的index集合，如果全部找过结束循环
            relationStart = sorted( relationGroup - indexUsed )[0]  #初始化，从差集排序后首个节点开始找关系（从小到大）
            indexUsed = indexUsed.union(set([relationStart]))       #标记找过关系的index，扩入indexUsed集合
            selectedRelation=[x for x in relationList if x[:][0]==relationStart ]  #筛选有关系的标记
            if len(selectedRelation) != 1:  #关系数超过1即有本身之外关系
                for item in selectedRelation:   
                    relationGroup=relationGroup.union(set(item))     #串联关系集合
                    #relationLeft=relationGroup-set([relationStart])
            else:
                for item in selectedRelation:  
                    noRelationGroup=noRelationGroup.union(set(item))    #将所有孤立节点分入同一集合
        relationAll = relationAll - relationGroup       #删减总关系集合
        if len(relationGroup) != 1:
            relationGroups.append(sorted(relationGroup))         #append关系集合列表
        if (time.time() - startTime) >= timeTH:     #如果运算已经
            noRelationGroup=noRelationGroup.union(relationAll)      #将所有还没来得及找关系的都并入noRelationGroup
            break
        indexUsed=set()     #清空找过关系的index标记    
    relationGroups.append(sorted(noRelationGroup))      #最后把无关系列表noRelationGroup附在列表最后，形成[[关系组1],[关系组2],...,[关系组k],[无关系组]]
    return relationGroups
    #Qin Yuxuan 2022-8-30 11:27 optimized，return relation groups，keep isolated nodes in one group (to avoid single normalization for each isolated node)

