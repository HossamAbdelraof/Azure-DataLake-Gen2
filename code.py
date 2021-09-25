from azure.storage.filedatalake import DataLakeServiceClient
from azure.core.exceptions import ResourceExistsError


## config client
Storage_Account_url = "https://{Storate_Account_Name}.dfs.core.windows.net/"

Storage_Account_credential = '{Access_Key}'

DataLake_service = DataLakeServiceClient(account_url = Storage_Account_url,
                   credential = Storage_Account_credential)



## try to open file system or create new one
try:
  File_Sistem_Client = DataLake_service.get_file_system_client( {File_System_Name} )
except ResourceExistsError:
  File_Sistem_Client = DataLake_service.create_file_system(file_system = {File_System_Name})

    
## try to open dircetory or create new one
 try:
   Directory_Client  = File_Sistem_Client.get_directory_client(" folder1\folder2 ")
 except ResourceExistsError:
  Directory_Client = File_Sistem_Client.create_directory("my-directory")

  
##rename directory
Directory_Client =  Directory_Clien.rename_directory(new_name= "{New_Name}")

## create  new directory and delete it
Directory_Client_n = File_Sistem_Client.create_directory("folder3")

Directory_Client_n.delete_directory()


## upload  file to DataLake
def upload_TextBased_file(data_dir):
    try:
        data_name= data_dir.split("\\")[-1] 
        file_client = directory_client.create_file ( data_name )

        source_file = open(data_dir,'rb')

        source_file_contents = local_file.read()

        file_client.append_data(data=source_file_contents, offset=0, length=len(file_contents))
         
        file_client.flush_data(len(source_file_contents))

    except Exception as e:
      print(e)

      
## upload  file to DataLake  
def upload_file(data_dir):
    try:

        data_name= data_dir.split("\\")[-1] 
        file_client = directory_client.create_file ( data_name )

        source_file = open("file",'rb')

        source_file_contents = local_file.read()

        file_client.upload_data(source_file_contents, overwrite=True)

    except Exception as e:
      print(e)




