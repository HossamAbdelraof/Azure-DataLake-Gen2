# Azure-DataLake-Gen2
manage Azure DataLake Gen 2 with python 


first install required libraries 

```python
pip install azure-storage-file-datalake
```

this python file provide important actions with azure Blob storage (DataLAke Gen2)

* here will manage directories (navigation, create, rename, delate)
* working with files(upload text file, upload big file)

## First 
import libraries

```python
from azure.storage.filedatalake import DataLakeServiceClient
from azure.core.exceptions import ResourceExistsError
```

### authorication 

Create Service Client 

```python
Storage_Account_url = "https://{Storate_Account_Name}.dfs.core.windows.net/"

Storage_Account_credential = '{Access_Key}'

DataLake_service = DataLakeServiceClient(account_url = Storage_Account_url,
                   credential = Storage_Account_credential)

```



## 1- manage directories

##### 1.1 create file systems 
to create 

```python
  File_Sistem_Client = DataLake_service.create_file_system(file_system = {File_System_Name})
```
> this code create file system with name of: {File_System_Name}
>  replace {File_System_Name} with any other name

 to load existing file system 
 ```python
  File_Sistem_Client = DataLake_service.get_file_system_client( {File_System_Name} )
 ```
 > this code will load an existing fileSystem (container) with the name: {File_System_Name}

#####1.1.2 Directories
create directories we must use 
 ```python
 Directory_Client = File_Sistem_Client.create_directory("my-directory")
  ```
  > the directorise must be inside File system so we use current file system client (File_Sistem_Client) \n
  > teh directory can be any number of folders like: " folder1\folder2\folder3 "

we can consider teh directory is child of File System and we can access teh child only of oyher directories 
```python
 Directory_Client  = File_Sistem_Client.get_directory_client(" folder1\folder2 ")
 Directory_Client = Directory_Clien.get_directory_client(" folder3 ")
```

##### 1.2 Rename

to rename file system or directory just use .rename_directory() method

```python
 Directory_Client =  Directory_Clien.rename_directory(new_name= "{New_Name}")
```

##### 1.3 Delete 

to deleate file system or Directory just use use 
```python
 Directory_Client.delete_directory()
```

##### 1.4 get directory contents
to get the content of crrent directory just use .get_paths() method
> .get_paths() return array of objects (PathProperties Class)
Each object have { name, owner, permissions, last_modifiedm , is_directory, etc..} fields that return data abon it's name

```python
 objjects = Directory_Client.get_paths()
 
 for object in objects:
     print( object.name )
```

##### 2 Upload File


to upload file we havemany steps
1- navigate directory
2- create target file 
3- read and upload file

to upload file we have 2 methods 
1- if the file is text based file (.csv, .tsv, .txt, etc..)
2- if the file of others types (.pdf, .jpeg, .mp4, .rar, etc..)

####  2.1 upload text based file:

```python
def upload_TextBased_file():
    try:

        file_system_client =datalake_service.get_file_system_client( {File_System_Name} )

        directory_client = file_system_client.get_directory_client( "my-directory" )
        
        file_client = directory_client.create_file ( "{file_name}.{Extinction}" )

        source_file = open("file",'rb')

        source_file_contents = local_file.read()

        file_client.append_data(data=source_file_contents, offset=0, length=len(file_contents))
         
        file_client.flush_data(len(source_file_contents))

    except Exception as e:
      print(e)
```

to  uploadany file tybe use this function 
```python
def upload_file():
    try:

        file_system_client =datalake_service.get_file_system_client( {File_System_Name} )

        directory_client = file_system_client.get_directory_client( "my-directory" )
        
        file_client = directory_client.create_file ( "{file_name}.{Extinction}" )

        source_file = open("file",'rb')

        source_file_contents = local_file.read()

        file_client.upload_data(source_file_contents, overwrite=True)

    except Exception as e:
      print(e)
```

