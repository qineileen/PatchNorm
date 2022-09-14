
import torch
def GroupByRelations(adj):
    # Author: Qin Yuxuan, Shanghai Pinghe School
    adj_fornorm = adj         #拷贝一份
    adj_fornorm = adj_fornorm + adj_fornorm.transpose(0, 1)  #转置相加
    adj_fornorm = torch.where(adj_fornorm > 0.0, 1.0, 0.0)    #非零处置1
    sizeofAdj = adj_fornorm.size()[0]
    relationGroups=[]               #initial relations list
    relationGroup={0}               #initial set of first relation group
    noRelationGroup=set()           #initial set of no relation group
    indexUsed=set()                 #initial set of index searched
    relationAll=set(range(0,sizeofAdj))    
    #initial full range of nodes
    relationList=torch.nonzero(adj_fornorm==1.0).squeeze().cpu().numpy()   
    #create relation list from adj
    if len(relationList)==sizeofAdj: 
        return [list(range(0,sizeofAdj)),]      
        #if only self-relations then return full list
    while (len(relationAll) !=0):   #cycle while relations not completed
        relationStart=sorted(relationAll)[0] #initial from first unsearched node
        relationGroup=set([relationStart])
        while (len(relationGroup) != len(indexUsed)):        
            relationStart=sorted(relationGroup-indexUsed)[0]
            indexUsed=indexUsed.union(set([relationStart]))     
            #mark the nodes searched
            selectedRelation=[x for x in relationList if x[:][0]==relationStart ]   
            #filter the relations from given node
                for item in selectedRelation:   
                    relationGroup=relationGroup.union(set(item))    
                    #union the relations into the set
        relationAll=relationAll-relationGroup       #erase from full range of nodes
        relationGroups.append(sorted(relationGroup))        #append relation groups
        indexUsed=set()     #clear index used for next loop
    return relationGroups
    #Qin Yuxuan 2022-8-28 9:34 modified，return relation groups，keep isolated nodes in separated groups (to be optimized)