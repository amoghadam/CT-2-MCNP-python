# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 23:25:36 2011

@author: mazdak


"""
import numpy
arand=rand(60,60,60)
pic=(numpy.array(2000)*numpy.array(arand))
#pic=[int(2000*z) for z in y: for y in x: for x in picudfg]
#pic=[[[2,3,-1000,5],[2,3,4,6]],[[2,3,4,7],[2,3,4,8]]];
presenceof1=0;
presenceof2=0;
presenceof3=0;
presenceof4=0;
presenceof5=1;
lumanxsize=1.2;
lumanysize=1.2;
lumanzsize=4.8;
catheter_positionx=6.6;
catheter_positiony=0.4;
catheter_positionz=-3.4;
if presenceof1 :
    source1_rel_pos=0.2;
    amnspd1=' d4'
    amnspd1p=' 1'
else:
    source1_rel_pos=-lumanzsize-0.8;
    amnspd1=''
    amnspd1p=''
    
if presenceof2 :
    source2_rel_pos=-0.2
    amnspd2=' d5'
    amnspd2p=' 1'
else:
    source2_rel_pos=-lumanzsize-0.8;
    amnspd2=''
    amnspd2p=''
    
if presenceof3 :
    source3_rel_pos=0.6;
    amnspd3=' d7'
    amnspd3p=' 1'
else:
    source3_rel_pos=-lumanzsize-0.8;
    amnspd3=''
    amnspd3p=''

if presenceof4:
    source4_rel_pos=-0.4;
    amnspd4=' d6'
    amnspd4p=' 1'
else:
    source4_rel_pos=-lumanzsize-0.8;
    amnspd4=''
    amnspd4p=''

if presenceof5:
    source5_rel_pos=0;
    amnspd5=' d3'
    amnspd5p=' 1'
else:
    source5_rel_pos=-lumanzsize-0.8;
    amnspd5=''
    amnspd5p=''


import time
cc=time.localtime()
Dateyear=cc.tm_year
Datemonth=cc.tm_mon
Dateday=cc.tm_mday
Datehour=cc.tm_hour
Datemin=cc.tm_min
Datesec=cc.tm_sec
wrightwait=20;    
filenameoo='';
pathoo='';
lastrun={'partnum2sim':2000}
lastrun['numberofsymiulations']=1
lastrun['airloestden']=-1000
lastrun['maxima']=1400;
lastrun['minimin']=-1000;
maxima=lastrun['maxima'];
minimin=lastrun['minimin'];
#                                      -150
lastrun['mat_discriminator']= [ minimin , -880 ,   -150,  -2 , 1 , 185 ,    maxima ]
flesh=1080;
lastrun['selectedmatterial']=[ 1 , 11,   10,  8,  4,  5 ]
    

amxs=numpy.size(pic,0)
amys=numpy.size(pic,1)
amzs=numpy.size(pic,2)
lastrun['xsize']=amxs;
lastrun['ysize']=amys;
lastrun['zsize']=amzs;
lastrun['meshxsize']=amxs;
lastrun['meshysize']=amys;
lastrun['meshzsize']=amzs;

lastrun['meshxsize2']=2;
lastrun['meshysize2']=2;
lastrun['meshzsize2']=2;
lastrun['filenameoo']=filenameoo;
lastrun['pathoo']=pathoo;
lastrun['piciinp1']=175;
lastrun['piciinp2']=175;
lastrun['piciinp3']=45;
lastrun['piciinp4']=325;
lastrun['piciinp5']=325;
lastrun['piciinp6']=110;
lastrun['piciinp7']=1;


lastrun['dimx']=0.2;
lastrun['dimy']=0.2;
lastrun['dimz']=0.2;
lastrun['meshdimx']=0.2;
lastrun['meshdimy']=0.2;
lastrun['meshdimz']=0.2;


lastrun['meshdimx2']=0.6;
lastrun['meshdimy2']=0.6;
lastrun['meshdimz2']=0.6;
lastrun['alphabet']=1;
lastrun['savefilename']=['patient1','.mat'];

xsize=lastrun['xsize']
ysize=lastrun['ysize']
zsize=lastrun['zsize']    
meshxsize=lastrun['meshxsize']
meshysize=lastrun['meshysize']
meshzsize=lastrun['meshzsize']
meshxsize2=lastrun['meshxsize2']
meshysize2=lastrun['meshysize2']
meshzsize2=lastrun['meshzsize2']
#%rhodata=zeros((xsize*ysize*zsize),1);
#%picdata=zeros((xsize*ysize*zsize),1);
dosedata=numpy.zeros([(meshxsize*meshysize*meshzsize),1]);
erordata=numpy.zeros([(meshxsize*meshysize*meshzsize),1]);
dosedata2=numpy.zeros([(meshxsize2*meshysize2*meshzsize2),1]);
erordata2=numpy.zeros([(meshxsize2*meshysize2*meshzsize2),1]);



partnum2sim=lastrun['partnum2sim']
numberofsymiulations=lastrun['numberofsymiulations']
airloestden=lastrun['airloestden']
maxima=lastrun['maxima']
minimin=lastrun['minimin']
mat_discriminator=lastrun['mat_discriminator']
selectedmatterial=lastrun['selectedmatterial']
xsize=lastrun['xsize']
ysize=lastrun['ysize']
zsize=lastrun['zsize']
meshxsize=lastrun['meshxsize']
meshysize=lastrun['meshysize']
meshzsize=lastrun['meshzsize']
meshxsize2=lastrun['meshxsize2']
meshysize2=lastrun['meshysize2']
meshzsize2=lastrun['meshzsize2']
filenameoo=lastrun['filenameoo']
pathoo=lastrun['pathoo']
piciinp1=lastrun['piciinp1']
piciinp2=lastrun['piciinp2']
piciinp3=lastrun['piciinp3']
piciinp4=lastrun['piciinp4']
piciinp5=lastrun['piciinp5']
piciinp6=lastrun['piciinp6']
piciinp7=lastrun['piciinp7']
dimx=lastrun['dimx']
dimy=lastrun['dimy']
dimz=lastrun['dimz']
meshdimx=lastrun['meshdimx']
meshdimy=lastrun['meshdimy']
meshdimz=lastrun['meshdimz']
meshdimx2=lastrun['meshdimx2']
meshdimy2=lastrun['meshdimy2']
meshdimz2=lastrun['meshdimz2']
alphabet=lastrun['alphabet']
savefilename=lastrun['savefilename']
differa=maxima-minimin;

import scipy.io
datam=scipy.io.loadmat('miumat.mat')

total_miu=datam['total_miu']
mat_names=datam['mat_names']
CT_det=datam['CT_det']
mat_gray=datam['mat_gray']


kvp=CT_det[0][0]*1e-3;
kvp=150*(1e-3);
bmd=CT_det[0][1];

len_disc=len(mat_discriminator)-1;
lsm=len(selectedmatterial)-1;
miu_ov_rhos=numpy.zeros([1,lsm]);
miu_ov_rhos_at20=numpy.zeros([1,lsm]);
i2=0;
miu_ov_rhos=[];
miu_ov_rhos_at20=[];

while i2<=lsm :
    miu_ov_rhos=miu_ov_rhos+[sum((kvp==((total_miu[:,0,(selectedmatterial[i2]-1)])))*((total_miu[:,1,(selectedmatterial[i2]-1)])))]
    miu_ov_rhos_at20=miu_ov_rhos_at20+[sum((0.02==(total_miu[:,0,(selectedmatterial[i2]-1)]))*((total_miu[:,1,(selectedmatterial[i2]-1)])))]
    i2=i2+1;
    
i2=0;
nmiu_ov_rhos=[];
while i2<=lsm :
    nmiu_ov_rhos=nmiu_ov_rhos+list([total_miu[list(total_miu[:,0,(selectedmatterial[i2]-1)]).index(kvp),1,(selectedmatterial[i2]-1)]])
    #print(nmiu_ov_rhos)
    #print(i2)
    i2=i2+1;
    
    


  

kvp    
water_miu=sum(numpy.array(kvp==((total_miu[:,0,7])))*(numpy.array((total_miu[:,1,7]))))


rho_scalermat1=1e-3
miu_scalermat1=miu_ov_rhos[0]*rho_scalermat1;
rho_scalermat2=bmd;
miu_scalermat2=miu_ov_rhos[lsm]*rho_scalermat2;

i1=0;
materialmat=range(minimin,maxima+1);
dsicedmat=numpy.array(numpy.zeros([maxima-minimin+1]));

while i1<len_disc:
    absu=numpy.array([(mat_discriminator[i1]<u<=mat_discriminator[i1+1])*selectedmatterial[i1] for u in materialmat])
    dsicedmat=dsicedmat+absu
    i1=i1+1
    
i1=0;
mius_over_ros_mat_at20=numpy.array(numpy.zeros([maxima-minimin+1]));
mius_over_ros_mat=numpy.array(numpy.zeros([maxima-minimin+1]));
while i1<len_disc:
    absu=numpy.array([(u==selectedmatterial[i1])*miu_ov_rhos[i1] for u in dsicedmat])
    mius_over_ros_mat=mius_over_ros_mat+absu;
    absu=numpy.array([(u==selectedmatterial[i1])*miu_ov_rhos_at20[i1] for u in dsicedmat])
    mius_over_ros_mat_at20=mius_over_ros_mat_at20+absu;
    i1=i1+1
    
rhosmat=((((numpy.array(materialmat)))*(numpy.array(water_miu)/1000))+numpy.array(water_miu))/(numpy.array(mius_over_ros_mat));
materialmat=numpy.array(materialmat)-(mat_discriminator[0]);
rhosmat[0]=0;
materialmat[0]=0;
# mcnp even
#tic
cylrad=0.032;
cylradthic=0.04;
cylhight=0.4834;
capthick=0.0083;
Irho=4.930;
sylvrho=4.540;
import os

if os.access("meshtal", os.F_OK):    
    os.remove('meshtal')
        
#move ami.txt to a safe place
#delete('ami.txt')
if os.access("mctal", os.F_OK):
    os.remove('mctal')
        
if os.access("runtpe", os.F_OK):
    os.remove('runtpe')
    
filename='ats.txt';
if xsize%2==0:
    latxmin=-dimx;
    latymin=-dimy;
    latzmin=-dimz;
    latxmax=0;
    latymax=0;
    latzmax=0;
else :
    latxmin=-dimx/2;
    latymin=-dimy/2;
    latzmin=-dimz/2;
    latxmax=dimx/2;
    latymax=dimy/2;
    latzmax=dimz/2;
    


minxgrid=-(xsize*dimx)/2;
minygrid=-(ysize*dimy)/2;
minzgrid=-(zsize*dimz)/2;
maxxgrid=(xsize*dimx)/2;
maxygrid=(ysize*dimy)/2;
maxzgrid=(zsize*dimz)/2;
meshminxgrid=-(meshxsize*meshdimx)/2;
meshminygrid=-(meshysize*meshdimy)/2;
meshminzgrid=-(meshzsize*meshdimz)/2;
meshmaxxgrid=(meshxsize*meshdimx)/2;
meshmaxygrid=(meshysize*meshdimy)/2;
meshmaxzgrid=(meshzsize*meshdimz)/2;
meshminxgrid2=-(meshxsize2*meshdimx2)/2;
meshminygrid2=-(meshysize2*meshdimy2)/2;
meshminzgrid2=-(meshzsize2*meshdimz2)/2;
meshmaxxgrid2=(meshxsize2*meshdimx2)/2;
meshmaxygrid2=(meshysize2*meshdimy2)/2;
meshmaxzgrid2=(meshzsize2*meshdimz2)/2;
#matnumnums=(
matnums=materialmat;
maxmatnum=numpy.max(matnums);
romat=rhosmat;
mode='p';
mode2='e';
xmode='n';
emode='0';
phmode='1';
nmode='0';
for inum in range(alphabet,numberofsymiulations+1) :
    print(savefilename)
    print(inum)
    aplok=numpy.array(pic)-(mat_discriminator[0])
    a=[(x>0)*x for x in aplok]
    rhoinp=numpy.zeros([amxs,amys,amzs])
    for k in range(len(matnums)):
        abtu=numpy.array([(x==matnums[k])*romat[k] for x in a])
        print(k)
        rhoinp=rhoinp+abtu
        
    print(rhoinp)
    pics=[x+((matnums[-1]+4)*(x==0)) for x in a]
    sx,sy,sz=amxs,amys,amzs
    pics2u=flesh*numpy.ones([2,2,2]);
    if sx%2==1:
        gzindm=1;
        gzindp=2;
        vyindm=1;
        vyindp=2;
        zeindm=1;
        zeindp=2;
        sx1p=round(sx/2);
        sx1m=-(round(sx/2)); 
        atxm=(sx1m*dimx)-((1/2)*dimx);
        atxp=(sx1p*dimx)+((1/2)*dimx);
    else:
        gzindm=1;
        gzindp=2;
        vyindm=1;
        vyindp=2;
        zeindm=1;
        zeindp=2;
        sx1p=round(sx/2)-1;
        sx1m=-(round(sx/2));
        atxm=-(sx/2)*dimx;
        atxp=(sx/2)*dimx;
        
    if sy%2==0:
        sy1p=round(sy/2)-1;
        sy1m=-(round(sy/2));
        atym=-(sy/2)*dimy;
        atyp=(sy/2)*dimy;
    else:
        sy1p=round(sy/2);
        sy1m=-(round(sy/2)); 
        atym=(sy1m*dimy)-((1/2)*dimy);
        atyp=(sy1p*dimy)+((1/2)*dimy);
        
    if sz%2==0:
        sz1p=round(sz/2)-1;
        sz1m=-(round(sz/2));
        atzm=-(sz/2)*dimz;
        atzp=(sz/2)*dimz;
    else:
        sz1p=round(sz/2);
        sz1m=-(round(sz/2)); 
        atzm=(sz1m*dimz)-((1/2)*dimz);
        atzp=(sz1p*dimz)+((1/2)*dimz);
        
    fid=open(filename,'w')
    R=numpy.sqrt((dimx**2)+(dimy**2)+(dimz**2))
    fid.write('sdim simulation\n')
    fid.write('c  cell defenitions\n')
    fid.write('30201     22  -22.42 (-1 -8 9 ):(-2 8 ):(-3 -9 ) u=1 \n')
    fid.write('          imp:n='+nmode+' imp:p='+phmode+' imp:e='+emode+'\n')
    fid.write('32011     22  -22.42 (-11 -81 91 ):(-12 81 ):(-13 -91 ) u=1 \n')
    fid.write('          imp:n='+nmode+' imp:p='+phmode+' imp:e='+emode+'\n')
    fid.write('32021     22  -22.42 (-21 -82 92 ):(-22 82 ):(-23 -92 ) u=1 \n')
    fid.write('          imp:n='+nmode+' imp:p='+phmode+' imp:e='+emode+'\n')
    fid.write('32031     22  -22.42 (-31 -84 94 ):(-32 84 ):(-33 -94 ) u=1 \n')
    fid.write('          imp:n='+nmode+' imp:p='+phmode+' imp:e='+emode+'\n')
    fid.write('32041     22  -22.42 (-41 -83 93 ):(-42 83 ):(-43 -93 ) u=1 \n')
    fid.write('          imp:n='+nmode+' imp:p='+phmode+' imp:e='+emode+'\n')
    fid.write('30202     24   -8.02 -4  -851 951 #30201  u=1  \n')
    fid.write('          imp:n='+nmode+' imp:p='+phmode+' imp:e='+emode+'\n')
    fid.write('32012     24   -8.02 -14 -861 961 #32011 u=1 \n')
    fid.write('          imp:n='+nmode+' imp:p='+phmode+' imp:e='+emode+'\n')
    fid.write('32022     24   -8.02 -24 -871 971 #32021 u=1 \n')
    fid.write('          imp:n='+nmode+' imp:p='+phmode+' imp:e='+emode+'\n')
    fid.write('32032     24   -8.02 -34 -881 981 #32031 u=1 \n')
    fid.write('          imp:n='+nmode+' imp:p='+phmode+' imp:e='+emode+'\n')
    fid.write('32042     24   -8.02 -44 -891 991 #32041 u=1  \n')
    fid.write('          imp:n='+nmode+' imp:p='+phmode+' imp:e='+emode+'\n')    
    fid.write('30203     24   -6.45 -99 -951 -7  u=1  \n')
    fid.write('          imp:n='+nmode+' imp:p='+phmode+' imp:e='+emode+'\n')
    fid.write('32013     24   -6.45 -99 -961 -17 u=1  \n')
    fid.write('          imp:n='+nmode+' imp:p='+phmode+' imp:e='+emode+'\n')
    fid.write('32023     24   -6.45 -99 -971 -27 u=1  \n')
    fid.write('          imp:n='+nmode+' imp:p='+phmode+' imp:e='+emode+'\n')
    fid.write('32033     24   -6.45 -99 -981 -37 u=1  \n')
    fid.write('          imp:n='+nmode+' imp:p='+phmode+' imp:e='+emode+'\n')
    fid.write('32043     24   -6.45 -99 -991 -47 u=1  \n')
    fid.write('          imp:n='+nmode+' imp:p='+phmode+' imp:e='+emode+'\n')
    fid.write('30204     28 -0.001086 -99 -5 #30201 #30202 #30203     u=1 \n')
    fid.write('          imp:n='+nmode+' imp:p='+phmode+' imp:e='+emode+'\n')
    fid.write('32014     28 -0.001086 -99 -15 #32011 #32012 #32013 u=1 \n')
    fid.write('          imp:n='+nmode+' imp:p='+phmode+' imp:e='+emode+'\n')
    fid.write('32024     28 -0.001086 -99 -25 #32021 #32022 #32023 u=1 \n')
    fid.write('          imp:n='+nmode+' imp:p='+phmode+' imp:e='+emode+'\n')
    fid.write('32034     28 -0.001086 -99 -35 #32031 #32032 #32033 u=1 \n')
    fid.write('          imp:n='+nmode+' imp:p='+phmode+' imp:e='+emode+'\n')
    fid.write('32044     28 -0.001086 -99 -45 #32041 #32042 #32043 u=1 \n')                            
    fid.write('          imp:n='+nmode+' imp:p='+phmode+' imp:e='+emode+'\n')
    fid.write('30205     25   -1.42 5 -6 -99   u=1 \n')
    fid.write('          imp:n='+nmode+' imp:p='+phmode+' imp:e='+emode+'\n')
    fid.write('32015     25   -1.42 15 -16 -99 u=1  \n')
    fid.write('          imp:n='+nmode+' imp:p='+phmode+' imp:e='+emode+'\n')
    fid.write('32025     25   -1.42 25 -26 -99 u=1  \n')
    fid.write('          imp:n='+nmode+' imp:p='+phmode+' imp:e='+emode+'\n')
    fid.write('32035     25   -1.42 35 -36 -99 u=1 \n')
    fid.write('          imp:n='+nmode+' imp:p='+phmode+' imp:e='+emode+'\n')
    fid.write('32045     25   -1.42 45 -46 -99 u=1  \n')
    fid.write('          imp:n='+nmode+' imp:p='+phmode+' imp:e='+emode+'\n')
    fid.write('30207     25   -1.42 99 -100 u=1   \n')
    fid.write('          imp:n='+nmode+' imp:p='+phmode+' imp:e='+emode+'\n')
    fid.write('30206     23   -1.06 6 16 26 36 46 -99 u=1 \n')
    fid.write('          imp:n='+nmode+' imp:p='+phmode+' imp:e='+emode+'\n')
    fid.write('32016     23   -1.06 -102 -99 6 16 26 36 46 u=1 \n')
    fid.write('          imp:n='+nmode+' imp:p='+phmode+' imp:e='+emode+'\n')
    fid.write('30208     0         101 u=1 \n')
    fid.write('          imp:n='+'0'+' imp:p='+'0'+' imp:e='+'0'+'\n')
    fid.write('30107     25   -1.42 100 u=1   \n')
    fid.write('          imp:n='+nmode+' imp:p='+phmode+' imp:e='+emode+'\n')
    # in the following lines the change in y and z dimentions from matlab to python may cause error
    alkix=round(((round((-(atxm-catheter_positionx))/dimx)*dimx)+(atxm-catheter_positionx)))
    Ncatheter_positionx=catheter_positionx-alkix
    alkiy=round(((round((-(atym-catheter_positiony))/dimy)*dimy)+(atym-catheter_positiony)))
    Ncatheter_positiony=catheter_positiony-alkiy
    alkiz=round(((round((-(atzm-catheter_positionz))/dimz)*dimz)+(atzm-catheter_positionz)))
    Ncatheter_positionz=catheter_positionz-alkiz
    lumanxm=round((lumanxsize/dimx)+0.0001);
    lumanym=round((lumanysize/dimy)+0.0001);
    lumanzm=round((lumanzsize/dimz)+0.0001);
    amindexs=round(((-Ncatheter_positionx-atxm)/dimx)-(round((lumanxm/2)+0.00001)-1)+0.00001);
    amindeys=round(((-Ncatheter_positiony-atym)/dimy)-(round((lumanym/2)+0.00001)-1)+0.00001);
    amindezs=round(((-Ncatheter_positionz-atzm)/dimz)-(round((lumanzm/2)+0.00001)-1)+0.00001);
    amindex=round(((-Ncatheter_positionx-atxm)/dimx)+0.00001);
    amindey=round(((-Ncatheter_positiony-atym)/dimy)+0.00001);
    amindez=round(((-Ncatheter_positionz-atzm)/dimz)+0.00001);
    anonumus1=[3,4,13,15,16,18,19,21,22,24,33,34];
    anonumus=anonumus1;
    for iluman in range(2,int(lumanzm+1)):
        anonumus=anonumus+([int(x+((iluman-1)*lumanxm*lumanym)) for x in anonumus1])
    
    lenumus=len(anonumus);
    #Sindmat=numpy.zeros([3,lenumus]);
    def giveindex(i,sx,sy,sz):
        if i>1:
            indz=int((i-2)/(sx*sy))+1
            if indz>sz:
                print('warning: index out of matrix extension')
                
            indy=int((i-1-((indz-1)*sx*sy))/sx)+1
            indx=i-((indz-1)*sx*sy)-((indy-1)*sx);
        else :
            indz=1;
            indy=1;
            indx=1
        
        return indx,indy,indz
    
    #probably not needed
    sindmat=[];    
    for ilumat in range(1,lenumus+1) :
        Xin,Yin,Zin=giveindex(5,24,24,24)
        sindmat.append([Xin+amindexs-((amxs/2)+1),Yin+amindeys-((amys/2)+1),Zin+amindezs-((amzs/2)+1)])
    #        
    anonumus=[ (x+4) for x in anonumus]
    
    lumanuniversmap=numpy.zeros([lumanxm,lumanym,lumanzm]);
    fid.write('3003 0  996 994 -997 -995 998 -999 u=2 fill=1 imp:n='+nmode+' imp:p='+phmode+' imp:e='+emode+'\n')
    unison=1;
    for bark in range(1,int(lumanzm+1)):
        for barj in range(1,int(lumanym+1)):
            for bari in range(1,int(lumanxm+1)):
                if ((-(lumanxsize/2)+((bari-1)*dimx))<0.0001) & ((-(lumanxsize/2)+((bari-1)*dimx))>-0.0001):
                    felakat_amirx=int((-(lumanxsize/2)+((bari-1)*dimx)+0.0002))
                else:
                    felakat_amirx=(-(lumanxsize/2)+((bari-1)*dimx))
                    
                if ((-(lumanysize/2)+((barj-1)*dimy))<0.0001) & ((-(lumanysize/2)+((barj-1)*dimy))>-0.0001):
                    felakat_amiry=int((-(lumanysize/2)+((barj-1)*dimy)+0.0002));
                else:
                    felakat_amiry=(-(lumanysize/2)+((barj-1)*dimy));
                    
                if ((-(lumanzsize/2)+((bark-1)*dimz))<0.0001) & ((-(lumanzsize/2)+((bark-1)*dimz))>-0.0001):
                    felakat_amirz=int((-(lumanzsize/2)+((bark-1)*dimz)+0.0002))
                else:
                    felakat_amirz=(-(lumanzsize/2)+(((bark-1)*dimz)))
                    
                fid.write(str(unison+3)+' like 3003 but trcl ('+str(felakat_amirx)+' '+str(felakat_amiry)+' '+str(felakat_amirz)+') u='+str(unison+3)+'\n')
                lumanuniversmap[bari-1,barj-1,bark-1]=unison+3;
                unison=unison+1;
                
            
        
    
    pics=numpy.array(pics)+4000
    for indz in range(int(amindezs),int(amindezs+lumanzm)):
        for indy in range (int(amindeys),int(amindeys+lumanym)):
            for indx in range (int(amindexs),int(amindexs+lumanxm)):
                pics[indx,indy,indz]=lumanuniversmap[indx-amindexs,indy-amindeys,indz-amindezs]
            
        
    
    #line 739 matlab code
    ap=len(matnums)
    print(str(matnums[len(matnums)-1]))
    fid.write(str(matnums[len(matnums)-1]+4004)+' 0 '+'-221'+' '+'u='+str(matnums[len(matnums)-1]+4004)+' '+'imp:'+xmode+'=0'+' '+'imp:'+mode+'=1 imp:e='+emode+'\n')
    aj=1; 
    while aj<ap:
        fid.write(str(matnums[aj]+4000)+' '+str(dsicedmat[aj])+' '+str(-romat[aj])+' '+'-221'+' '+'u='+str(matnums[aj]+4000)+' '+'imp:'+xmode+'=0'+' '+'imp:'+mode+'=1 imp:e='+emode+'\n')
        aj=aj+1
    
    fid.write(str(matnums[aj-1]+1)+' '+'0'+' '+'2210 -2211 2212 -2213 2214 -2215 '+'lat=1 '+'u='+str(matnums[aj-1]+1)+' '+'imp:'+xmode+'=0'+' '+'imp:'+mode+'=1 imp:e='+emode+'\n')
    fid.write('     fill='+str(sx1m)+':'+str(sx1p)+' '+str(sy1m)+':'+str(sy1p)+' '+str(sz1m)+':'+str(sz1p)+'\n')
    
    #a waitbar needed
    #h = waitbar(0,'Please wait...');
    
    ts=(sx*sy*sz)
    i=1
    while i<ts:
        stri='     ';
        while len(stri)<(70-len(str((ts)-i))):
            stri=stri+' '+str(pics[giveindex(i,sx,sy,sz)]);
            i=i+1
            if i>ts:
                break
            
            j=0;
            while pics[giveindex(i,sx,sy,sz)]==pics[giveindex(i-1,sx,sy,sz)]:
                j=j+1
                i=i+1
                if i>ts:
                    break
                
            
            if j==1:
                stri=stri+' '+str(pics[giveindex(i-1,sx,sy,sz)])
            elif j>1:
                stri=stri+' '+str(j)+'R'
                
            if i>ts:
                break
            
        
        fid.write(stri+'\n')
        
    
                
                    
                
            
        
    
        
    
    fid.close()
    



    




def importdatam(filenamoo):    
    import csv
    spamReader = csv.reader(open(filenamoo, 'rb'), delimiter=',')
    i=0;
    for row in spamReader:    
        b=[]
        for x in row:
                if x!='': 
                    b.append([numpy.double(x)])
        
        
        a.append(b)
        print i
        print a
        i=i+1
    
    return a
        
filenamoo='o7.dat'
ziba=importdatam('o7.dat')        

 


#for x in inu:
    
#    abs=array([(u==x)*(1200+x) for u in vec])
#    tbs=tbs+abs
    

#dsicedmat=[];
#while i1<len_disc:
    #dsicedmat=dsicedmat+((selectedmatterial[i1])*((materialmat>mat_discriminator[i1])*(materialmat<=mat_discriminator[i1+1])));
    #i1=i1+1;


#data = {}
#data['xios'] = maxima
#scipy.io.savemat('test.mat',data)

ce=[3,1,5,2]
asd=numpy.array(ce)
vv=5*(asd==3)
#pickle.dump(x, f)
#To unpickle the object again, if f is a file object which has been opened for reading:
#x = pickle.load(f)

#matplotlib.mlab.load
    

#a, b = 0, 1
#>>> while b < 1000:
# if it was print b    then numbers apeared one in a line
#..     print b,
#...     a, b = b, a+b
#...
#1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987

#range(5, 10)
#[5, 6, 7, 8, 9]
#>>> range(0, 10, 3)
#[0, 3, 6, 9]

#a = ['Mary', 'had', 'a', 'little', 'lamb']
#>>> for i in range(len(a)):
#...     print i, a[i]
#...
#0 Mary
#1 had
#2 a

#define a function
#def fib(n):    
#statements that form the body of the function start at the next line, and must be indented.
#return result



# ~=   =   !=
#norm = %  6%5  =>1



# len(s)

#    %&&&&&&&&&&&&&&&&&&&&&&&&&&&&
 #   lastrun['partnum2sim=2000;
