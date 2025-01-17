# -*- coding: utf-8 -*-
# Source: pydpi-1.0
"""
################################################################################################

This module is used to download the protein sequence from the uniprot (http://www.uniprot.org/) 

website. You can only need input a protein ID or prepare a file (ID.txt) related to ID. You can

 obtain a .txt (ProteinSequence.txt) file saving protein sequence you need.  You can freely use 
 
 and distribute it. If you hava  any problem, you could contact with us timely!
 
Authors: Dongsheng Cao and Yizeng Liang.

Date: 2012.9.3

Email: oriental-cds@163.com

################################################################################################
"""

import urllib
import string
##################################################################################################
def GetProteinSequence(ProteinID):
	"""
	#########################################################################################
	Get the protein sequence from the uniprot website by ID.
	
	Usage:
	
	result=GetProteinSequence(ProteinID)
	
	Input: ProteinID is a string indicating ID such as "P48039".
	
	Output: result is a protein sequence.
	#########################################################################################
	"""

	ID=str(ProteinID)
	localfile=urllib.urlopen('http://www.uniprot.org/uniprot/'+ID+'.fasta')
	temp=localfile.readlines()
        res=''
        try:
            gene_name = temp[0].split('GN=')[1].split(' ')[0]
            print(gene_name)
        except:
            pass
	for i in range(1,len(temp)):
		res=res+string.strip(temp[i])
	return gene_name+','+res
##################################################################################################
def GetProteinSequenceFromTxt(path,openfile,savefile):
	"""
	#########################################################################################
	Get the protein sequence from the uniprot website by the file containing ID.
	
	Usage: 
	
	result=GetProteinSequenceFromTxt(path,openfile,savefile)
	
	Input: path is a directory path containing the ID file such as "/home/orient/protein/" 
	
	openfile is the ID file such as "proteinID.txt"
	
	savefile is the file saving the obtained protein sequences such as "protein.txt"
	#########################################################################################
	"""
	f1=file(path+savefile,'wb')
	f2=file(path+openfile,'r')
        header = ',sequence'
        f1.write(header+'\n')
#	res=[]
	for index,i in enumerate(f2):
		
		itrim=string.strip(i)
		if itrim == "":
			continue
		else:
			temp=GetProteinSequence(itrim)
			print "--------------------------------------------------------"
			print "The %d protein sequence has been downloaded!" %(index+1)
			print temp
			f1.write(temp+'\n')
			print "--------------------------------------------------------"
#		res.append(temp+'\n')
#	f1.writelines(res)
	f2.close()
	f1.close()
	return 0

##################################################################################################
if __name__=='__main__':
	
	import os
	path=os.getcwd()  ##please run the script in the directory containing the files
	path="/Users/gvin/pki_paper_work/Kinase_pKI/pydpi_2/protein/"
        savefile=file(path+'/result.txt','wb')
	localfile=file(path+'/target.txt','r')
#	res=[]
	for index,i in enumerate(localfile):
		itrim=string.strip(i)
		if itrim == "":
			continue
		else:
			temp=GetProteinSequence(itrim)
			print "--------------------------------------------------------"
			print "The %d protein sequence has been downloaded!" %(index+1) 
			print temp
			savefile.write(temp+'\n')
			print "--------------------------------------------------------"
#			res.append(temp+'\n')
#	savefile.writelines(res)
	localfile.close()
	savefile.close()

	flag=GetProteinSequenceFromTxt("/Users/gvin/pki_paper_work/Kinase_pKI/pydpi_2/protein/","target.txt","result.txt")
	print flag


