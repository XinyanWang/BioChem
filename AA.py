# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 09:59:32 2015

@author: xinyan wang
"""

from random import randint as randint
import sqlite3

def getplace():
    this_file=inspect.getfile(inspect.currentframe())  
    path=os.path.abspath(os.path.dirname(this_file))  
    return path

def create():
    AA=[['丙氨酸','Ala','A','Alanine','alanine'],
        ['精氨酸','Arg','R','Arginine','arginine'],
        ['天冬氨酸','Asp','D','Aspartic acid','aspartic_acid'],
        ['半胱氨酸','Cys','C','Cysteine','cysteine'],
        ['谷氨酰胺','Gln','Q','Glutamine','glutamine'],
        ['谷氨酸','Glu','E','Glutamic acid','glutamic_acid'],
        ['组氨酸','His','H','Histidine','histidine'],
        ['异亮氨酸','Ile','I','Isoleucine','isoleucine'],
        ['甘氨酸','Gly','G','Glycine','glycine'],
        ['天冬酰胺','Asn','N','Asparagine','asparagine'],
        ['亮氨酸','Leu','L','Leucine','leucine'],
        ['赖氨酸','Lys','K','Lysine','lysine'],
        ['甲硫氨酸','Met','M','Methionine','methionine'],
        ['苯丙氨酸','Phe','F','Phenylalanine','phenylalanine'],
        ['脯氨酸','Pro','P','Proline','proline'],
        ['丝氨酸','Ser','S','Serine','serine'],
        ['苏氨酸','Thr','T','Threonine','threonine'],
        ['色氨酸','Trp','W','Tryptophan','tryptophan'],
        ['酪氨酸','Tyr','Y','Tyrosine','tyrosine'],
        ['缬氨酸','Val','V','Valine','valine']]
        
    AAdb=sqlite3.connect('AA.db')
    AAdb.execute('create table AA (CNname,Three,One,Engname,pic)')
    for i in AA:
        AAdb.execute('insert into AA (CNname,Three,One,Engname,pic) \
        values ("%s","%s","%s","%s","%s")'%(i[0],i[1],i[2],i[3],getplace()+'\\pic\\'+i[4]+'.gif'))
    AAdb.commit()
    AAdb.close()
    

def makequiz():
    AAdb=sqlite3.connect('AA.db')
    AA=AAdb.execute('select * from AA').fetchall()
    quiz=[]
    for i in range(len(AA)):
        quiz+=[AA.pop(randint(1,len(AA))-1)]
    return quiz
    
def main():
    quiz=makequiz()
    right1=[]
    
    while True:
        #将quiz刷入right1
        t=0
        anstype=[[0,'CNname'],[3,'ENname'],[2,'1letter'],[1,'3letters']]
        pop=randint(0,3)
        if pop==1:
            popr=3
        elif pop==3:
            popr=1
        else:
            popr=pop
        print (anstype.pop(pop)[1]+': '+quiz[0][popr] )
        for j in anstype:
            ans=input("%s: "%j[1])
            if ans!=quiz[0][j[0]]:
                print ('Wrong. The answer is %s'%quiz[0][j[0]] )
                print ('======')
                t=1
                break
        print('======')
        if t!=1:
            quiz.pop(0)
        else:
            temp=quiz.pop(0)
            quiz+=[temp]
        if len(quiz)==0:
            break
        
    print  ('Task is over' )
    
if __name__=='__main__':
    main()
    
    
    
    

