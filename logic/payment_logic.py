from calculus.models import ProductPayment
import pandas as pd
import numpy as np
from user.models import User

def payment_report(user , qs , get_queryset):
       
        
        reports = []

        qs_for_sub = []

        buyers = []

        for_whos = []

        for q in qs:
            buyers.append(q.buyer.id)
            for_whos.append(q.for_who.id)
        
        buyers = User.objects.order_by('id').all()

        for_whos = User.objects.order_by('id').all()

       
        matrix = np.zeros((len(buyers) , len(for_whos)))

        
        print(buyers)
        print(for_whos)




        for i in range(len(buyers)+1):
            for j in range(len(for_whos)+1):
                try:
                   
                    for p in ProductPayment.objects.filter(buyer = i , for_who = j).values('price'):

                        matrix[i-1][j-1] += p['price']
                        
                except Exception as e:
                    pass



        print(matrix)



        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                try:
                    if matrix[i][j] > matrix[j][i]:
                        matrix[i][j] = matrix[i][j] - matrix[j][i]
                        matrix[j][i] = 0

                    if matrix[i][j] < matrix[j][i]:
                        matrix[j][i] = matrix[j][i] - matrix[i][j]
                        matrix[i][j] = 0
                   
                except:
                    pass

        print(matrix)
        for i in range(1,matrix.shape[0]+1):
            for j in range(1,matrix.shape[1]+1):
                
                
                if i == j:
                    continue
                

                if i != user.id and j != user.id:
                    continue
    
                print(i,j)

                try:

                    if matrix[i-1][j-1] != 0 :
                        buyer = i
                        for_who = j
                        price = matrix[i-1][j-1]

                        reports.append(f'{User.objects.get(id=for_who)} pay  toman {price} to {User.objects.get(id=buyer)}')
                except Exception as e:
                    print(e)
            


       

        return reports