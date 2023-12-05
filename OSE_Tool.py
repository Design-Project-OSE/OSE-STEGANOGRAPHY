import os

class Name_Detect:
    def file_name_controller(self,patch,search):
        save_loc="Project_Tools\\"
        list_patch=os.listdir(save_loc)
        if len(list_patch)==0:
            name=patch_search+'0'+'.wav'
        else:   
            last_file=list_patch[-1] 
            index_start=last_file.rfind(search)
            index_start=index_start+search.__len__()
            index_end=last_file.rfind('.')
            number=last_file[index_start:index_end]
            number=str(int(number)+1)
            name=save_loc+search+number+'.wav'
        return name


    def name_check(self,loc_dir):
        index_start=loc_dir.rfind("/")
        index_final=loc_dir.rfind(".")
        name=loc_dir[index_start+1:index_final]
        return name