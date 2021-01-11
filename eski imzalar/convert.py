import matplotlib.pyplot as plt
import numpy as np
import os
from skimage.transform import resize

def crop_and_return_min_mn_for_a_folder(folder_name):
    # for resize
    min_m_for_all,min_n_for_all=0,0
    files=get_all_files_in_folder(folder_name)
    i=0
    for file in files:
        full_file_name=folder_name+"/"+file
        print(file,end=" " )
        print(full_file_name)

        try:

            im_rgb=plt.imread(full_file_name)
            im_bw=convert_rgb_to_bw(im_rgb)
            mbr=get_MBR_from_a_bwImage(im_bw)
            im_bw_cropped=crop_an_image_by_new_mn(im_bw,mbr)
            if(i==0):

                min_m_for_all,min_n_for_all=im_bw_cropped.shape
            else:
                if (min_m_for_all>im_bw_cropped.shape[0]):
                    min_m_for_all=im_bw_cropped.shape[0]
                if (min_n_for_all>im_bw_cropped.shape[1]):
                    min_n_for_all=im_bw_cropped.shape[1]

            new_file_name=file[0:-4] + "_cropped" + file[-4:]
            print("_cropped")
            full_file_name=new_path+"/"+new_file_name
            plt.imsave(full_file_name,im_bw_cropped,cmap='gray')
            # print(new_file_name)
        except:
            print("error in "+file)
    print(" finished ...")

    return min_m_for_all,min_n_for_all
def convert_rgb_to_bw(im_rbg):
    try :

        im_rbg=im_rbg/np.max(im_rbg)

        m=im_rbg.shape[0]
        n=im_rbg.shape[1]
        my_new_image=np.zeros((m,n),dtype=int)

        for row in range(m):
            for column in range(n):
                s=im_rbg[row,column,0]/3+im_rbg[row,column,1]/3+im_rbg[row,column,2]/3
                img_avg=np.mean(im_rbg)
                img_std=np.std(im_rgb)
                # diff_to_0=s-0
                # diff_to_1=np.abs(1-diff_to_0)

                if s<img_std:
                    my_new_image[row,column]=0
                else:
                    my_new_image[row,column]=1

        return my_new_image
    except:
        print(" convert_rgb_to_bw da hata oluştu ....")
def get_all_folders_in_path(path_=""):
    my_folders=[folder for folder in os.listdir(path_) if os.path.isdir(path_ + '/'+str(folder))]
    return my_folders
def get_all_files_in_folder(path_=""):
    my_files=[file for file in os.listdir(path_) if os.path.isfile(path_ + '/'+str(file))]
    return my_files
def get_my_files(data_folder_1):
    #data_folder_1=r"C:\\Users\\ikahraman\\lab_files_for_courses_synch_with_github\\data_signature\\987654321\\"
    files=get_all_files_in_folder(data_folder_1)
    return files
def get_MBR_from_a_bwImage(im_bw):

    # for smallest biggest m
    m,n=im_bw.shape[0],im_bw.shape[1]

    smallest_m=m

    biggest_m=0

    for i in range(m):
        for j in range(n):
            intensity=im_bw[i,j]
            if (intensity==0 and i<smallest_m):
                smallest_m=i
            if (intensity==0 and i>biggest_m):
                biggest_m=i

    # for smallest biggest n
    smallest_n=n
    biggest_n=0
    for i in range(m):
        for j in range(n):
            intensity=im_bw[i,j]
            if (intensity==0 and j<smallest_n):
                smallest_n=j
            if (intensity==0 and j>biggest_n):
                biggest_n=j
    smallest_n,biggest_n
    smallest_m,biggest_m

    m1,m2,n1,n2=smallest_m,biggest_m,smallest_n,biggest_n

    return m1,m2,n1,n2
def crop_an_image_by_new_mn(im_bw,mbr):

    m1,m2,n1,n2=mbr[0],mbr[1],mbr[2],mbr[3]

    m,n=m2-m1,n2-n1
    my_new_image=np.zeros((m,n),dtype=int)
    my_new_image=im_bw[m1:m2+1,n1:n2+1]

    return my_new_image
def my_cropp_process():
    data_folder_1=r"/home/thmyris/Desktop/tes/170401001"
    print("took address")
    files=get_my_files(data_folder_1)
    print("got files", files)
    for file in files:

        full_file_name=data_folder_1+"/"+file

        im_1=plt.imread(full_file_name)
        im_2=convert_rgb_to_bw(im_1)
        # (im_1.ndim,im_1.shape),(im_2.ndim,im_2.shape)
        mbr=get_MBR_from_a_bwImage(im_2)
        im_3=crop_an_image_by_new_mn(im_2,mbr)

        size=(200,200)

        im_4=resize(im_3,size)


        # (im_3.ndim,im_3.shape)

        #     plt.subplot(1,3,1),plt.imshow(im_1)
        #     plt.subplot(1,3,2),plt.imshow(im_2,cmap='gray')
        #     plt.subplot(1,3,3),plt.imshow(im_3,cmap='gray')
        #     plt.show()

        a=file
        #a="1234567890.png"
        i=len(a)-4
        b=a[0:-4]+"_cropped_"+a[i:]
        print(a)
        print(b)
        full_file_name=data_folder_1+"/"+b
        full_file_name

        plt.imsave(full_file_name,im_4,cmap='gray')
def convert_rgb_to_bw(im_rbg):

        im_rbg=im_rbg/np.max(im_rbg)
        # m,n,k=im_rbg.shape
        m=im_rbg.shape[0]
        n=im_rbg.shape[1]

        my_new_image=np.zeros((m,n),dtype=int)
        my_new_image=my_new_image+1

        for row in range(m):
            for column in range(n):

                s=im_rbg[row,column,0]/3+im_rbg[row,column,1]/3+im_rbg[row,column,2]/3

                diff_to_0=s-0
                diff_to_1=np.abs(1-diff_to_0)

                if diff_to_0<diff_to_1:
                    my_new_image[row,column]=0
                else:
                    my_new_image[row,column]=1

        return my_new_image

my_cropp_process()
